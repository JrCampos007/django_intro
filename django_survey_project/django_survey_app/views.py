from django.shortcuts import render, redirect

def index(request):
    return render(request, 'form.html')

def process(request):                               # POST request triggered by the Form action on index.html
    if request.method == "POST":
        
        checklanguages = request.POST.getlist('checklangs[]')       
        checkdata = ''                                              
        for x in checklanguages:                                    
            checkdata = checkdata + x + " "

        request.session['name'] = request.POST['name']              # request.session is the new dict, so no longer need "context"
        request.session['dojo'] = request.POST['dojo_location']     # leave comma separators out between these lines or you will get ['brackets'] around the 
        request.session['language'] = request.POST['fav_language']  # text values of the session variables
        request.session['radiolanguage'] = request.POST['radiofav_language']
        request.session['data'] = checkdata
        request.session['comment'] = request.POST['comment']

        return redirect('/result')

def result(request):                                # GET request triggered by redirect from .process (above)
    return render(request, 'result.html')

# Create your views here.
