from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Full_name(request):
    
    return render(request, 'home.html', {'lang': 'JAVASCRIPT'})


def Division(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])

    ans = num1/num2
    return render(request, 'result.html', {'result': ans})