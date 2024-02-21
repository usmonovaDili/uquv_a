from rest_framework import serializers
from .models import Category, Course, Teacher, Registration, AboutUs
from django.shortcuts import get_object_or_404


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class CourseSerializes(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'title', 'description', 'category', 'instructor', 'duration_in_hours', 'price', 'created_at', 'updated_at')

    def create(self, validated_data):
        return Course.objects.create(**validated_data)


class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('f_name', 'phone', 'gmail', 'enrolled_at', 'password')


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('l_name',)


class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('title',)
