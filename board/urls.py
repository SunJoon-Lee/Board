from django.contrib import admin
from django.urls import path, include
from board import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('post/',views.post, name='post'), #글쓰기
    path('<int:board_id>/',views.detail, name='detail'), #글 상세보기
    path('show/',views.show, name='show'), #전체 글 보기
    path('<int:pk>/edit/', views.edit, name='edit'), #폼 수정
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('logoutgo/',views.logoutgo, name='logoutgo'),
]