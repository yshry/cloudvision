from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ImageFileForm
#from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import ImageFile
from django.template import loader
from django.urls import reverse

# Create your views here.

class IndexView(generic.ListView):
    context_object_name = 'detection_type_list'
    template_name = 'apps/index.html'
    
    def get_queryset(self):
        return tuple(x[0] for x in ImageFile.DETECTION_CHOICES)

#class UploadView(generic.TemplateView):
#    template_name = 'apps/upload.html'

def handle_upload_file(f):
    destination = open

def upload(request):
    if request.method == 'POST':
        form = ImageFileForm(request.POST, request.FILES)
        #form.save()
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('apps:result', kwargs={'detection_type': form.cleaned_data['detection']}))
        else:
            return HttpResponse("failed")
    else:
        form = ImageFileForm()
        return render(request, 'apps/upload.html', {'form':form})

def result(request, detection_type):
    detection_list = ImageFile.objects.filter(detection = detection_type).order_by('-datetime')
    template = loader.get_template('apps/result.html')
    context = {
        'detection_result_list': detection_list
    }
    return HttpResponse(template.render(context, request))
