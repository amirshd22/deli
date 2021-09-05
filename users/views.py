from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Teacher,Student
from .serializers import TeacherSerializer,StudentSerializer,UserSerializerWithToken



# once its registered try to lookup the national code and then set the first_name and last_name to its user


class RegisterView(APIView):
    permission_classes=[AllowAny]
    authentication_classes = []

    def post(self, request):
        data = request.data
        username= data["nationalCode"]
        password = data["password"]
        messages ={ "error": []}
        if username == None:
            messages['errors'].append('username can\'t be empty')
        if password == None:
            messages['errors'].append('Password can\'t be empty')
        if User.objects.filter(username__iexact=username).exists():
            messages['errors'].append("Account already exists with this national id.")
        if len(messages['errors']) > 0:
            return Response({"detail":messages['errors']},status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create(
                username=username,
                password=make_password(password)
            )
            serializer = UserSerializerWithToken(user, many=False)
        except Exception as e:
            print(e)
            return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
        




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_staff'] = user.is_staff
        token['id'] = user.id

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user=  request.user
    profile = Student.objects.get(user=user)
    serializer = StudentSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_profile_pic(request):
    user = Student.objects.get(user= request.user)
    file = request.FILES
    try:
        user.picture = file
        user.save()
        serializer = StudentSerializer(user , many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_profile_details(request):
    user = User.objects.get(user= request.user)
    data = request.data
    try:
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"]
        user.save()
        serializer = StudentSerializer(user , many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
