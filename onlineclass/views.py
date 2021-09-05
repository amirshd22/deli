
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes

from .models import OnlineClassItems, OnlineClass,Reviews,Comments,Subject
from .serializers import CategorySerializers,ReviewsSerializer,OnlineClassItemsSerializer,SubjectSerializers,OnlineClassSerializer


# Create your views here.

@api_view(["GET"])
def getAllClassess(request):
    allClassess = OnlineClass.objects.all().order_by("-createdAt")
    serializer = OnlineClassSerializer(allClassess, many=True)
    return Response(serializer.data)