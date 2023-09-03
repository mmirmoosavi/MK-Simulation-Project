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
    review_count = IntegerField(read_only=True)
    review_score_avg = FloatField(read_only=True)

    def validate_price(self, value):
        if value < 1000000:
            raise ValidationError(detail={'title': 'cannot create or update course',
                                          'detail': "you cannot create or update "
                                                    "course that price is lower than 100000"})
        return value

    class Meta:
        model = Course
        fields = "__all__"


class CourseBriefSerializer(serializers.ModelSerializer):
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
    course = CourseBriefSerializer()

    class Meta:
        model = Review
        fields = "__all__"
