
from django.shortcuts import render

from PyDictionary import PyDictionary
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
# Create your views here.

def home(request):
    return render(request,'home.html')


            
def translation(request):
    search = request.GET.get('search')
    new_lang = request.GET.get('languages')
    if search == '':
            message= {'message':"INPUT CANNOT BE EMPTY!!!"}
            return render(request,'notfound.html',message)
    try:
        translator = Translator()
        translation =  translator.translate(search, dest = new_lang)
        
        wordsound = gTTS(text=translation.text , lang = new_lang , slow = False )
        wordsound.save("sound.mp3")
    except ValueError:
        
        translations={
            'translation':translation.text ,
            'word':search,
            'language':new_lang,
            'playsound': " "
        }
        return render(request,'translate.html',translations)
    
    else:
        translations={
            'translation':translation.text ,
            'word':search,
            'language':new_lang,
            'playsound': os.system("sound.mp3")
        }
        return render(request,'translate.html',translations)

def word(request):
    
        search = request.GET.get('word')
        dictionary =  PyDictionary()
        
        if search == '':
            message= {'message':"INPUT CANNOT BE EMPTY!!!"}
            return render(request,'notfound.html',message)
        else:
            meaning = dictionary.meaning(search)
            wordsound = gTTS(text=search,lang = "en" , slow = True)
            wordsound.save("pronunciation.mp3")
            if meaning == None:
                message= {'message': f"INPUT {search} NOT RECOGNIZED!!!"}
                return render(request,'notfound.html',message)
            
            else:
                context = {
                    'search':search,
                    'meaning': meaning,
                    'pronunciation' : os.system("pronunciation.mp3")
                    
                }
                return render(request,'word.html', context)
