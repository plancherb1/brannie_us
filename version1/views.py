from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.templatetags.static import static

# 404 error
def error404(request):
	return HttpResponse("Sorry you have reached an invalid url!")	

# home page
#def index(request):
#	return HttpResponseRedirect("/wedding")
#    return render(request, 'index/indexWithAjax.html')

''' 
wedding website views
'''
# home page
def index(request):
	return render(request, 'epilogue/index.html')
# hotels page
def hotels(request):
	return render(request, 'epilogue/hotels.html')
# Saturday activities page
def saturday(request):
	return render(request, 'epilogue/saturday.html')
# restaurant suggestions page
def restaurants(request):
	return render(request, 'epilogue/restaurants.html')
# cape cod activities page
def activities(request):
	return render(request, 'epilogue/activities.html')
# directions page
def travel(request):
	return render(request, 'epilogue/travel.html')
# main itinerary page
def itinerary(request):
	return render(request, 'epilogue/itinerary.html')
# return image url
def getImage(request, id):
	url = static("images/slideshow/" + str(id) + ".jpg")
	return HttpResponse(url)
# guest locations page
def guestLoc(request):
	return render(request, 'epilogue/guestLoc.html')