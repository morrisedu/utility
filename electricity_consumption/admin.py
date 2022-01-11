from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Electricity)
admin.site.register(CostPerUnit)
admin.site.register(Totals)
admin.site.register(Payments)
admin.site.register(TotalPaid)