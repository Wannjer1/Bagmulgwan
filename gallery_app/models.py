
from django.db import models

# Create your models here.
class Images(models.Model):
    image_link = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def save_image(self):
        '''Method to save the image'''
        self.save()

    def delete_image(self):
        '''Method to delete the image'''
        self.delete()

    @classmethod
    def get_all(cls):
        '''
        method to retrieve all images
        '''
        pics = Images.objects.all()
        return pics

    @classmethod
    def get_image_by_id(cls, id):
        '''
        method to retrieve images by unique id
        '''
        retrieved = Images.objects.get(id = id)
        return retrieved

    @classmethod
    def search_image(cls, cat):
        '''
        method to search images by category
        '''
        retrieved = cls.objects.filter(category__name__icontains=cat)
        return retrieved #list of instances

    @classmethod
    def filter_by_location(cls ,location):
        '''
        method to retrive images by their locations
        '''
        retrieved = Images.objects.filter(location__name__icontains=location)
        return retrieved


   

# category model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def save_category(self):
        '''Method to save category'''
        self.save()

    def update_category(self, update):
        '''Method to update category'''
        self.name = update
        self.save()

    def delete_category(self):
        '''Method to delete category'''
        self.delete()

    @classmethod
    def update_category(cls, search_term , new_cat):
        '''
        method to update a category
        '''
        try:
            to_update = Category.objects.get(name = search_term)
            to_update.name = new_cat
            to_update.save()
            return to_update
        except Category.DoesNotExist:
            print('Category you specified does not exist')


    def __str__(self):
        return self.name


# location model

class Location(models.Model):
    name = models.CharField(max_length=50)

    def save_location(self):
        '''Method to save the location'''
        self.save()

    def delete_location(self):
        '''Method to delete the location'''
        self.delete()

    @classmethod
    def update_location(cls, search_term , new_locale):
        '''
        method to update a location's city name
        '''
        try:
            to_update = Location.objects.get(country = search_term)
            to_update.city = new_locale
            to_update.save()
            return to_update
        except Location.DoesNotExist:
            print('Location you specified does not exist')

    @classmethod
    def get_all(cls):
        '''
        method to retrive all stored locations
        '''
        cities = Location.objects.all()
        return cities


    def __str__(self):
        return self.name

