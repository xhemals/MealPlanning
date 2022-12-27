from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from . import gCalendar

persons = [
    (1, "All"),
    (2, "Jamie"),
    (3, "Chris"),
    (4, "Josey"),
    (5, "Toby"),
    (6, "Other"),
]


class startForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit", css_class="btn btn-success"))
        self.furthestEvent = datetime.strptime(
            gCalendar.furthestEvent(), "%Y-%m-%d %H:%M:%S"
        )
        self.furthestEvent = self.furthestEvent.date()
        self.fields["start_planning_from"].widget.attrs.update(
            {
                "min": self.furthestEvent + timedelta(days=1),
            }
        )

    start_planning_from = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "style": "max-width: 150px",
            }
        )
    )


class MealForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit", css_class="btn btn-success"))
        self.helper.attrs.update({"id": "form_id"})

    meal = forms.CharField(required=True)
    who_is_eating = forms.MultipleChoiceField(
        required=True, choices=persons, widget=forms.CheckboxSelectMultiple()
    )
    other = forms.CharField(label=False, required=False)


class EditMealForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit", css_class="btn btn-success"))
        self.helper.attrs.update({"id": "form_id"})

    meal = forms.CharField(required=True)
    who_is_eating = forms.MultipleChoiceField(
        required=True, choices=persons, widget=forms.CheckboxSelectMultiple()
    )
    other = forms.CharField(label=False, required=False)


class deleteMeal(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Delete", css_class="btn btn-danger"))

    cornfirm = forms.BooleanField(
        error_messages={"required": "You must confirm the deletion"},
        label="Confirm",
    )
