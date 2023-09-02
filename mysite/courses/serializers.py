from rest_framework import serializers

from .models import Course, Teacher, Review
from accounts.serializers import UserSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer()

    class Meta:
        model = Review
        fields = "__all__"