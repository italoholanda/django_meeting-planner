from .models import Meeting
from django.forms import DateInput, ModelForm, ValidationError
from datetime import date


class MeetingForm(ModelForm):

    class Meta:
        model = Meeting
        fields = "__all__"
        widgets = {
            'date': DateInput(attrs={"type": "date"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meeting cannot be in the past.")
        return d
