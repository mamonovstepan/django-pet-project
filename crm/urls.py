from django.urls import path
from .views import LeadsList


urlpatterns = [
    path('', LeadsList.as_view(), name='lead_list')
]
