from django.shortcuts import render
from django.http import HttpResponse
from django import forms

#Formsets
class HangmanForm(forms.Form):
    alpha_list = ["a", "b", "c", "d"]

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def starter(request):

	if request.method == "POST":

		pick = request.POST.get("alpha_pick", "")	

		picks = request.session['picks']
		picks.append(pick)
		request.session['picks'] = picks

		form = HangmanForm()
		projectName = "Hang in there Hangman!"
		context = {
			"forma": form,
			"headerName": projectName,
			"picks" : picks
		}

		return render(request, "starter.html", context)

	else:

		request.session['word'] = 'avokado'
		form = HangmanForm()
		#array
		request.session['picks'] = []

		projectName = "Hang in there Hangman!"
		context = {
			"forma": form,
			"headerName": projectName
		}

		return render(request, "starter.html", context)
