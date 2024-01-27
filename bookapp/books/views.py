from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def helloworld(request):
    # return render("")
    return JsonResponse({'main': 'hello world'})