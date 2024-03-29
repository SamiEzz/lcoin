from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from .forms import NewUserForm

# Create your views here.

def homepage(request):
    return render(request=request,template_name="main/home.html")
    #return render(request=request,template_name="main/home.html",context={"mails": Player.objects.all})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})
    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    print( "Logged out successfully!")
    return redirect("homepage")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"You are now logged in as {username}")
                return redirect('/')
            else:
                print("Invalid username or password.")
                return redirect('/login?result=inv')
        else:
            print("Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def map(request):
    return render(request=request,template_name="main/map.html")
