from django.urls import path
from quanly import views
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    path('',views.dashboard, name='dashboard'),
    path('add_emp/',views.add_emp, name='add_emp'),
    path('update_emp/<str:id>/',views.update_emp, name='update_emp'),
    path('delete_emp/<str:id>/',views.delete_emp, name='delete_emp'),
    path('details_emp/<str:id>/',views.details_emp, name='details_emp'),
]