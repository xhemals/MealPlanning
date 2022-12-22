from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from . import gCalendar


class startForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))

    furthestEvent = datetime.strptime(gCalendar.furthestEvent(), "%Y-%m-%d %H:%M:%S")
    furthestEvent = furthestEvent.date()
    start_planning_from = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                # "min": (datetime.now().date() + timedelta(days=1)),
                "min": furthestEvent,
                "style": "max-width: 150px",
            }
        )
    )


class MealForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))

    persons = [(1, "All"), (2, "Jamie"), (3, "Chris"), (4, "Josey"), (5, "Toby")]

    meal = forms.CharField(required=True)
    who_is_eating = forms.MultipleChoiceField(
        required=True, choices=persons, widget=forms.CheckboxSelectMultiple()
    )
