from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def first_request(request):
    # Notice: the args must be a iterate, not a int type , so make sure that there is a comma in the args
    return HttpResponseRedirect(reverse("new-year-archive", args=(2222,)))


def year_archive(request, year):
    return HttpResponse(f"year-archive:year:{year}")


def html_redirect(request):
    return render(request, "redirect.html")
