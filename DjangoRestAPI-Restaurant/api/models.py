from django.db import models
import uuid


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    address = models.CharField(max_length=300, verbose_name="Address")
    PictureIcon = models.ImageField(upload_to='images/',verbose_name="PictureIcon")
    phone = models.CharField(max_length=10, unique=True, null=True)
    OpeningDays = models.CharField(max_length=50, verbose_name="OpeningDays",default="Monday-Saturday")
    OpeningHours = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    type = models.CharField(max_length=20,
                            choices=[('Appetizers/Starters','Appetizers/Starters'), ('Breakfast','Breakfast'), ('Snacks','Snacks'), ('Lunch','Lunch'),
                                     ('DINNER','DINNER'), ('Beverage','Beverage'),('Desserts','Desserts')])
    Price = models.PositiveIntegerField(help_text="Please fill the price", default=999)
    thumbnail = models.ImageField(upload_to="recipe_thumbnails", default="recipe_thumbnails/default.png")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe = models.ManyToManyField(Recipe)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")

    def __str__(self):
        return self.name
