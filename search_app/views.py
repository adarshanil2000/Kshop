from django.shortcuts import render
from Ecapp.models import product
from django.db.models import Q

# Create your views here.
def searchresult(request):
    Products=None
    query=None
    if 'q' in request.GET:
        query= request.GET.get('q')
        Products=product.objects.all().filter(Q(name__contains=query) | Q(dec__contains=query))
        return render(request,'search.html',{'query':query,'products':Products})




