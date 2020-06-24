#Created by Paggo

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    print(request.GET.get('text','default'))
    print(request.GET.get('removepunc','off'))
    print(request.GET.get('capitalize','off'))
    text=request.POST.get('text','default')
    removepunc =request.POST.get('removepunc','off')
    capitaltext=request.POST.get('capitalize','off')
    newlineremover=request.POST.get('newlineremover','off')
    charcount = request.POST.get('charcount', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc== "on":
        analyzedtext = ""
        for char in text:
            if(char not in punctuations):
                analyzedtext=analyzedtext+char
        params = {'purpose': 'To Remove Punctuatins', 'analyzed_text': analyzedtext}

    elif newlineremover=="on":
        analyzedtext=""
        for char in text:
            if char!="\n":
                analyzedtext=analyzedtext+char
        params = {'purpose': 'To Remove extra space', 'analyzed_text': analyzedtext}

    elif capitaltext=="on":
        analyzedtext = ""
        analyzedtext = analyzedtext + text.title()
        params = {'purpose': 'To  Capitalize all text', 'analyzed_text': analyzedtext}

    elif charcount == "on":
        analyzedtext = ""
        ui=0

        for char in text:

            if(char!=" "):
                ui=ui+1
        params = {'purpose': 'To Count Charaters','chrcount':ui}
    else:
        return HttpResponse("Error")

    return render(request,'analyze.html',params)

def AboutUs(request):
    return render(request,'AboutUs.html')

def ContactUs(request):
    return render(request,'ContactUs.html')
