from django.db.models import Count, Avg
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import ListModelMixin

from .permissions import CustomCoursePermission
from .serializers import CourseReadSerializer, CourseWriteSerializer, TeacherSerializer, ReviewSerializer
from .models import Course, Teacher, Review
from .utils import TeacherCoursePagination


class CourseViewSet(ModelViewSet):
    permission_classes = [CustomCoursePermission]
    queryset = Course.objects.all().select_related('teacher').annotate(
        review_count=Count('review__id'),
        review_score_avg=Avg('review__score')
    )

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update', 'create', 'destroy']:
            return CourseWriteSerializer
        else:
            return CourseReadSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @action(methods=['get'], detail=True, url_path='courses', url_name='courses')
    def courses(self, request, *args, **kwargs):
        # set pagination class for this action
        self.pagination_class = TeacherCoursePagination

        # set course serializer to show the courses of a teacher
        self.serializer_class = CourseReadSerializer

        queryset = Course.objects.filter(teacher__id=kwargs.get('pk')).select_related('teacher').annotate(
            review_count=Count('review__id'),
            review_score_avg=Avg('review__score')
        )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ReviewViewSet(GenericViewSet,
                    ListModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # get django user
        django_user = self.request.user
        # return review of specific django_user only
        return Review.objects.filter(user=django_user)