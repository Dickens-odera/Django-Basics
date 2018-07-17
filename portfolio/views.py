from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def me(request):
    return render(request,'ports/index.php')

def about(request):
    return HttpResponse("Hi there")