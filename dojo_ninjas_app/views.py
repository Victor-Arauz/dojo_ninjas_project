from django.shortcuts import redirect, render, HttpResponse
from .models import Dojo, Ninja

def index(request):
    dojo = Dojo.objects.all()
    context = {
        'allDojos': dojo
    }
    return render(request, 'index.html', context)

def create_dojo(request):

    Dojo.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
    return redirect('/')

def create_ninja(request):

    new_ninja = Ninja.objects.create(
        first_name = request.POST['first_name'], 
        last_name = request.POST['last_name'], 
        dojo_id = request.POST['dojo'])
    print(new_ninja)
    return redirect('/')

@property
def full_name(self):
    return f"{self.first_name} {self.last_name}"
