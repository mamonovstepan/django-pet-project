from rest_framework import generics
from crm.models import Lead
from .serializers import LeadSerializer


class LeadList(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class LeadDetail(generics.RetrieveAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
