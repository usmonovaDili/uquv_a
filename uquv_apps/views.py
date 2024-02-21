from django.shortcuts import render
from .serializers import CategorySerializer, AboutUsSerializers, CourseSerializes, TeacherSerializers, \
    RegistrationSerializers
from rest_framework import generics, status
from .models import AboutUs, Registration, Course, Category, Teacher


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(some_condition=True)


class TeacherListAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers


class CourseListAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializes

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            return Course.objects.filter(category_id=category_id)
        else:
            return Course.objects.all()


class CategoryUpdateListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(some_condition=True)


class RegistrationListAPIView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializers

    def get_queryset(self):
        course_id = self.request.query_params.get('course_id')

        if course_id:
            return Registration.objects.filter(course_id=course_id)
        else:
            return Registration.objects.all()


class AboutUsListAPIView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializers


class CourseUpdateListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializes
