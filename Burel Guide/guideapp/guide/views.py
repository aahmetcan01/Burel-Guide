from django.shortcuts import render
from .models import guide
# Create your views here.



def index(request):
     obj=guide.objects.all()
     data={
          "obj":obj,
     }
     return render(request,"index.html",data)