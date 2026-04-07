from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    UserProfile, Ride, RideRequest, Review, 
    Alert, SOSLog, Transaction, Message, LocationSuggestion
)
from .serializers import (
    UserProfileSerializer, RideSerializer, RideRequestSerializer, 
    ReviewSerializer, AlertSerializer, SOSLogSerializer, 
    TransactionSerializer, MessageSerializer, LocationSuggestionSerializer
)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['role', 'is_verified']
    search_fields = ['display_name', 'email']

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['driver', 'status']
    ordering_fields = ['departure_time', 'created_at']

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['passenger', 'ride', 'status']

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reviewer', 'reviewee', 'ride']

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'status']

class SOSLogViewSet(viewsets.ModelViewSet):
    queryset = SOSLog.objects.all()
    serializer_class = SOSLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'success']

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ride', 'user', 'status', 'method']

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ride', 'sender']

class LocationSuggestionViewSet(viewsets.ModelViewSet):
    queryset = LocationSuggestion.objects.all()
    serializer_class = LocationSuggestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
