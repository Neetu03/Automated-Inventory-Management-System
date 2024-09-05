from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.dispatch import Signal  # Import Signal class

sell_product =Signal()  # Define sell_product as a Signal

@receiver(pre_save, sender='app.Products')
def sell_product_presave(sender, instance, **kwargs):
    from .models import transactions
    if int(instance.Quantity) < 0:
        instance.Quantity = 0
        t = transactions(ProductID=instance,
                        TransactionType="OUT",
                        Quantity=0,
                        Category=instance.Category)
        t.save()

@receiver(post_save, sender='app.Products')
def sell_product(sender, instance, created, **kwargs):
    from .models import transactions
    if not created:
        t = transactions(ProductID=instance,
                        TransactionType="OUT",
                        Quantity=instance.Quantity,
                        Category=instance.Category)
        t.save()
