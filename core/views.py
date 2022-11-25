from django.shortcuts import render,get_object_or_404
from .models import Lanches1
def index(request):
    produto = Lanches1.objects.all()
    context = {
        'curso' : 'isso é uma chave, para chamar no index',
        'produto' : produto,
    }
    return render(request,'index.html', context)

def carrinho(request):
    return render(request,'carrinho.html')

def lanches(request):
    return render(request, 'lanches.html')

def pasteis(request):
    return render(request, 'pasteis.html')

def tapiocas(request):
    return render(request, 'tapiocas.html')

def bebidas(request):
    return render(request, 'bebidas.html')

def combos(request):
    return render(request, 'combos.html')

def produto(request,pk):
    #produ = Lanches1.objects.get(id=pk)
    produ = get_object_or_404(Lanches1, id=pk)
    context = {
        'lanches1': produ
    }
    return render(request,'produto.html', context)

def error404(request,exception):
    return render(request,'404.html')

def error500(request):
    return render(request,'500.html')