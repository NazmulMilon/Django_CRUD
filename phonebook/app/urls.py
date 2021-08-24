
from django.urls import path
from . import views

urlpatterns = [
    path('',views.display, name='list'),
    path('reg', views.register, name='re'),
    path('list', views.display, name='list'),
    path('s', views.search, name='s'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
