from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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


class CourseWriteSerializer(serializers.ModelSerializer):
    review_count = IntegerField()
    review_score_avg = FloatField()

    def validate_price(self, value):
        if value < 1000000:
            raise ValidationError(detail={'title': 'cannot create course',
                                  'detail': "you cannot create course that price is lower than 100000"})

    class Meta:
        model = Course
        fields = "__all__"


class CourseReadSerializer(serializers.ModelSerializer):
    teacher = TeacherBriefSerializer()
    review_count = IntegerField()
    review_score_avg = FloatField()

    class Meta:
        model = Course
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseReadSerializer()

    class Meta:
        model = Review
        fields = "__all__"
