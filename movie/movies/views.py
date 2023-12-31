from django.shortcuts import render
from movies.models import Movies
from movies.forms import movieform
# Create your views here.

def home(request):
    m=Movies.objects.all()
    return render(request,'home.html',{'Movies':m})


def add(request):# user defined
    if(request.method=="POST"):
        ti=request.POST['t']
        dire=request.POST['d']
        yr=request.POST['y']
        pos=request.FILES['psr']
        m=Movies.objects.create(title=ti,director=dire,year=yr,poster=pos)
        m.save()
        return home(request)
    return render(request,'add.html')
def add1(request):# build in type
    form=movieform()
    if(request.method=="POST"):
        form=movieform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
        return mdetails(request)
    return render(request,'add1.html',{'form':form})



def mdetails(request,p):
    m=Movies.objects.get(id=p)
    return render(request,'mdetails.html',{'Movies':m})


def deletemoviebyid(request,p):
    m=Movies.objects.get(id=p)
    m.delete()
    return home(request)


def editmoviebyid(request,p):
    m=Movies.objects.get(id=p)
    form=movieform(instance=m)
    if(request.method=="POST"):
        form=movieform(request.POST,request.FILES,instance=m)
        if form.is_valid():
            form.save()
            return mdetails(request,p)
    return render(request,'add1.html',{'form':form})

