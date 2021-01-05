from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,DetailView
from pdf import forms
from django.urls import reverse_lazy
from pdf.models import Resume
import pdfkit
import io
from django.http import HttpResponse
from django.template import loader

# Create your views here.
class resume_form(CreateView):
    template_name = 'pdf/create_resume.html'
    form_class = forms.ResumeForm
    success_url = reverse_lazy('pdf:generating')

def pdf_detail(request,id):
    pdftemplate = Resume.objects.get(pk=id)
    template = loader.get_template('pdf/pdf_page.html')
    html = template.render({'pdftemplate':pdftemplate})
    options = {
        'page-size' : 'Letter',
        'encoding' : 'UTF-8',
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename = 'resume.pdf'
    return response

class list_user(ListView):
    model = Resume
    context_object_name = "resume"
    template_name = "pdf/download_page.html"


class generating(TemplateView):
    template_name = 'pdf/generating.html'
