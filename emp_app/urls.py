from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('all_emp',views.all_emp,name="all_emp"),
    path('add_emp',views.add_emp,name="add_emp"),
    path('submit/',views.submit,name="submit"),
    path('remove_emp',views.remove_emp,name="remove_emp"),
    path('remove_emp/<int:emp_id>/',views.remove_emp,name="remove_emp/id"),
    path('promote/', views.promote_employee, name='promote_employee'),  # Employee selection dropdown
    path('promote/<int:employee_id>/', views.promote_employee, name='promote_employee_with_id'),
]