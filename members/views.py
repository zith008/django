from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

# def members_view(request):
#     #return HttpResponse("Hello world!")
#     return HttpResponse(render(request,'myfirst.html'))

def members_view(request):
    mymembers = Member.objects.all().values()
    return HttpResponse(render(request, 'all_members.html',{'mymembers':mymembers}))
