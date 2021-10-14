from django.shortcuts import render
from basic.models import Topic,Webpage,AccessRecord

# Create your views here.
def home(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request,'home.html',context=date_dict)
