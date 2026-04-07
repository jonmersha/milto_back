from django.db import models
from django.utils import timezone
import uuid

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('driver', 'Driver'),
        ('passenger', 'Passenger'),
        ('admin', 'Admin'),
    ]
    
    uid = models.CharField(max_length=255, primary_key=True)
    display_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    photo_url = models.URLField(max_length=500, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    vehicle_info = models.JSONField(blank=True, null=True) # model, plateNumber, color, seats
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)
    rating_count = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    current_location = models.JSONField(blank=True, null=True) # latitude, longitude, updatedAt
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.display_name

class Ride(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    driver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='offered_rides')
    driver_name = models.CharField(max_length=255)
    origin = models.TextField()
    destination = models.TextField()
    departure_time = models.DateTimeField()
    available_seats = models.IntegerField()
    total_seats = models.IntegerField()
    price_per_seat = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    route = models.JSONField(default=list) # Array of objects {lat, lng}
    passengers = models.JSONField(default=list) # Array of user UIDs
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.origin} to {self.destination}"

class RideRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    passenger = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ride_requests')
    passenger_name = models.CharField(max_length=255)
    ride = models.ForeignKey(Ride, on_delete=models.SET_NULL, null=True, blank=True, related_name='requests')
    origin = models.TextField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    seats = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_given')
    reviewee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_received')
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

class Alert(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('resolved', 'Resolved'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    location = models.JSONField() # latitude, longitude
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(default=timezone.now)

class SOSLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    success = models.BooleanField()
    error = models.TextField(blank=True, null=True)

class Transaction(models.Model):
    METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('telebirr', 'Telebirr'),
        ('cbe_birr', 'CBE Birr'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class LocationSuggestion(models.Model):
    TYPE_CHOICES = [
        ('fuel', 'Fuel'),
        ('atm', 'ATM'),
        ('food', 'Food'),
        ('parking', 'Parking'),
        ('hospital', 'Hospital'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=255)
    location = models.JSONField() # latitude, longitude
    distance = models.DecimalField(max_digits=10, decimal_places=2)
