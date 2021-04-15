from rest_framework import serializers
from core.models import creds

class credSerializer(serializers.ModelSerializer):
    class Meta:
        model=creds
        fields=['project_name','secret_key','database_host','database_user','database_password','database_name']

