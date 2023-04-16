from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Pet
# Create your views here.

def home(request):
    pets = Pet.objects.all()
    #return HttpResponse('<p>home view<p>')
    return render(request, 'home.html', {'pets': pets})

def pet_detail(request,id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet': pet})
    #return HttpResponse('<p>pet_detail view with the id {}</p>'.format(id))