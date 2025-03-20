from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
# Create your views here.

monthly_challenge = {
    "january": "Eat no meat for a month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django at least 20 minutes every day!",
    "april": "Exercise 60 minutes every day!",
    "may": "Cardio 60 minutes every day!",
    "june": "Back 60 minutes every day!",
    "july": "Leg 60 minutes every day!",
    "august": "Chest 60 minutes every day!",
    "september": "Biceps y 60 minutes every day!",
    "october": "Core 60 minutes every day!",
    "november": "CODM 20 minutes every day!",
    "december": None
}


def index(request):
    # list_item = ""
    months = list(monthly_challenge.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Month not supported!</h1>")


"""
    for month in months:
        capitalize_months = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_item += f"<li><a href=\"{month_path}\">{capitalize_months}</a></li>"
    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)
"""

"""""
def january(requests):
    return HttpResponse("Eat no meat for a month!")
def february(requets):
    return HttpResponse("Walk for at least 20 minutes every day!")
def march(requets):
    return HttpResponse("Learn at least 20 minutes every day!")
"""

""""
def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for a month!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("Month not supported!")
    return HttpResponse(challenge_text)
"""
