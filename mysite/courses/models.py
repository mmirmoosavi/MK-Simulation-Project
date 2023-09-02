from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Teacher(BaseModel):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)


class Course(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    published_at = models.DateTimeField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # you cannot create course with price lower than minium_course_price
        # ( MINIMUM_COURSE_PRICE is defined in django settings that preventing hard codes
        # we restrict model level creation object for better coding styles
        # also we apply this restriction in our serializer to show appropriate message to user

        # todo: we can also define pre_save signals for this check it other developers is Ok with django signals
        if self.price < settings.MINIMUM_COURSE_PRICE:
            raise Exception('you cannot create course with price lower than minium_course_price ')
        return super(Course, self).save(force_insert=False, force_update=False, using=None,
                                        update_fields=None)

    class Meta:
        ordering = ['-published_at']


class Review(BaseModel):
    SCORE_CHOICES = (
        (5, "5"),
        (4, "4"),
        (3, "3"),
        (2, "2"),
        (1, "1"),
    )

    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    score = models.SmallIntegerField(choices=SCORE_CHOICES)
