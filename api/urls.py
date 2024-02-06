from django.urls import path
from .views import LeadList, LeadDetail


urlpatterns = [
    path('<int:pk>/', LeadDetail.as_view(), name='lead_detail'),
    path('', LeadList.as_view(), name='lead_list'),
]
