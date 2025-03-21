from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
        raise Http404("page not found")

