from django.urls import path
from .views import panelView, studentsListView, teacherListView, student_update, add_courses, update_courses



urlpatterns = [
    path("admin/", panelView, name="admin"),
    path("admin/students/", studentsListView, name="students"),
    path("admin/teachers/", teacherListView, name="teachers"),
    path("admin/students/update_student", student_update, name="update_student" ),
    path("admin/courses/add_courses", add_courses, name="add_courses" ),
    path("admin/courses/update_courses", update_courses, name="update_courses" )

]
