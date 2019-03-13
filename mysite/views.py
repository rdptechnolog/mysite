from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def contact(request):
    return HttpResponse('<center><h1>Our Contact </h1><br>This is our contact page to know more call on 9987067019 </center>')

def count(request):
    data = request.GET['txtarea']
    word_list = data.split()
    list_length = len(word_list)

    worddictionary = {}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sorted_list = sorted(worddictionary.items(), key = operator.itemgetter(1))

    return render(request, 'count.html', {'txtarea':data, 'word':list_length, 'worddictionary':sorted_list})