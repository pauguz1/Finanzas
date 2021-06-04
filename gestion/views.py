from django.shortcuts import render

# Create your views here.



def index(request):
    contexto={
        'objeto':'objeto1'
    }
    return render(request,'gestion/index.html',contexto)