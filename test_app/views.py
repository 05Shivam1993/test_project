from django.shortcuts import render,HttpResponse
from test_app.models import Item

# Create your views here.


def add_data(request):
    if request.method == "POST":
        item = request.POST.get("item").strip()
        if item:
            Item.objects.create(item=item)
    return render(request,"add_data.html")

def list_data(request):
    qs = Item.objects.all()
    result = []
    for item in qs:
        data = dict()
        data[item.id] = item.item
        result.append(data)
        
    return render(request,"list_data.html",context={"data":result})