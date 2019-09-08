from rest_framework import serializers
from .models import Profile,Contact,Project
from django.contrib.auth.models import User



class ProfileSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Profile
      fields = ['bio']
class UserSerializer(serializers.ModelSerializer):
   profile = ProfileSerializer('profile')
   class Meta:
      model = User
      fields = ['username','email','profile']

class PrflSerializer(serializers.ModelSerializer):
   user = UserSerializer('user')
   class Meta:
      model = Profile
      fields = ['bio','user']
class  ProjectSerializer(serializers.ModelSerializer):
   author = PrflSerializer('profile')
   class Meta:
      model = Project
      fields = ['name','description','link','author']