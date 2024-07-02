from django.utils import timezone
from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=50)
    car_price = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(upload_to = 'car/media/uploads/', blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    quantity = models.IntegerField(default = 0)

    def make_purchase(self, user):
        from profile_user.models import Purchase  # Import inside the method
        if self.quantity > 0:
            Purchase.objects.create(user=user, car=self)
            self.quantity -= 1
            self.save()
            return True
        else:
            return False

    def __str__(self):
        return self.car_name



class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete = models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length=30)
    email = models.EmailField(blank = True, null = True, verbose_name='Contact Email (Optional)')
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Comment by {self.name} on {self.created_on}"