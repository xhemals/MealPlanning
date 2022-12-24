from django.shortcuts import render, redirect
from django.http import HttpResponse
from MealPlanning.forms import MealForm, startForm, EditMealForm
import datetime
from datetime import datetime, timedelta
from . import gCalendar
from .models import Meal
from django.views.generic import DetailView
import re

mealPersons = {
    1: "All",
    2: "Jamie",
    3: "Chris",
    4: "Josey",
    5: "Toby",
}


class MealView(DetailView):
    model = Meal
    template_name = "meal_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pk"] = self.kwargs.get("pk")
        form = EditMealForm()
        fullName = self.object.meal
        mealName = re.sub("^.*?- ", "", fullName)
        persons = re.sub(" -.*", "", fullName)
        persons = re.sub(",", "", persons).split(" ")
        personsLi = []
        for x in persons:
            for key, value in mealPersons.items():
                if value == x:
                    personsLi.append(key)
        form.fields["meal"].initial = mealName
        form.fields["who_is_eating"].initial = personsLi
        context["form"] = form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == "POST":
            form = EditMealForm(request.POST)
            values = form["who_is_eating"].value()
            meal = form["meal"].value()
            persons = []
            for i in values:
                temp = mealPersons[int(i)]
                persons.append(temp)
            persons = ", ".join(map(str, persons))
            print(persons)
            if request.POST.get("submit"):
                gCalendar.editEvent(meal, persons, self.object.eventID)
                return redirect("/")

        return render(request, "meal_detail.html")


def meal(request):
    if request.method == "POST":
        if request.POST.get("submit"):
            print("post")
    test = MealView.get_context_data()
    context = {"test": test}
    return render(request, "meal_detail.html", context)


def suffix(day):
    suffix = ""
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix


def mealToDB():
    events = gCalendar.viewEvent()
    Meal.objects.all().delete()
    for key, value in events.items():
        recordDate = datetime.strptime(value["date"], "%Y-%m-%d %H:%M:%S")
        recordDate = recordDate.date()
        newRecord = Meal(date=recordDate, meal=value["meal"], eventID=value["eventID"])
        newRecord.save()


def viewMeals():
    db = Meal.objects.all()
    eventsLi = []
    for item in db:
        ordinal = item.date.strftime("%A, %B %d") + suffix(item.date.day)
        eventsLi.append(
            f"""<ul><li class='date'>{ordinal}
            <a href='/meal/{item.eventID}'><button type='button' class='btn btn-danger'> edit </button></a> 
            <ol class='meal'>{item.meal}</ol></li></ul><br>"""
        )
    event = "".join(eventsLi)
    return event


def index(request):
    form = startForm()
    date = ""
    mealToDB()
    event = viewMeals()
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
