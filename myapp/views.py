from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app(request):
    return HttpResponse("Hello Asur")

def dynamic_response(request,string):
    return HttpResponse(f"{string}")

def factvw(request,no):
    fact=1
    for i in range(1,no+1):
        fact =fact*i
    return HttpResponse(f"{fact}")


def length(request,string):
    length=len(string)
    return HttpResponse(f"{length}")

def find(request,string,char):
    count=0
    for i in range(len(string)):
        if string[i]==char:
            count+=1
    return HttpResponse(f"{count}")

def indexvw(request,a):
    print(a)
    return render(request,'index.html',{'a':a})

def avw(request):
    return render(request,'a.html')