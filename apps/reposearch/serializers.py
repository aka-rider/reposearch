from .models import RepoSearch
from rest_framework import serializers


class RepoSearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepoSearch
        fields = [
            'id', 'name', 'description', 'web_url', 'created_at', 'updated_at'
        ]
