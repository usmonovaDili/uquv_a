from django.urls import path
from .views import CourseListAPIView, CategoryListAPIView, AboutUsListAPIView, RegistrationListAPIView, \
    TeacherListAPIView, CategoryUpdateListAPIView, CourseUpdateListAPIView

urlpatterns = [
    path('course/', CourseListAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
    path('register/', RegistrationListAPIView.as_view()),
    path('teacher/', TeacherListAPIView.as_view()),
    path('aboutus/', AboutUsListAPIView.as_view()),
    path('update/<int:pk>/', CategoryUpdateListAPIView.as_view()),
    path('updateCourse/<int:pk>/', CourseUpdateListAPIView.as_view()),
]
