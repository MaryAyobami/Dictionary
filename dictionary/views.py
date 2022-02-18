from django.shortcuts import render

from PyDictionary import PyDictionary
from googletrans import Translator
# Create your views here.

def home(request):
    return render(request,'home.html')

def word(request):
        search = request.GET.get('search')
        dictionary =  PyDictionary()
        meaning = dictionary.meaning(search)
        antonym = dictionary.antonym(search)
        synonym = dictionary.synonym(search)
        context = {
            'meaning':meaning,
            'antonym':antonym,
            'synonym':synonym
        }
        
        return render(request,'word.html',context)    
    
def translation(request):
    search = request.GET.get('search')
    new_lang = request.GET.get('languages')
    translator = Translator()
    translation =  translator.translate(search, dest = new_lang)
    translations={
        'translation':translation.text
    }
    return render(request,'translate.html',translations)

def notfound(request):
    pass