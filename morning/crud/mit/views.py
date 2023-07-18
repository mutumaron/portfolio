from django.shortcuts import render
from .models import People
from django.http import HttpResponse



def home(request):
    return render(request,'index.html')

def insert(request):
    if request.method == "POST":
        name=request.POST.get('name')
        school=request.POST.get('school')
        email = request.POST.get('email')



        person = People(name=name,email=email,school=school)
        person.save()


       #print(name,school)


    #return HttpResponse("succes")
    return render(request, 'people.html')

# Create your views here.

def people(request):
    d = People.objects.all()
    context={"d": d}
    return render(request,'people.html',context)

def delete(request, id):
    dd= People.objects.get(id=id)
    dd.delete()

    #return HttpResponse("Succes")
    return render(request,'people.html' )
def update(request,id):
    l = People.objects.get(id=id)

    return render(request,"update.html",{"l":l})








