from django import forms
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from .models import Booking, time_slots

MAX_BOOKINGS_PER_SLOT = 10

class BookingForm(forms.ModelForm):
    requested_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}
        )
    )

    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('+353123456789')}
    ))

    class Meta:  # 👈 this must be indented to be inside BookingForm
        model = Booking
        fields = (
            'name',
            'phone',
            'email',
            'guest_count',
            'requested_date',
            'requested_time',
        )

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    selected_date = self.data.get('requested_date') or self.initial.get('requested_date')

    if isinstance(selected_date, str):
        try:
            selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
        except ValueError:
            selected_date = None
    elif not isinstance(selected_date, datetime.date):
        selected_date = None

    if selected_date:
        available_slots = []
        for time_value, time_label in time_slots:
            count = Booking.objects.filter(
                requested_date=selected_date,
                requested_time=time_value
            ).count()
            if count < MAX_BOOKINGS_PER_SLOT:
                available_slots.append((time_value, time_label))
        self.fields['requested_time'].choices = available_slots
    else:
        self.fields['requested_time'].choices = time_slots

    self.fields['requested_time'].error_messages['invalid_choice'] = (
        "This time slot is no longer available. Please select a different time."
    )

