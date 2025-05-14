from django.test import TestCase
from .models import Menu, Reservas


class MenuModelTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="Test Menu", price=50.00, inventory=10)

    def test_menu_creation(self):
        menu = Menu.objects.get(title="Test Menu")
        self.assertEqual(menu.title, "Test Menu")
        self.assertEqual(menu.price, 50.00)
        self.assertEqual(menu.inventory, 10)

    def test_menu_str_representation(self):
        menu = Menu.objects.get(title="Test Menu")
        self.assertEqual(str(menu), "Test Menu")


class ReservasModelTest(TestCase):

    def setUp(self):
        Reservas.objects.create(name="John Doe", no_of_guests=4, bookingdate="2024-10-10T10:00:00Z")

    def test_reservas_creation(self):
        reserva = Reservas.objects.get(name="John Doe")
        self.assertEqual(reserva.name, "John Doe")
        self.assertEqual(reserva.no_of_guests, 4)
        self.assertEqual(str(reserva.bookingdate), "2024-10-10 10:00:00+00:00")

    def test_reservas_str_representation(self):
        reserva = Reservas.objects.get(name="John Doe")
        self.assertEqual(str(reserva), "John Doe")

