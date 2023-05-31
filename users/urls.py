from django.urls import path, include

from .views import UserCourseListView

urlpatterns = [
    path('courses/', UserCourseListView.as_view(), name='user-courses')

]