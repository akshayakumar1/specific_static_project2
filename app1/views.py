from django.shortcuts import render

# Create your views here.

def staticTemplates(request):
    return render(request,"staticTemplates.html")
    
