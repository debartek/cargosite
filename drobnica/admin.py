from django.contrib import admin
from .models import *

admin.site.register(Order)
admin.site.register(Shipper)
admin.site.register(Consignee)
admin.site.register(Address)
admin.site.register(Package)
