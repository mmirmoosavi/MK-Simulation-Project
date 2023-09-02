from rest_framework.permissions import IsAdminUser


class CustomCoursePermission(IsAdminUser):
    def has_permission(self, request, view):
        # get django user of the request
        django_user = request.user

        # save is_admin_user boolean
        is_admin_user = django_user.is_staff

        if is_admin_user:
            # if admin user call the parent class
            return super(CustomCoursePermission, self).has_permission(request, view)

        # if user not is_admin_user
        # our behavior is:  admin can create and destroy a course

        if view.action in ['create', 'destroy']:
            return bool(django_user and is_admin_user)

        # every users can see list and details of courses
        elif view.action in ['list', 'retrieve']:
            # all users have permissions for list and details of Courses
            return bool(django_user)
        # otherwise we want has_permission return True and check it accesss in has_object_permission for update a course
        else:
            return bool(django_user)

    def has_object_permission(self, request, view, obj):
        django_user = request.user

        is_admin_user = django_user.is_staff
        if is_admin_user:
            # if admin user call the parent class
            return super(CustomCoursePermission, self).has_object_permission(request, view, obj)

        teacher = getattr(django_user, 'teacher', None)

        if teacher and view.action in ['update', 'partial_update']:
            # check the django user is related to teacher or not
            if obj in teacher.course_set.all():
                return True
            else:
                return False
        else:
            return True
