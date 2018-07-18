from django.contrib import admin

# Register your models here.
from .models import Airport, Passenger, Flight
admin.site.register(Passenger)
admin.site.register(Airport)
admin.site.register(Flight)