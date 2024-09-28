from django.db import models
from django.contrib.auth.models import User

# Semester Model
class Semester(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.year} - {self.name}"

# Course Model
class Course(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    semesters = models.ManyToManyField(Semester, related_name='courses')

    def __str__(self):
        return f"{self.name} ({self.code})"

# Lecturer Model
class Lecturer(models.Model):
    staff_id = models.IntegerField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

# Class Model
class Class(models.Model):
    number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Class {self.number} - {self.course.name}"

# Student Model
class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

# Enrollment Model
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.full_name} enrolled in Class {self.enrolled_class.number}"

# Attendance Model
class Attendance(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.enrollment.student.full_name} - {self.date} - {self.status}"

# CollegeDay Model (New)
class CollegeDay(models.Model):
    date = models.DateField()
    class_info = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"College Day {self.date} for Class {self.class_info.number}"
