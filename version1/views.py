from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.templatetags.static import static

# 404 error
def error404(request):
	return HttpResponse("Sorry you have reached an invalid url!")	

# home page
def index(request):
	return HttpResponseRedirect("/wedding")
#    return render(request, 'index/indexWithAjax.html')

''' 
wedding website views
'''
# home page
def wedding(request):
	return render(request, 'epilogue/index.html')
# events page
def weddingEvents(request):
	return render(request, 'epilogue/404.html')
# venue page
def weddingVenue(request):
	return render(request, 'epilogue/404.html')
# travel page
def weddingTravel(request):
	return render(request, 'epilogue/404.html')
# return image url
def getImage(request, id):
	url = static("images/slideshow/" + str(id) + ".jpg")
	return HttpResponse(url)