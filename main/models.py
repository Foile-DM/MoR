from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Material(models.Model):
    title = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    price_per_one = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        if self.count > 0:
            self.price_per_one = self.price / self.count
        else:
            self.price_per_one = 0.0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
#
#
# @receiver(post_save, sender=Material)
# def recalculate_price_per_one(sender, instance, **kwargs):
#     if instance.count > 0:
#         instance.price_per_one = instance.price / instance.count
#     else:
#         instance.price_per_one = 0.0
#     instance.save()


class Product(models.Model):
    title = models.CharField(max_length=100)
    materials = models.ManyToManyField(Material, through='ProductMaterial')
    cost = models.FloatField(editable=False, default=0)

    def __str__(self):
        return self.title


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product} - {self.material}: {self.quantity}'


@receiver(post_save, sender=ProductMaterial)
def recalculate_product_cost(sender, instance, **kwargs):
    product = instance.product
    materials = product.materials.all()
    total_cost = sum(material.price_per_one * instance.quantity for material in materials)
    product.cost = total_cost
    product.save()
