from django.contrib import admin

# Register your models here.
from flights.models import Passenger, Flight, Airport

admin.site.register(Passenger)
admin.site.register(Airport)
admin.site.register(Flight)