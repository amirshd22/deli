from users.serializers import UserSerializer
from rest_framework import serializers
from .models import OnlineClass, OnlineClassItems, Reviews,Subject,Category,Comments

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields = "__all__"

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = "__all__"

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comments
        fields ="__all__"

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reviews
        fields ="__all__"

class OnlineClassItemsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=OnlineClassItems
        fields="__all__"

    def get_comments(self,obj):
        comments = obj.comments_set.all().order_by("-createdAt")
        serializer = CommentsSerializer(comments , many=True)
        return serializer.data

class OnlineClassSerializer(serializers.ModelSerializer):
    onlineclassitems= serializers.SerializerMethodField(read_only=True)
    reviews= serializers.SerializerMethodField(read_only=True)
    teacher= serializers.SerializerMethodField(read_only=True)
    class Meta:
        model =OnlineClass
        fields ="__all__"
    
    def get_onlineclassitems(self,obj):
        onlineclassitems=  obj.onlineclassitems_set.all()
        serializer = OnlineClassItemsSerializer(onlineclassitems , many=True)
        return serializer.data

    def get_reviews(self,obj):
        reviews = obj.reviews_set.all().order_by("-createdAt")
        serializer = ReviewsSerializer(reviews , many=True)
        return serializer.data

    # TODO : add UserSerializer to this place
    def get_teacher(self,obj):
        teacher = obj.teacher
        serializer = UserSerializer(teacher, many=False)
        return serializer.data
    