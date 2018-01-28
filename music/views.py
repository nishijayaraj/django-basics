# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1> this is the music app home page </h1>")	

