from django.shortcuts import render



# Create your views here.

class ViewsHome:
    """_summary_

    """
    @staticmethod
    def home(request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        return render(request, 'home.html')
    
    @staticmethod
    def login(request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        return render(request, 'login.html')
    
    @staticmethod
    def cadastro(request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        return render(request, 'cadastro.html')