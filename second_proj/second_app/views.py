from django.shortcuts import render
# from django.http import HttpResponse
# from second_app.models import User
from second_app.forms import NewUserForm

# Create your views here.

def index(request):
    my_dict = {'insert_me':"Now I am coming from second_app/index.html",'insert_help':"This is the message for the help page only!"}
    return render(request,'second_app/index.html',context=my_dict)

def indexHelp(request):
    my_dict = {'insert_me':"Now I am coming from second_app/index.html",'insert_help':"This is the message for the help page only!"}
    return render(request,'second_app/help.html',context=my_dict)

def usersIndex(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'second_app/users.html',{'form':form})
