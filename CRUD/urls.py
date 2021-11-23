from CRUD import views
from django.urls import path

urlpatterns = [
    path('',views.employee_list,name="employee_list"),
    path('add',views.add,name="addnew_employee"),
    path('edit/<int:id>',views.edit,name="edit_employee"),
    path('update/<int:id>',views.update,name="update_employee"),
    path('delete/<int:id>',views.delete,name="delete_employee"),
    path('get',views.get,name="get"),
]