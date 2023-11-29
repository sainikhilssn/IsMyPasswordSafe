from django.shortcuts import render
from django.http import HttpResponse
from .services import breached_web , breached_password

from .forms import PasswordForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PasswordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.cleaned_data)
            service = breached_password.PasswordService(form.cleaned_data['your_password'])
            count = service.breach_count()
            breach_message = f"your password has been breached {count} times"
            messages = service.check_password_strength()
            return render(request, "myPassword/name.html", {"form": form , "messages" : messages , "breach_message" : breach_message})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PasswordForm()
    return render(request, "myPassword/name.html", {"form": form})

def breached_websites(request):
    json_response = breached_web.breached_websites()
    return render(request , "myPassword/breached_websites.html", {"breached_websites" : json_response})

def home(request) : 
    # response = breached_web.breached_websites()
    # service = breached_password.Password_Service()
    # return HttpResponse(response )
    return render(request , 'myPassword/index.html')