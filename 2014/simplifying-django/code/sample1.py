import sys

from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
)

def index(request):
    return HttpResponse("Powered by Django")

urlpatterns = [
    url(r"^$", index, name="index"),
]

if __name__ == "__main__":
    from django.core import management as m
    m.execute_from_command_line(sys.argv)
