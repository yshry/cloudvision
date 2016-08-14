from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .forms import ImageFileForm
#from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'apps/index.html'

#class UploadView(generic.TemplateView):
#    template_name = 'apps/upload.html'

def handle_upload_file(f):
    destination = open

def upload(request):
    if request.method == 'POST':
        form = ImageFileForm(request.POST, request.FILES)
        form.save()
        if form.is_valid():
            #form.save()
            return  HttpResponse("saved")
        else:
            return HttpResponse("failed")
    else:
        form = ImageFileForm()
        return render(request, 'apps/upload.html', {'form':form})

