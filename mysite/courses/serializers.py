from rest_framework import serializers
from rest_framework.fields import IntegerField, FloatField

from .models import Course, Teacher, Review
from accounts.serializers import UserSerializer


class TeacherBriefSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ('id', 'user')


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherBriefSerializer()
    review_count = IntegerField()
    review_score_avg = FloatField()

    class Meta:
        model = Course
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer()

    class Meta:
        model = Review
        fields = "__all__"
