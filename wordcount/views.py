# Allows us to return back HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
import operator


def wordcount(request):
    return render(request, 'wordcount/wordcount.html')

def count(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()
    
    wordDict = {}
    for word in wordlist:
        if word in wordDict:
            #Increase
            wordDict [word] += 1
        else:
            #Add to dict
            wordDict [word] = 1

    sortedWords = sorted(wordDict.items(), key = operator.itemgetter(1), reverse = True)



    return render(request, "wordcount/count.html", {'fulltext':fulltext,'count':len(wordlist),'sortedWords':sortedWords} )

