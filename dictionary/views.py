
from django.shortcuts import render

from PyDictionary import PyDictionary
from googletrans import Translator
from difflib import get_close_matches
# Create your views here.

def home(request):
    return render(request,'home.html')

def word(request):
    
        search = request.GET.get('search')
        dictionary =  PyDictionary()
        if search == '':
            message= {'message':"INPUT CANNOT BE EMPTY!!!"}
            return render(request,'home.html',message)
        else:
            meaning = dictionary.meaning(search)
            if meaning == None:
                message= {'message': f"INPUT {search} NOT RECOGNIZED!!!"}
                # get_close_matches(search,dictionary.args)
                return render(request,'home.html',message)
            
            else:
                context = {
                    'search':search,
                    'meaning': meaning
                }
                return render(request,'word.html', context)
            
def translation(request):
    search = request.GET.get('search')
    new_lang = request.GET.get('languages')
    translator = Translator()
    translation =  translator.translate(search, dest = new_lang)
    translations={
        'translation':translation.text
    }
    return render(request,'translate.html',translations)

