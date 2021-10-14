from rest_framework import fields, serializers
from .models import *
from api import models 
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class User_DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Degree
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class Study_leaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Study_leave
        fields = '__all__'

class PendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = '__all__'

class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'