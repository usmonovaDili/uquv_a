from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructor = models.CharField(max_length=100)
    duration_in_hours = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Registration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    gmail = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.f_name} enrolled in {self.course.title}"


class AboutUs(models.Model):
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title


class Teacher(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    l_name = models.CharField(max_length=40)
    picture = models.ImageField(upload_to='add_pic')
    # level=models.CharField(max_length=100)

    def __str__(self):
        return self.l_name

