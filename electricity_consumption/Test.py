from django.test import TestCase
from .models import *

class ElectricityTestClass(TestCase):
    # Set up
    def setUp(self):
        self.JuneConsumption = Electricity()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.JuneConsumption, Electricity))
    
    def tearDown(self):
        Electricity.objects.all().delete()

class CostPerUnitTestClass(TestCase):
    #Set up
    def setUp(self):
        self.CostOfUnit = CostPerUnit
    
    def test_instance(self):
        self.assertTrue(isinstance(self.CostOfUnit, CostPerUnit))
    
    def tearDown(self):
        CostPerUnit.objects.all().delete()