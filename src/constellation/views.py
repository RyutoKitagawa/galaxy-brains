from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseNotFound, Http404
import pyrebase

config = {
    'apiKey': "AIzaSyD4pquYNH5AnnnKTFmdRg0dzooWkwQrj8I",
    'authDomain': "scholar-system.firebaseapp.com",
    'databaseURL': "https://scholar-system.firebaseio.com",
    'storageBucket': "scholar-system.appspot.com",
}

firebase = pyrebase.initialize_app(config)

loggedin = False
mydict = {'loggedin': loggedin}

"""
raise Http404
"""
# Get a reference to the auth service
firebase_auth = firebase.auth()
firebase_database = firebase.database()



def f(): 
    global loggedin 
    loggedin = True
    global mydict
    mydict = {'loggedin': loggedin}

def index(request):

    return render(request, 'index.html', mydict)
def signup(request):
    return render(request, 'SignUp.html')

def signInSubmit(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = firebase_auth.sign_in_with_email_and_password(email, password)
        request.session['uid'] = str(user['idToken'])
    except:
        messages.success(request, ('Invalid Credentials'))
        return redirect('index')
    f()
    return redirect('landingPage')


def logoutSubmit(request):
    auth.logout(request)
    messages.success(request, ('You have been logged out'))
    return render(request, 'index.html')

def landingPage(request):
    return render(request, 'landingPage.html', mydict)

def createproject(request):
    return render(request, 'creatproject.html')

def createproject(request):
    return render(request, 'createproject.html')

def projectPage(request):
    return render(request, 'project_page.html')
