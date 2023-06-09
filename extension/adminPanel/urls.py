from django.urls import path
from .views import *



urlpatterns = [
    path("admin/", panelView, name="admin"),
    path("admin/courses", coursesView, name="courses" ),
    path("admin/students/", studentsListView, name="students"),
    path("admin/teachers/", teacherListView, name="teachers"),
    path("admin/students/update_student", student_update, name="update_student" ),
    path("admin/courses/add_courses", add_courses, name="add_courses" ),
    path("admin/courses/update_courses", update_courses, name="update_courses" ),
    path("admin/courses/delete_courses", deleteCourse, name="delete_courses"),
    path("admin/services", servicesListView, name="services"),
    path("admin/deans", decanosListView, name="deans"),
    path("admin/projects", projectsListView, name="projects"),
    path("inprogres/", inProgressView, name="inprogres")
]
