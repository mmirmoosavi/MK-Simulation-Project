from django.db.models import Count, Avg
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import ListModelMixin

from .permissions import CustomCoursePermission
from .serializers import CourseSerializer, TeacherSerializer, ReviewSerializer
from .models import Course, Teacher, Review


class CourseViewSet(ModelViewSet):
    permission_classes = [CustomCoursePermission]
    queryset = Course.objects.all().select_related('teacher').annotate(
        review_count=Count('review__id'),
        review_score_avg=Avg('review__score')
    )
    serializer_class = CourseSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ReviewViewSet(GenericViewSet,
                    ListModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
