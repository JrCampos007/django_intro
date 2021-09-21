from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "index.html")

def random(request):
    word = get_random_string(length=14)         

    if "counter" not in request.session:        
        request.session["counter"] = 0

    request.session["counter"] +=1              

    if "word_list" not in request.session:      
        request.session["word_list"] = []

    request.session['random_word'] = word       
    request.session["word_list"].append(word)   


    return redirect("/")                        

def reset(request):
    request.session.flush()                     

    return redirect('/')


# Create your views here.
