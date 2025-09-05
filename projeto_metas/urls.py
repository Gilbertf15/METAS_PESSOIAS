from django.urls import path

from projeto_metas import views

urlpatterns = [
    path('', views.ViewsHome.home, name='home'),
    path('login/', views.ViewsHome.login, name='login'),
    path('cadastro/', views.ViewsHome.cadastro, name='cadastro'),
    path('painel/', views.PainelUser.painel, name='painel'),
    path('logout/', views.ViewsHome.logout_painel, name='logout_painel'),
    path('listgoal/', views.PainelUser.listgoal, name='listgoal'),
    path('creategoal/', views.PainelUser.goalcreate, name='creategoal'),
    path('deletegoal/<int:pk>/', views.PainelUser.goaldelete, name='goaldelete'),
    path('updategoal/<int:pk>/', views.PainelUser.goalupdate, name="goalupdate"),
    path('testecard/', views.ViewsHome.testecard, name='testecard'),
    
]


