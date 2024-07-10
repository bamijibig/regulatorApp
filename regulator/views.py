from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Regulation

def regulation_list(request):
    query = request.GET.get('q')
    if query:
        regulations = Regulation.objects.filter(title__icontains=query)
    else:
        regulations = Regulation.objects.all()
    
    paginator = Paginator(regulations, 3)  # Show 10 regulations per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'regulations/regulation_list.html', {'page_obj': page_obj, 'query': query})

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
