from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def Count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1

    return render(request, 'count.html', {'fulltext': fulltext, 'word':len(wordlist), 'worddictionary':worddictionary.items() })


