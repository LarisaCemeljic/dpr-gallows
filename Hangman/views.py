from django.shortcuts import render
from django import forms
from .models import Word
import random


# Formsets
class HangmanForm(forms.Form):

    # Larisa
    # Treba dodati sva slova
    alpha_list = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
        "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "z", "x", "y"]


def home(request):
    context = {
        "message": "This is message from the depths of the Earth!"
    }
    return render(request, "home.html", context)


def starter(request):

    if request.method == "POST":

        pick = request.POST.get("alpha_pick", "")
        picks = request.session['picks']
        picks.append(pick)
        request.session['picks'] = picks

        text_question = request.session['word']
        scorecount = 0

        hidden_text = []
        isWin = 0
        for x in range(0, len(text_question)):
            if text_question[x] in picks:
                hidden_text.append(text_question[x])
                isWin = isWin + 1
                scorecount = scorecount + 10

            elif text_question[x] == " ":
                hidden_text.append("-")
                isWin = isWin + 1
            else:
                hidden_text.append("_")

        trys = request.session['trials']
        trys = trys + 1
        for x in range(0, len(text_question)):
            if text_question[x] == pick:
                trys = trys - 1
                break

        request.session['trials'] = trys

        if(isWin == len(text_question) or trys >= 5):
            winstatus = ""
            scorecount = scorecount * len(text_question)
            if trys < 5:
                winstatus = "YOU WIN! :)"
            else:
                winstatus = "YOU LOSE! :("

            context = {
                "word": text_question,
                "winStatus": winstatus,
                "score": scorecount,
            }

            return render(request, "endgame.html", context)
        else:

            form = HangmanForm()
            projectName = "Hang in there Hangman!"
            context = {
                "forma": form,
                "headerName": projectName,
                "picks": picks,
                "hiddenWord": hidden_text,
                "cheat": text_question
            }

            return render(request, "starter.html", context)
    # new game
    else:

        # Znaci iz baze dohvati zapis sa random indexom
        rnd_index = random.randint(0, Word.objects.count() - 1)
        word = Word.objects.all()[rnd_index]
        text_question = word.word

        # text_question = 'avokado mango'
        request.session['word'] = text_question

        # array
        request.session['picks'] = []
        request.session['trials'] = 0
        hidden_text = []
        for x in range(0, len(text_question)):
            if text_question[x] == " ":
                hidden_text.append("-")
            else:
                hidden_text.append("_")

        projectName = "Hang in there Hangman!"
        form = HangmanForm()
        context = {
            "forma": form,
            "headerName": projectName,
            "hiddenWord": hidden_text,
            "cheat": text_question
        }

        return render(request, "starter.html", context)
