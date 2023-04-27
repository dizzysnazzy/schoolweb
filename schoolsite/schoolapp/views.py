from django.shortcuts import render

# Create your views here
def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def downloads(request):
    return render(request, 'downloads.html')

def e_learning(request):
    return render(request, 'elearning.html')

def home(request):
    return render(request, 'home.html')

def school_admin(request):
    return render(request, 'schooladmin.html')

def tenders(request):
    return render(request, 'tenders.html')



