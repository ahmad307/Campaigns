from django.urls import path, include
from campaign.views import CampaignView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('campaigns', CampaignView)

urlpatterns = [
    path('', include(router.urls)),
]