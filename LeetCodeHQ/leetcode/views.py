from django.shortcuts import render
from .models import CodeInject
from django.shortcuts import get_object_or_404

# Create your views here.

def indexl(request):
    return render(request,template_name='indexl.html')

def code_list(request):
    order_by = request.GET.get('order_by', 'cid')
    direction = '-' if order_by.startswith('-') else ''
    codel = CodeInject.objects.all().order_by(direction + order_by.lstrip('-'))
    return render(request, 'indexl.html', {'codel': codel, 'order_by': order_by})

def code_detail(request, cid):
    code = get_object_or_404(CodeInject, cid=cid)
    return render(request, 'code_detail.html', {'code': code})