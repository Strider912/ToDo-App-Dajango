from django.urls  import path
from todo import views

urlpatterns = [
    path('', views.index, name='index' ), 
    path('about', views.about, name='about' ), 
    path('contact', views.contact, name='contact' ), 
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('complete/<int:task_id>', views.complete, name='complete'),
    path('pending/<int:task_id>', views.pending, name='pending'),
    path('edit/<int:task_id>', views.edit, name='edit'),
]

