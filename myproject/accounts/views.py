from django.shortcuts import render

# Create your views here.


def account_index(request):
    return render(request, "base.html")
