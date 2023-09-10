from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index, name="home"),
    path("add_employee", views.add_employee, name="add_employee"),
    path("delete_emp/<int:empid>", views.delete_emp),
    path("update_employee/<int:empid>", views.update_employee),
    path("update_employee/do_update/<int:empid>", views.do_update),
]
