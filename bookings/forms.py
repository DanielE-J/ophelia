from django import forms
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from .models import Booking, time_slots, Table
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    requested_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}
        )
    )

    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('+353123456789')}
    ))

    class Meta:
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

        if selected_date:
            available_slots = []
            for time_value, time_label in time_slots:
                count = Booking.objects.filter(
                    requested_date=selected_date,
                    requested_time=time_value
                ).count()

                max_bookings = Table.objects.count()

                if count < max_bookings:
                    available_slots.append((time_value, time_label))
            self.fields['requested_time'].choices = available_slots
        else:
            self.fields['requested_time'].choices = time_slots

        self.fields['requested_time'].error_messages['invalid_choice'] = (
            "This time slot is no longer available. Please select a different time."
        )

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('requested_date')
        time = cleaned_data.get('requested_time')

        if date and time:
            count = Booking.objects.filter(
                requested_date=date,
                requested_time=time
            ).count()

            max_bookings = Table.objects.count()

            if count >= max_bookings:
                raise forms.ValidationError(
                    f"Sorry, {time} on {date} is fully booked. Please choose a different time."
                )
        return cleaned_data
    

class CustomSignUpForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email address'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password (again)'
        })
    