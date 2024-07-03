from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Regulation

def regulation_list(request):
    regulations = Regulation.objects.all()
    return render(request, 'regulations/regulation_list.html', {'regulations': regulations})

def regulation_detail(request, pk):
    regulation = get_object_or_404(Regulation, pk=pk)
    return render(request, 'regulations/regulation_detail.html', {'regulation': regulation})
