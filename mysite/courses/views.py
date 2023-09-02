from django.db.models import Count, Avg
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import ListModelMixin

from .permissions import CustomCoursePermission
from .serializers import CourseReadSerializer, CourseWriteSerializer, TeacherSerializer, ReviewSerializer
from .models import Course, Teacher, Review


class CourseViewSet(ModelViewSet):
    permission_classes = [CustomCoursePermission]
    queryset = Course.objects.all().select_related('teacher').annotate(
        review_count=Count('review__id'),
        review_score_avg=Avg('review__score')
    )

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update', 'create','destroy']:
            return CourseWriteSerializer
        else:
            return CourseReadSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ReviewViewSet(GenericViewSet,
                    ListModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
