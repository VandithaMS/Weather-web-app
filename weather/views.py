from django.shortcuts import render
from django import forms
from .weather import get_weather, image

info = None
class InputForm(forms.Form):
    city = forms.CharField(label="City name", min_length=1)

def index(request):
    info=None
    img=''
    if request.method == "POST":
        new=InputForm(request.POST)
        info=dict()
        if new.is_valid():
            name=new.cleaned_data['city']
            print(name)
            info=get_weather(name)
            print(info)
            img=image(info["time"])
            
    
    return render(request, "app/index.html", {
        'form': InputForm(),
        'result':info,
        'img': img,
    })
