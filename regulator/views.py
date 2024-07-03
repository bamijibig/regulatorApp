from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Regulation

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Regulation

def regulation_list(request):
    query = request.GET.get('q')
    if query:
        regulations = Regulation.objects.filter(title__icontains=query)
    else:
        regulations = Regulation.objects.all()
    return render(request, 'regulations/regulation_list.html', {'regulations': regulations})

def regulation_detail(request, pk):
    regulation = get_object_or_404(Regulation, pk=pk)
    return render(request, 'regulations/regulation_detail.html', {'regulation': regulation})

def regulation_detail_pdf(request, pk):
    regulation = get_object_or_404(Regulation, pk=pk)
    template_path = 'regulations/regulation_detail_pdf.html'
    context = {'regulation': regulation}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="regulation_{regulation.title}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response