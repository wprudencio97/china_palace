from django.db import models

# Create your models here.
class MenuItem(models.Model):

    FOOD_CATEGORIES = [
        ('OTHER', 'Other'),
        ('APPETIZERS', 'Appetizers'),
        ('SOUP', 'Soup'),
        ('FRIED_RICE', 'Fried Rice')
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    category = models.CharField(max_length=30, choices=FOOD_CATEGORIES, default=FOOD_CATEGORIES[0])
    picture = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.name}'