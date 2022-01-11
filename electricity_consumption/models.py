from django.db import models

# Create your models here.
class Electricity(models.Model):
    inputDate = models.DateField(auto_now_add=True, editable=True)
    inputTime = models.TimeField(auto_now_add=True)
    reading = models.DecimalField(max_digits=9, decimal_places=2)
    unitsUsed = models.DecimalField(max_digits=9, decimal_places=2)
    unitsCost = models.DecimalField(max_digits=9, decimal_places=2)

    costPerUnit = 30

    """
    Django takes cares of the def __init__ part
    def __init__(self, inputDate=None, inputTime=None, currentReading=0, unitsUsed=0, unitsCost=0):
        self.inputDate = inputDate
        self.inputTime = inputTime
        self.reading = currentReading
        self.unitsUsed = unitsUsed
        self.unitsCost = unitsCost
    """
    
    def save_electricity(self):
        self.save()
    
    def delete_electricity(self):
        self.delete()
    
    def update_electricity(self):
        # Method to update an existing entry
        pass
    
    def __str__(self):
        return "Meter Reading: {}, Date Read: {}".format(self.reading, self.inputDate)
    
    class Meta:
        ordering = ["inputDate"]

    @classmethod
    def units_used(cls, currentReading):
        # Method to calculate the number of units used
        previousReading = cls.objects.all().order_by("-inputDate")[:1]
        return currentReading - previousReading

    @classmethod
    def unit_cost(cls, unitsUsed):
        # Method to calculate total cost of unit used
        return CostPerUnit.objects.filter(id=0)

class CostPerUnit(models.Model):
    unitCost = models.IntegerField()

    @classmethod
    def set_cost_per_unit(cls, cost):
        ed1 = cls.object.filter(id=0)
        ed1.unitCost = cost
        ed1.save()

class Totals(models.Model):
    TotalCostOverTime = models.DecimalField(max_digits=9, decimal_places=2)

class Payments(models.Model):
    for_month = models.ForeignKey(Electricity, on_delete=models.CASCADE)
    expected_payment = models.DecimalField(max_digits=9, decimal_places=2)
    total_paid = models.IntegerField()
    payment_date = models.DateField(auto_now_add=True)

class TotalPaid(models.Model):
    TotalPayment = models.DecimalField(max_digits=9, decimal_places=2)