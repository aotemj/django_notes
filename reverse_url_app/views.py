from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def first_request(request):
    # TODO this request catch 500 but I didn't find the reason, I will check it out later
    return HttpResponseRedirect(reverse("new-year-archive", args=(2222)))


def year_archive(request, year):
    return HttpResponse(f"year-archive:year:{year}")
