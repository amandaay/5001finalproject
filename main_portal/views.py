from django.shortcuts import render
from main_portal.forms import NewUserForm
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, 'main_portal/index.html')


def your_portal(request):
    my_portal = {'your_portal_insert': 'YOUR PORTAL'}
    return render(request, 'main_portal/your_portal.html',
                  {'your_portal_insert': my_portal})


def signed_up(request):
    sign_up_success = {'signed_up_insert': 'SIGNED UP'}
    return render(request, 'main_portal/signed_up.html',
                  context=sign_up_success)


def sign_up(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            print("Validation Success!")
            form.save(commit=True)
            # return signed_up(request)
            return HttpResponseRedirect('/signed_up/')

        else:
            form = NewUserForm()
            print("ERROR FORM INVALID")

    return render(request, 'main_portal/sign_up.html', {'form': form})
