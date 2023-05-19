from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def home(requests):
    ctg = Catigory.objects.all()
    snakers = Snakers.objects.all()
    ctx = {
        'ctg':ctg,
        'snakers':Snakers
    }
    return render(requests,'details/index.html',ctx)

def contact(requests):
    ctx = {}
    return render(requests,'details/contact.html',ctx)

def products(requests,slug=None):
    ctg = Catigory.objects.all()
    catigory=Catigory.objects.get(slug=slug)
    snakers=Snakers.objects.all().filter(type_id=catigory.id)
    ctx = {
        'ctg':ctg,
        'catigory':catigory,
        'snakers':snakers,
    }
    return render(requests,'details/products.html',ctx)

def register(requests):
    ctx = {}
    return render(requests,'details/register.html',ctx)

def single(requests,pk=None):
    ctg =Catigory.objects.all()
    produck_pk = Snakers.objects.get(pk=pk)
    form = ChouseForm()
    ctx = {
        'ctg':ctg,
        'produck_pk':produck_pk,
        'form':form,
    }
    if requests.POST:
        forms = ChouseForm(requests.POST or None,
         requests.FILES or None)
        if forms.is_valid():
                root = forms.save()
                root = Buy.objects.get(pk=root.id)
                root.produck = produck_pk
                root.save()
        else:
            print(forms.errors)
    return render(requests,'details/single.html',ctx)
def home2(requests):
    return render(requests,'index.html',)
def about(request):
     return render(request,'about.html')
def contact(request):
     if request.method == 'POST':
         Contact.objects.create(
              name = request.POST['name'],
              email = request.POST['email'],
              subject = request.POST['sub'],
              message = request.POST['mess'],
         ) 
         return redirect('home')
     return render(request,'contact.html')