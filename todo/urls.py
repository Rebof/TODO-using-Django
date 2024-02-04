from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.addtask , name='addtask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done , name='done'),
    path('mark_as_undone/<int:pk>/', views.mark_as_undone , name='undone'),
    path('update/<int:pk>/', views.update , name='update'),
    path('delete/<int:pk>/', views.delete , name='del'),
]
