from rest_framework import serializers
from .models import Teacher,Student
from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken
# from onlineclass.serializers import OnlineClassSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email", "is_staff","id"]


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Teacher
        fields =" __all__"

    def get_user(self,obj):
        user= obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Student
        fields= "__all__"

    def get_user(self,obj):
        user= obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data


class UserSerializerWithToken(UserSerializer):
    access = serializers.SerializerMethodField(read_only=True)
    refresh = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email", "is_staff","refresh","access"]

    def get_access(self, obj):
        token = RefreshToken.for_user(obj)

        token['username'] = obj.username
        token['first_name'] = obj.first_name
        token['last_name'] = obj.last_name
        token['is_staff'] = obj.is_staff
        token['id'] = obj.id
        return str(token.access_token)
    
    def get_refresh(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)