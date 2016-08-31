from django.template import Library
from django.conf import settings

register = Library()

@register.filter
def slideshow_link(value):
  """
    Filter - returns link to slideshow pictures from number of picture:

    {% with 3|slideshow_link as link %}
    <img src="{{ link }} />

    Results with the HTML:
    <img src="/STATIC_URL/images/slideshow/3.jpg"

    Instead of 3 one may use the variable set in the views
  """
  return settings.STATIC_URL + "/images/slideshow/" + str(value) + ".jpg"