from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.models import Movie
from movieapp.forms import Forms


# Create your views here.
def index(request):
    movies=Movie.objects.all()
    context={
        'movie_list':movies
    }

    return render(request,'index.html',context)

def detail(request,movie_id):
    movies=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movies})


def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        Movie.objects.create(name=name,desc=desc,year=year,img=img)

    return render(request,'add.html')

def update(request,id):
    ids=Movie.objects.get(id=id)
    form=Forms(request.POST,None,request.FILES,instance=ids)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'id':ids})

def delete(request,id):
    if request.method=='POST':
      m=Movie.objects.get(id=id)
      m.delete()
      return redirect('/')

    return render(request,'delete.html')
