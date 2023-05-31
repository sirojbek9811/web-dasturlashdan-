from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.views import View, generic
from .models import Course, Opinion, Lesson, Contact
from users.models import User


class HomeView(View):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        teachers = User.objects.filter(role="TEACHER")
        opinions = Opinion.objects.all()
        return render(request, 'index.html', context={
                                                "courses": courses,
                                                "teachers": teachers,
                                                "opinions": opinions,
                                                })


class CourseDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            course = Course.objects.get(pk=pk)
        except:
            return redirect('home')
        if request.user.is_authenticated:
            enroll = True if request.user in course.students.all() else False
        else:
            enroll = False
        return render(request, 'detail.html', context={"course": course, 'enroll': enroll})


class CourseListView(generic.ListView):
    model = Course
    queryset = Course.objects.all()
    template_name = 'courses.html'

    # def get_queryset(self):
    #     user = self.request.user
    #     print(user)
    #     object_list = Course.objects.filter(students=user)
    #     print(object_list)
    #     return object_list


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')

    def post(self, request):
        n = request.POST.get('name')
        e = request.POST.get('email')
        s = request.POST.get('subject')
        m = request.POST.get('message')
        try:
            Contact.objects.create(name=n, email=e, subject=s, message=m)
        except:
            pass
        return redirect('home')


class EnrollCourseView(LoginRequiredMixin, View):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except:
            return redirect('home')

        course.students.add(request.user)
        if request.user.is_authenticated:
            enroll = True if request.user in course.students.all() else False
        else:
            enroll = False

        return render(request, 'detail.html', context={"course": course, 'enroll': enroll})

    def post(self, request, pk):
        id=request.POST.get('id')
        try:
            course = Course.objects.get(id=id)
        except:
            return redirect('home')

        course.students.add(request.user)
        if request.user.is_authenticated:
            enroll = True if request.user in course.students.all() else False
        else:
            enroll = False

        return render(request, 'detail.html', context={"course": course, 'enroll': enroll})


class LessonsListView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        lesson_id = self.request.GET.get('lesson', None)
        print(lesson_id)
        try:
            course = Course.objects.get(pk=pk)
        except:
            return redirect('home')
        object_list = Lesson.objects.filter(course_id=pk)

        if lesson_id:
            lesson = Lesson.objects.filter(id=lesson_id).first()
        else:
            lesson = Lesson.objects.filter(course=course, number=1)

        return render(request, 'course-lessons.html', {'lessons': object_list, 'course': course, 'lesson': lesson})




