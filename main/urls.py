from django.urls import path


from .views import HomeView, CourseDetailView, CourseListView, AboutView, EnrollCourseView, LessonsListView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('course-detail/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses-list/', CourseListView.as_view(), name='courses-list'),
    path('course-lessons/<int:pk>/', LessonsListView.as_view(), name='course-lessons'),
    path('enroll-course/<int:pk>/', EnrollCourseView.as_view(), name='enroll-course'),
]