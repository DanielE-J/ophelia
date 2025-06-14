# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, reverse, redirect
from django.views import generic, View
from django.contrib.auth.models import User
import datetime
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Booking
from .forms import BookingForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MAX_BOOKINGS_PER_SLOT = 10

def get_user_instance(request):
    """
    Retrieves user details if logged in
    """
    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


class Reservations(View):
    """
    Displays the booking form and handles new bookings.
    """
    template_name = 'bookings/reservations.html'
    success_message = 'Booking has been made.'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            booking_form = BookingForm()
        return render(request, self.template_name, {'booking_form': booking_form})

    def post(self, request):
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)

            # Check time slot capacity
            date = booking.requested_date
            time = booking.requested_time

            existing_bookings = Booking.objects.filter(
                requested_date=date,
                requested_time=time
            ).count()

            if existing_bookings >= MAX_BOOKINGS_PER_SLOT:
                messages.error(request, "That time slot is fully booked. Please choose another.")
                return render(request, self.template_name, {'booking_form': booking_form})

            booking.user = request.user
            booking.save()
            messages.success(request, "Booking successful, awaiting confirmation.")
            return render(request, 'bookings/confirmed.html')

        return render(request, self.template_name, {'booking_form': booking_form})


class Confirmed(generic.DetailView):
    """
    Displays confirmation page for a successful booking
    """
    template_name = 'bookings/confirmed.html'

    def get(self, request):
        return render(request, self.template_name)


class BookingList(generic.ListView):
    """
    Lists current user's bookings
    """
    model = Booking
    template_name = 'bookings/booking_list.html'
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        today = datetime.date.today()
        bookings = Booking.objects.filter(user=request.user).order_by('-created_date')

        for booking in bookings:
            if booking.requested_date < today:
                booking.status = 'Booking Expired'

        paginator = Paginator(bookings, self.paginate_by)
        page = request.GET.get('page')
        booking_page = paginator.get_page(page)

        if request.user.is_authenticated:
            return render(
                request,
                self.template_name,
                {'booking_page': booking_page, 'bookings': bookings}
            )
        else:
            return redirect('accounts/login')


class EditBooking(SuccessMessageMixin, UpdateView):
    """
    Allows user to edit a booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/edit_booking.html'
    success_message = 'Booking has been updated.'

    def get_success_url(self, **kwargs):
        return reverse('booking_list')


def cancel_booking(request, pk):
    """
    Allows user to cancel a booking
    """
    booking = Booking.objects.get(pk=pk)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking cancelled")
        return redirect('booking_list')

    return render(request, 'bookings/cancel_booking.html', {'booking': booking})
