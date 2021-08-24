from django.shortcuts import render, redirect,HttpResponse
from .models import Contact
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
import os

# Create your views here.


def home(request):
    return render(request, 'base.html')

def register(request):
    m=Contact()
    if request.method=="POST":
        m.name=request.POST['name']
        m.phone=request.POST['phone']
        m.work_info=request.POST['work_info']
        m.email=request.POST['email']
        m.address=request.POST['address']
        if len(request.FILES) != 0:
            m.image=request.FILES['image']
        messages.info(request, 'Contact Saved Successfully')
        m.save()
        #return redirect('register')
    return render(request, 'add.html')

def display(request):
    n=Contact.objects.all()
    con={
        'z':n
        
    }
    return render(request, 'show.html', con)


def search(request):
    if request.method=="POST":
        naz=request.POST['sa']
        mul=Contact.objects.filter(Q(name__icontains=naz)|Q(phone__icontains=naz)).distinct()
        if mul:
            con={
                'x':mul
            }
            return render(request,'search.html', con)
    return render(request, 'search.html')


def edit(request, id):
    e=Contact.objects.get(id=id)
    #milon=Contact(instance=e)
    con={
        'e': e
    }
    return render(request, 'edit.html', con)

def update(request,id):
    e=Contact.objects.get(id=id)
    if request.method=="GET":
        if len(request.FILES) != 0:
            if len(e.image) > 0:
                os.remove(e.image.path)
            e.image = request.FILES['image']
        e.name=request.GET['name']
        e.phone=request.GET['phone']
        e.work_info=request.GET['work_info']
        e.email=request.GET['email']
        e.address=request.GET['address']
        #e.image=request.POST['image']
        e.save()

        #messages.info(request, 'Contact Saved Successfully')
        #e.save()
    return redirect('list')

    '''
    e.name=request.GET['name']
    e.phone=request.GET['phone']
    e.work_info=request.GET['work_info']
    e.email=request.GET['email']
    e.address=request.GET['address']
    e.image=request.GET['image']

    #messages.info(request, 'Contact Saved Successfully')
    e.save()
    return redirect('list')
    '''


def delete(request, id):
    f=Contact.objects.get(id=id)
    f.delete()
    return redirect('list')


        


 
