from django.shortcuts import render


def index(request):
    return render(request, 'tools/index.html', {'num': range(16)})
