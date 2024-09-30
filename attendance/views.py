from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Semester, Course, Class, Lecturer, Student, Enrollment, Attendance
import pandas as pd
from django.contrib.auth import logout
# Home view
@login_required
def home(request):
    is_lecturer = request.user.groups.filter(name="Lecturers").exists()
    is_student = request.user.groups.filter(name="Students").exists()
    is_admin = request.user.is_superuser
    return render(request, 'attendance/home.html', {
        'is_lecturer': is_lecturer,
        'is_student': is_student,
        'is_admin': is_admin,
    })

# Custom Admin login view
class AdminLoginView(LoginView):
    template_name = 'attendance/admin_login.html'
    redirect_authenticated_user = True  # Redirects if the user is already authenticated

# Custom Lecturer login view
class LecturerLoginView(LoginView):
    template_name = 'attendance/lecturer_login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Log out the user if already logged in
            logout(request)
        return super().dispatch(request, *args, **kwargs)


# Custom Student login view
class StudentLoginView(LoginView):
    template_name = 'attendance/student_login.html'
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True

# Custom General login view for other users
class CustomLoginView(LoginView):
    template_name = 'attendance/login.html'
    redirect_authenticated_user = True

# Redirect user after login
def login_redirect(request):
    return redirect('home')  # After successful login, redirect to home page

# Logout view
class CustomLogoutView(LogoutView):
    next_page = 'home'  # Redirect to home after logout


# Semester CRUD views
class SemesterListView(LoginRequiredMixin, ListView):
    model = Semester
    template_name = 'attendance/semester_list.html'


class SemesterCreateView(LoginRequiredMixin, CreateView):
    model = Semester
    fields = ['year', 'name', 'start_date', 'end_date']
    template_name = 'attendance/semester_form.html'
    success_url = reverse_lazy('semester_list')


class SemesterUpdateView(LoginRequiredMixin, UpdateView):
    model = Semester
    fields = ['year', 'name', 'start_date', 'end_date']
    template_name = 'attendance/semester_form.html'
    success_url = reverse_lazy('semester_list')


class SemesterDeleteView(LoginRequiredMixin, DeleteView):
    model = Semester
    template_name = 'attendance/semester_confirm_delete.html'
    success_url = reverse_lazy('semester_list')


# Administrator CRUD for Courses
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'attendance/course_list.html'
    login_url = 'admin_login'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['code', 'name', 'semesters']
    template_name = 'attendance/course_form.html'
    success_url = reverse_lazy('course_list')
    login_url = 'admin_login'


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['code', 'name', 'semesters']
    template_name = 'attendance/course_form.html'
    success_url = reverse_lazy('course_list')
    login_url = 'admin_login'


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'attendance/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')
    login_url = 'admin_login'


# Administrator CRUD for Classes
class ClassListView(LoginRequiredMixin, ListView):
    model = Class
    template_name = 'attendance/class_list.html'
    login_url = 'admin_login'


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    fields = ['number', 'course', 'semester', 'lecturer']
    template_name = 'attendance/class_form.html'
    success_url = reverse_lazy('class_list')
    login_url = 'admin_login'


class ClassUpdateView(LoginRequiredMixin, UpdateView):
    model = Class
    fields = ['number', 'course', 'semester', 'lecturer']
    template_name = 'attendance/class_form.html'
    success_url = reverse_lazy('class_list')
    login_url = 'admin_login'


class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = Class
    template_name = 'attendance/class_confirm_delete.html'
    success_url = reverse_lazy('class_list')
    login_url = 'admin_login'


# Administrator CRUD for Lecturers
class LecturerListView(LoginRequiredMixin, ListView):
    model = Lecturer
    template_name = 'attendance/lecturer_list.html'
    login_url = 'admin_login'


class LecturerCreateView(LoginRequiredMixin, CreateView):
    model = Lecturer
    fields = ['staff_id', 'user', 'full_name']
    template_name = 'attendance/lecturer_form.html'
    success_url = reverse_lazy('lecturer_list')
    login_url = 'admin_login'


class LecturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Lecturer
    fields = ['staff_id', 'user', 'full_name']
    template_name = 'attendance/lecturer_form.html'
    success_url = reverse_lazy('lecturer_list')
    login_url = 'admin_login'


class LecturerDeleteView(LoginRequiredMixin, DeleteView):
    model = Lecturer
    template_name = 'attendance/lecturer_confirm_delete.html'
    success_url = reverse_lazy('lecturer_list')
    login_url = 'admin_login'


# Lecturer Assign/Remove from Class
class LecturerAssignView(LoginRequiredMixin, UpdateView):
    model = Class
    fields = ['lecturer']
    template_name = 'attendance/class_assign_lecturer.html'
    success_url = reverse_lazy('class_list')
    login_url = 'admin_login'


# Administrator CRUD for Students
class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'attendance/student_list.html'
    login_url = 'admin_login'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['student_id', 'user', 'full_name']
    template_name = 'attendance/student_form.html'
    success_url = reverse_lazy('student_list')
    login_url = 'admin_login'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['student_id', 'user', 'full_name']
    template_name = 'attendance/student_form.html'
    success_url = reverse_lazy('student_list')
    login_url = 'admin_login'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'attendance/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
    login_url = 'admin_login'


# Administrator Enroll/Remove Students from Classes
class EnrollmentListView(LoginRequiredMixin, ListView):
    model = Enrollment
    template_name = 'attendance/enrollment_list.html'
    login_url = 'admin_login'


class EnrollStudentCreateView(LoginRequiredMixin, CreateView):
    model = Enrollment
    fields = ['student', 'enrolled_class']
    template_name = 'attendance/enroll_form.html'
    success_url = reverse_lazy('enrollment_list')
    login_url = 'admin_login'


class EnrollStudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Enrollment
    template_name = 'attendance/enrollment_confirm_delete.html'
    success_url = reverse_lazy('enrollment_list')
    login_url = 'admin_login'


# Upload Students from Excel
@login_required(login_url='admin_login')
def upload_students(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        df = pd.read_excel(excel_file)

        for _, row in df.iterrows():
            Student.objects.create(
                student_id=row['student_id'],
                full_name=row['full_name'],
                user=User.objects.create(username=row['username'])
            )
        return redirect('student_list')

    return render(request, 'attendance/upload_students.html')


# Email Students with Poor Attendance
@login_required(login_url='admin_login')
def email_students_with_poor_attendance(request):
    students_with_poor_attendance = Enrollment.objects.filter(attendance__status='Absent').distinct()

    for enrollment in students_with_poor_attendance:
        student_email = enrollment.student.user.email
        send_mail(
            'Attendance Alert',
            'You have poor attendance. Please attend your classes.',
            'admin@attendancesystem.com',
            [student_email],
            fail_silently=False,
        )

    return redirect('student_list')


# Lecturer Enter Attendance
@login_required(login_url='lecturer_login')
def enter_attendance(request, class_id):
    enrolled_students = Enrollment.objects.filter(enrolled_class=class_id)

    if request.method == 'POST':
        for enrollment in enrolled_students:
            status = request.POST.get(f'attendance_{enrollment.id}')
            Attendance.objects.create(
                enrollment=enrollment,
                date=datetime.now(),
                status=status
            )
        return redirect('class_list')

    return render(request, 'attendance/enter_attendance.html', {'enrolled_students': enrolled_students})


# Student View Attendance
@login_required(login_url='student_login')
def student_view_attendance(request):
    student = Student.objects.get(user=request.user)
    attendance_records = Attendance.objects.filter(enrollment__student=student)

    return render(request, 'attendance/student_attendance.html', {'attendance_records': attendance_records})
