from rest_framework import serializers
from crm.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'region', 'city')
