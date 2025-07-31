from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login,authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
User = get_user_model()
class ViewsHome:
    """_summary_

    """
    
    @staticmethod
    def home(request):
       
        return render(request, 'home.html')
    
    @staticmethod
    def login(request):
        

        """if not request.user.is_authenticated:
            return print("ERROR LOGIN")
        render(request, "myapp/login_error.html") """


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
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'painel.html')