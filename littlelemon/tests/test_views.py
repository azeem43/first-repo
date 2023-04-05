from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(Title="cake",Price="20",Inventory="30")
    
    def test_getall(self):
        item = Menu.objects.all()
        
        for items in item:
            self.assertEqual(items,"cake : 20")        
        
