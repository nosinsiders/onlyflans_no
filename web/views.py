from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Flan, ContactForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ContactFormModelForm
# Create your views here.
def home(request):
  #flans = Flan.objects.all()
  flanes_publicos = Flan.objects.filter(is_private = False)
  return render(request,'index.html', { 'flanes' : flanes_publicos  })

@login_required
def welcome_vista(request):
  flanes_privados = Flan.objects.filter(is_private = True)
  return render(request, 'welcome.html', {'flanes': flanes_privados })

def about_vista(request):
  return render(request, 'about.html')

#def contacto_vista(request):
#  return render(request, 'contacto.html')

#Forms
def contacto(request):
  if request.method == 'POST':
      form = ContactFormModelForm(request.POST)
      if form.is_valid():
          # Procesar datos en form.cleaned_data
          ContactForm.objects.create(**form.cleaned_data)
          return redirect('success')
  else:
      form = ContactFormModelForm()  
  return render(request, 'contacto.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def contacto_beta(request):
  if request.method == 'POST':
      form = ContactFormModelForm(request.POST)
      if form.is_valid():
          # Procesar datos en form.cleaned_data
          ContactForm.objects.create(**form.cleaned_data)
          return redirect('success')
  else:
      form = ContactFormModelForm()  
  return render(request, 'contacto_beta.html', {'form': form})

def logoutyo(request):
    logout(request)
    return redirect('home')