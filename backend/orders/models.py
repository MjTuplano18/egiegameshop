from django.db import models

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.productName} in {self.cart.user.username}'s cart"

class OrderDetails(models.Model):
    user = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, related_name='orders')
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    discount = models.ForeignKey('products.Discount', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity}x {self.product.productName} in Order #{self.order.id}"

class Payment(models.Model):
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, related_name='payments')
    provider = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"

class Shipping(models.Model):
    user = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, related_name='shipping')
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, related_name='shipping')
    trackingNumber = models.CharField(max_length=100)
    address = models.TextField()
    shippingMethod = models.CharField(max_length=50)
    shippedAt = models.DateTimeField(null=True, blank=True)
    deliveredAt = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Shipping for Order #{self.order.id}"

class OrderReport(models.Model):
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, related_name='reports')
    reportText = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for Order #{self.order.id}"
