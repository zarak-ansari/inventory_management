from pdb import post_mortem
from django.shortcuts import render

from .forms import BundleGenerationForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def generate_bundles(request):  
    
    context = {}

    if request.method == 'POST':
        form = BundleGenerationForm(request.POST)
    else:
        form = BundleGenerationForm()
    
    context['form'] = form

    return render(request, "generate_bundles.html", context=context)
