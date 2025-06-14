from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bookings.views import Reservations, Confirmed, BookingList, EditBooking, cancel_booking
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Test that all the correct urls are used when requested


class TestReservationsUrls(SimpleTestCase):
    """
    This class is for testing the bookings app URLs.
    """

    def test_reservations_resolved(self):
        url = reverse('reservations')
        self.assertEqual(resolve(url).func.view_class, Reservations)

    def test_confirmed_resolved(self):
        url = reverse('confirmed')
        self.assertEqual(resolve(url).func.view_class, Confirmed)

    def test_booking_list_resolved(self):
        url = reverse('booking_list')
        self.assertEqual(resolve(url).func.view_class, BookingList)

    def test_edit_booking_url_resolved(self):
        url = reverse('edit_booking', args=['1'])
        self.assertEqual(resolve(url).func.view_class, EditBooking)

    def test_delete_booking_url_resolved(self):
        url = reverse('cancel_booking', args=['1'])
        self.assertEqual(resolve(url).func, cancel_booking)