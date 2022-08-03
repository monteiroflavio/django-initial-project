from django.http import HttpResponse

STATUSES = {
    "HTTP_OK": 200,
}
# Create your views here.
def hello(request: None) -> None:
    return HttpResponse('Hello World!', status=STATUSES["HTTP_OK"])