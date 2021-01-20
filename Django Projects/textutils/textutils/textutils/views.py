
# Created by Roshaa

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse('about Roshaa <a href="/">Back to home</a>')

def contact(request):
    return render(request,'contact.html')

def punc(request):

    if request.POST.get('chk') == 'on':

        rawtext = request.POST.get('txtIndex')
        newtext = ''

        for index,char in enumerate(rawtext):
            if rawtext[index] == ' ':
                if rawtext[index + 1] == ' ':
                    pass
                else:
                    newtext = newtext + char

            else:
                newtext = newtext + char

        params = {
            'para1': 'rama',
            'para2': 'rama',
            'trimmed' : newtext
        }

        return render(request,'punc.html',params)

    else:
        return HttpResponse("Please check")