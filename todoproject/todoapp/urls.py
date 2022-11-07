from django.urls import path

from todoapp import views

urlpatterns = [
    path('', views.add, name ='index'),
    path('delete/<int:taskid>/', views.delete, name ='delete'),
    path('update/<int:taskid>/', views.update, name ='update'),
    path('cbvhome/', views.task_listview.as_view(), name ='cbvhome'),
    path('detailview/<int:pk>', views.task_detailview.as_view(), name ='detailview'),
    path('updateview/<int:pk>', views.task_updateview.as_view(), name ='updateview'),
    path('deleteview/<int:pk>', views.task_deleteview.as_view(), name ='deleteview'),

]
