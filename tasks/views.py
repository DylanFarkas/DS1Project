from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
def admin_page(request):
    return render(request, 'adminpage.html')