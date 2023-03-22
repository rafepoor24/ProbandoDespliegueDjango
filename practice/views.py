from django.shortcuts import render,get_object_or_404
from practice.models import Person
from .forms import CreateNewPerson

# Create your views here.

def home (request):
    a=1+2
    return render(request, 'index.html',{'a':a})

def people(request):
    people=Person.objects.all()
    return render (request,'people.html',{
        
        'people':people
    })
    
def detailPeople(request,id):
    
    person=get_object_or_404(Person,pk=id)
    form=CreateNewPerson(instance=person)
    print(request.POST)
    return render(request,'personDetail.html',{
        'form':form
    })
    