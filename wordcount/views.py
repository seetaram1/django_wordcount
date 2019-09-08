from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse('Hello')

def psycho(request):
    return HttpResponse('psycho')
def blank(request):
    return HttpResponse('<h4>blank/<h4>')
def TemplateReturn(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def count(request):
    s=request.GET['fulltext']

    words=s.split(' ');
    print(words)

    UniqueWords={}


    for word in words:
        if word in UniqueWords:
            UniqueWords[word]=UniqueWords[word]+1
        else:
            UniqueWords[word]=1

            print(len(UniqueWords))


    return render(request,'count.html',{'words_found':UniqueWords})
