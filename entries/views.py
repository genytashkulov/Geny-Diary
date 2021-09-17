from django.shortcuts import render,redirect,HttpResponse
from .models import Entry
from .form import Entryform
# Create your views here.
def index(request):
    entries = Entry.objects.order_by('-date')

    context = {'entries': entries}
    return render(request,'entries/index.html',context)

def add(request):

    if request.method == 'POST':
        form = Entryform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
      form = Entryform()

    context = {'form': form}


    return render(request,'entries/add.html',context)


