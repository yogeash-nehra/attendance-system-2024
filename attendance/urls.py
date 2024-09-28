from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Administrator Login
    path('admin/login/', views.AdminLoginView.as_view(), name='admin_login'),

    # Lecturer Login
    path('lecturer/login/', views.LecturerLoginView.as_view(), name='lecturer_login'),

    # Student Login
    path('student/login/', views.StudentLoginView.as_view(), name='student_login'),

    # Semester CRUD
    path('semesters/', views.SemesterListView.as_view(), name='semester_list'),
    path('semesters/create/', views.SemesterCreateView.as_view(), name='semester_create'),
    path('semesters/<int:pk>/update/', views.SemesterUpdateView.as_view(), name='semester_update'),
    path('semesters/<int:pk>/delete/', views.SemesterDeleteView.as_view(), name='semester_delete'),

    # Course CRUD
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', views.CourseUpdateView.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),

    # Class CRUD
    path('classes/', views.ClassListView.as_view(), name='class_list'),
    path('classes/create/', views.ClassCreateView.as_view(), name='class_create'),
    path('classes/<int:pk>/update/', views.ClassUpdateView.as_view(), name='class_update'),
    path('classes/<int:pk>/delete/', views.ClassDeleteView.as_view(), name='class_delete'),

    # Lecturer CRUD
    path('lecturers/', views.LecturerListView.as_view(), name='lecturer_list'),
    path('lecturers/create/', views.LecturerCreateView.as_view(), name='lecturer_create'),
    path('lecturers/<int:pk>/update/', views.LecturerUpdateView.as_view(), name='lecturer_update'),
    path('lecturers/<int:pk>/delete/', views.LecturerDeleteView.as_view(), name='lecturer_delete'),

    # Assign/Remove Lecturer to/from Class
    path('classes/<int:pk>/assign-lecturer/', views.LecturerAssignView.as_view(), name='assign_lecturer'),

    # Student CRUD
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

    # Enrollment
    path('enrollments/', views.EnrollmentListView.as_view(), name='enrollment_list'),
    path('enrollments/create/', views.EnrollStudentCreateView.as_view(), name='enrollment_create'),
    path('enrollments/<int:pk>/delete/', views.EnrollStudentDeleteView.as_view(), name='enrollment_delete'),

    # Upload Students via Excel
    path('students/upload/', views.upload_students, name='upload_students'),

    # Email Students with Poor Attendance
    path('students/email-poor-attendance/', views.email_students_with_poor_attendance, name='email_poor_attendance'),

    # Lecturer Enter Attendance for a Class
    path('attendance/enter/<int:class_id>/', views.enter_attendance, name='enter_attendance'),

    # Student View Attendance
    path('attendance/view/', views.student_view_attendance, name='view_attendance'),
]
