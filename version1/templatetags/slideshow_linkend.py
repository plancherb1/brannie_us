from django.template import Library

register = Library()

@register.filter
def slideshow_linkend(value):
  """
    Filter - returns link to slideshow pictures from number of picture:

    {% with linkend as 3|slideshow_linkend %}
    <img src="{% static linkend %} />

    Results with the HTML:
    <img src="/STATIC_URL/images/slideshow/3.jpg"

    Instead of 3 one may use the variable set in the views
  """
  return "/images/slideshow/" + str(value) + ".jpg"