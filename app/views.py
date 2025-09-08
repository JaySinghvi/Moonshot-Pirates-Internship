from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views import generic
import markdown
from .forms import DisasterForm
from .models import disaster

from .models import disaster, resources, tasks

from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'home.html')


def disaster_page(request):
    disaster_page = disaster.objects.all()
    return render(request, 'disaster.html', context={"disaster_page":disaster_page})


def create_disaster(request):
    if request.method == 'POST':
        form = DisasterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('disaster')
    else:
        form = DisasterForm()
    return render(request, 'create_disaster.html', {'form': form})

def resources_page(request):
    resource_page = resources.objects.all()
    return render(request, 'resource.html', context={"resource_page":resource_page})



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


def DisasterDetail(request, slug):
    md = markdown.Markdown(extensions=["fenced_code"])
    disaster_detail = get_object_or_404(disaster, slug=slug)

    # Render the template
    return render(request, 'disaster_details.html', {
        'disaster_detail': disaster_detail,
    })

def ResourceDetail(request, slug):
    md = markdown.Markdown(extensions=["fenced_code"])
    resource_detail = get_object_or_404(resources, slug=slug)

    # Render the template
    return render(request, 'resource_details.html', {
        'resource_detail': resource_detail,
    })