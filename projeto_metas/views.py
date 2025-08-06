from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login,authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Goal
from .forms import GoalForm


# Create your views here.
User = get_user_model()
class ViewsHome:
    """_summary_

    """
    

    # metodo estatico para para rota home do sistema
    @staticmethod
    def home(request):
       
        return render(request, 'home.html')
    

    # metodo estatico para login do usuario
    @staticmethod
    def login(request):
        

        if request.method == 'POST':
            nome = request.POST.get('nome', "").strip()
            password  = request.POST.get('senha1')
            print(f'nome {nome}, senha {password}')

            if not nome or not password:
                messages.error(request, 'Error preencha o usuario e senha')
                return render(request, 'login.html')
            

            user_1 = authenticate(request, username=nome, password=password)
            teste_user = User.objects.filter(password=password).exists()
            print(teste_user)
            print(user_1)
            # validando usuario verificando se é nulo
            if user_1 is not None:
                login(request, user_1)
                return redirect('painel')
            
            else:
                messages.error(request, 'Credenciais invalidas')
                

        return render(request, 'login.html')
    
    @staticmethod
    
    # metodo estatico para cadastro do usuario
    def cadastro(request):
        """if request.user.is_authenticated:
            return redirect('painel')"""
        
        if request.method == 'POST':
            nome = request.POST.get('username')
            password  = request.POST.get('password')
            email = request.POST.get('email')
            print(f'nome {nome}, senha {password} email{email}')
            
            # verificando se os campos estão nulos
            if not nome or not password or not email:
                messages.error(request, 'Todos os campos são obrigatorios')
                return render(request, 'cadastro.html')

            # verificando se o usuario já existe
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuario ja existe')
                return render(request, 'cadastro.html')
            
            user = User.objects.create_user(username=nome, email=email, password=password)
            messages.success(request, 'Conta criada com sucesso, ja esta logado')
            login(request, user)
            return redirect('painel')


        return render(request, 'cadastro.html')
    
   

    @staticmethod
    def logout_painel(request):
        logout(request)
        messages.info(request, 'Você saiu da sua conta')
        return redirect('login')
    
class PainelUser(LoginRequiredMixin, View):
    login_url='login'
    
    # metodo para verificar se o usuario esta autenticado para acessar o painel
    def get(self, request):
        
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'painel.html')

    @staticmethod
    @login_required
    def listgoal(request):
        goal = Goal.objects.all()

        return render(request, 'listgoal.html', {'goal': goal})

    @staticmethod
    @login_required
    #medoto estatico e necessario login para criar tarefa
    def goalcreate(request):
        if request.method == 'POST':
            formcreate = GoalForm(request.POST)
            #formcreate.users_id = request.user.id
            if formcreate.is_valid():
                postform = formcreate.save(commit=False)

                postform.users = request.user

                postform.save()

                return redirect("listgoal")

        else:
            formcreate = GoalForm()

        return render(request, 'creategoal.html', {'formcreate': formcreate})

    @staticmethod
    @login_required
    # metodo estatico e necessario login para atualizar a tarefa 
    def goalupdate(request, pk):
        goalinstance = get_object_or_404(Goal, pk=pk)
        formupdate = GoalForm(request.POST or None, instance=goalinstance) # formulario com os dados do banco 
      
            # validando formulario
        if formupdate.is_valid():
            formupdate.save()

            return redirect('listgoal')
        return render(request, 'editegoal.html', {'formupdate': formupdate})
        

    @staticmethod
    @login_required
    # metodo estatico e necessario login para excluir uma meta do usuario no banco 
    def goaldelete(request, pk):
        goaldelete = get_object_or_404(Goal, pk=pk) # aqui faz a busca do produto (pra não esquecer depois)

        if request.method == 'POST':
            goaldelete.delete()

            return redirect('listgoal')

        return render(request, 'goaldelete.html', {'goaldelete': goaldelete})

    
            

