from django.shortcuts import render, redirect
from django.http import HttpResponse
from MealPlanning.forms import MealForm, startForm
import datetime
from datetime import datetime, timedelta
from . import gCalendar
from .models import Meal

mealPersons = {
    1: "All",
    2: "Jamie",
    3: "Chris",
    4: "Josey",
    5: "Toby",
}


def suffix(day):
    suffix = ""
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix


def mealList():
    events = gCalendar.viewEvent()
    eventsLi = []
    Meal.objects.all().delete()
    for key, value in events.items():
        recordDate = datetime.strptime(value["date"], "%Y-%m-%d %H:%M:%S")
        recordDate = recordDate.date()
        newRecord = Meal(date=recordDate, meal=value["meal"], calID=value["calID"])
        newRecord.save()
        inputDate = datetime.strptime(value["date"], "%Y-%m-%d %H:%M:%S")
        ordinal = inputDate.strftime("%A, %B %d") + suffix(inputDate.day)
        eventsLi.append(
            f"<ul><li class='date'>{ordinal}<ol class='meal'>{value['meal']}</ol></li></ul>"
        )
    event = "".join(eventsLi)
    return event


def index(request):
    form = startForm()
    date = ""
    event = mealList()
    if request.method == "POST":
        if request.POST.get("submit"):
            date = request.POST.get("start_planning_from")
            request.session["date"] = date
            request.session["inputDate"] = ""
            request.session["times"] = 0
            return redirect("/planning")
    context = {"form": form, "date": date, "events": event}
    return render(request, "index.html", context)


def planning(request):
    if request.session.get("times", None) == 7:
        return redirect("/done")
    date = request.session.get("date", None)
    inputDate = datetime.strptime(date, "%Y-%m-%d")
    if request.session.get("inputDate", None):
        inputDate = datetime.strptime(
            request.session.get("inputDate", None), "%Y-%m-%d %H:%M:%S"
        )
    if request.method == "POST":
        form = MealForm(request.POST)
        values = form["who_is_eating"].value()
        meal = form["meal"].value()
        persons = []
        for i in values:
            temp = mealPersons[int(i)]
            persons.append(temp)
        persons = ", ".join(map(str, persons))
        print(persons)
        if request.POST.get("submit"):
            request.session["inputDate"] = str(inputDate + timedelta(days=1))
            request.session["times"] = request.session.get("times", None) + 1
            gCalendar.runCalendar(inputDate, meal, persons)
            return redirect("/planning")

    ordinal = inputDate.strftime("%A, %B %d") + suffix(inputDate.day)
    context = {
        "form": MealForm,
        "day": ordinal,
    }
    return render(request, "planning.html", context)


def done(request):
    return render(request, "done.html")
