from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'basic/home.html')

def form(request):
    return render(request,'basic/form.html')

