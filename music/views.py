# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Album

def index(request):
        #return HttpResponse("<h1> this is the music app home page </h1>")	
	all_albums = Album.objects.all()
	template = loader.get_template('music/index.html')
	context = {
	           'all_albums':all_albums, 
	 }
        return HttpResponse(template.render(context,request))


def detail(request, album_id):
	return HttpResponse("<h2> Details for the album id: " + str(album_id)+ "</h2>")
