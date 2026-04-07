from django.contrib import admin
from .models import (
    UserProfile, Ride, RideRequest, Review, 
    Alert, SOSLog, Transaction, Message, LocationSuggestion
)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'email', 'role', 'is_verified')
    search_fields = ('display_name', 'email')

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('driver_name', 'origin', 'destination', 'departure_time', 'status')
    list_filter = ('status', 'departure_time')

@admin.register(RideRequest)
class RideRequestAdmin(admin.ModelAdmin):
    list_display = ('passenger_name', 'ride', 'status', 'created_at')
    list_filter = ('status',)

admin.site.register(Review)
admin.site.register(Alert)
admin.site.register(SOSLog)
admin.site.register(Transaction)
admin.site.register(Message)
admin.site.register(LocationSuggestion)
