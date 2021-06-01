from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hellowworld</h1>")
	return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
	my_content = { "title" : "cool title",
				  "my_text": "this is cool",
	              "my_number": 123,
	              "my_list": [123, 455, 'abc'],
	              }
	return render(request, "contact.html", my_content)


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})


def portfolio_view(request, *args, **kwargs):
	return render(request, "portfolio.html", {})
