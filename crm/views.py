from rest_framework import generics

from .models import Lead
from .serializers import LeadSerializer


class LeadsList(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
