from django.shortcuts import render
from module import func

# Create your views here.
def index2(request):  

    id, Url = func.sendImageURL()      



    return render(request, "search/index2.html", locals())