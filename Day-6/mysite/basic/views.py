from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("form is invalid")


    return render(request,'register.html',{'form':form})
