from django.test import TestCase
from .models import Images,Location,Category

# Create your tests here.

# images class test case

class ImagesTest(TestCase):
    '''
    test class for Images model
    '''
    def setUp(self):
        '''
        test method to create Image instances called before all tests
        '''
        self.new_category = Category(name='testing')
        self.new_category.save_category()
        
        self.new_location = Location(name='testing')
        self.new_location.save_location()
        
        self.new_picture = Images(image_link='images/picture.jpeg', name='Name title', description='Random description', category=self.new_category, location=self.new_location)
        self.new_picture.save_image()
        self.another_picture = Images(image_link='images/photo.jpg', name='name', description='sth else more random', category=self.new_category, location=self.new_location)
        self.another_picture.save_image()

    def tearDown(self):
        '''
        test method to delete Image instances after each test is run
        '''
        Category.objects.all().delete()
        Location.objects.all().delete()
        Images.objects.all().delete()

    def test_instances(self):
        '''
        test method to assert instances created during setUp
        '''
        self.assertTrue(isinstance(self.new_picture,Images))
        self.assertTrue(isinstance(self.new_category, Category))
        self.assertTrue(isinstance(self.new_location, Location))

    def test_save_image(self):
        '''
        test method to ensure an Image instance has been correctly saved
        '''
        self.assertTrue(len(Images.objects.all()) == 2)

    def test_delete_image(self):
        '''
        test method to ensure an Image instance has been correctly deleted
        '''
        self.new_picture.delete_image()
        self.assertTrue(len(Images.objects.all()) == 1)

    def test_update_image(self):
        '''
        test method to ensure an Image instance has been correctly updated
        '''
        update_test = self.new_picture.update_image('images/updated.png')
        self.assertEqual(update_test.image_link, 'images/updated.png')

    def test_get_all(self):
        '''
        test method to ensure all instances of Image class have been retrieved
        '''
        pictures = Images.get_all()
      

    def test_get_image_by_id(self):
        '''
        test method to ensure Image instances can be retrieved by id
        '''
        obtained_image = Images.get_image_by_id(self.another_picture.id)
       

    def test_search_image(self):
        '''
        test method to ensure correct searching of an multiple image instances by category
        '''
        obtained_image = Images.search_image(self.new_picture.category)
        

    def test_filter_by_location(self):
        '''
        test method to obtain image insatnces by location
        '''
        obtained_image = Images.filter_by_location(self.another_picture.location)
        print(obtained_image)

# Category test method
