from django.db import models

from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="teach_course")
    students = models.ManyToManyField(User, related_name="course")
    text = models.TextField()
    rate = models.FloatField()
    skill_level = models.CharField(max_length=50)
    duration = models.FloatField()
    language = models.CharField(max_length=50)
    price = models.FloatField()
    photo = models.ImageField(upload_to="course/images/", null=True)


    # @property
    # def teacher_name(self):
    #     return self.teacher.last_name

    @property
    def student_count(self):
        return self.students.count()

    @property
    def lessons_count(self):
        return self.lessons.count()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='lessons')
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    source = models.CharField(max_length=256, null=True, blank=True)
    text = models.TextField()
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Opinion(models.Model):
    student_name = models.CharField(max_length=50)
    text = models.CharField(max_length=256)
    speciality = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="users/images/", null=True)


class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=126, null=True, blank=True)
    message = models.TextField(null=True, blank=True)





