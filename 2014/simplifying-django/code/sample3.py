import sys
from functools import partial, wraps

from django.conf.urls import url
from django.conf import settings
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
)

def smart_view(fn):
    @wraps(fn)
    def _wrapper(*args, **kwargs):
        response = fn(*args, **kwargs)
        if isinstance(response, HttpResponse):
            return response
        return HttpResponse(response)

    return _wrapper

def route(rx:str, name:str, fn=None):
    if fn is None:
        return partial(route, rx, name)

    _g = globals()
    _g.setdefault("urlpatterns", [])
    _g["urlpatterns"].append(url(rx, smart_view(fn),
                                 name=name))
    return fn

@route(r"^$", name="index")
def index(request):
    return "Powered by Django v3"

if __name__ == "__main__":
    from django.core import management as m
    m.execute_from_command_line(sys.argv)
