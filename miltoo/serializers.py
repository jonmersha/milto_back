from rest_framework import serializers
from .models import (
    UserProfile, Ride, RideRequest, Review, 
    Alert, SOSLog, Transaction, Message, LocationSuggestion
)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'

class SOSLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOSLog
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class LocationSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationSuggestion
        fields = '__all__'
