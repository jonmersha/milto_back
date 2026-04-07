from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet, RideViewSet, RideRequestViewSet, 
    ReviewViewSet, AlertViewSet, SOSLogViewSet, 
    TransactionViewSet, MessageViewSet, LocationSuggestionViewSet
)

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'rides', RideViewSet)
router.register(r'ride-requests', RideRequestViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'alerts', AlertViewSet)
router.register(r'sos-logs', SOSLogViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'location-suggestions', LocationSuggestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
