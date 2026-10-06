from django.shortcuts import render


def index(request):
    
    contexto = {
        'nome': 'John',
        'idade': 26,
        'frutas': ['Maçã', 'Banana', 'Laranja', 'Uva'],
    }

    return render(
        request,
        'cadastro/index.html', 
        contexto
    )

def contato(request):
    contexto = {
        'nome': 'Johnny'
    }
    return render(
        request,
        'cadastro/contato.html',
        contexto
    )