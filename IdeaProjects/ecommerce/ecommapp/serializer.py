from rest_framework import serializers
from ecommapp.models import *
from django.contrib.auth.models import User


class AdminSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())
    job_title = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Admin.objects.create(**validated_data)

    def details(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.job_title = validated_data.get('job_title', instance.job_title)
        instance.save()
        return instance

