from django.shortcuts import render
import requests

# Create your views here.
def location_generator(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    #url='http://api.ipstack.com/'+str(ip)+'?access_key=YOUR ACESS KEY'
    response = requests.get(url)
    data = response.json()
    return render(request,'testapp/index.html',data)