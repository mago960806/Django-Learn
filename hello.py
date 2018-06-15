import sys
from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings
from django.core.wsgi import get_wsgi_application


def index(request):
    return HttpResponse('<h1>Hello World</h1>')

urlpatterns = (
    url(r'^$', index),
)

settings.configure(
    DEBUG=type,
    SECRET_KEY='sxy960806',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

app = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)