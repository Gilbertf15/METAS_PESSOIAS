from django.urls import path

from projeto_metas import views

urlpatterns = [
    path('', views.ViewsHome.home, name='home'),
    path('login/', views.ViewsHome.login, name='login'),
    path('cadastro/', views.ViewsHome.cadastro, name='cadastro'),
]
