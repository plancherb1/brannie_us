from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.templatetags.static import static

# 404 error
def error404(request):
	return HttpResponse("Error 404")	

# home page
def index(request):
    return render(request, 'index/indexWithAjax.html')

# wedding website home
def home(request):
	return render(request, 'epilogue/index.html')

# return image url
def getImage(request, id):
	url = static("images/slideshow/" + str(id) + ".jpg")
	return HttpResponse(url)