from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request,'home.html')

def formName(request):
    form = forms.review()

    if request.method == 'POST':
        form = forms.review(request.POST)

        if form.is_valid():
            print("validation success")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request, 'form-page.html', context={'form': form})