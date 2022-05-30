from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    description = models.TextField()
   

# category model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def save_category(self):
        self.save()

    def update_category(self):
        self.update()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


# location model

class Location(models.Model):
    name = models.CharField(max_length=50)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

