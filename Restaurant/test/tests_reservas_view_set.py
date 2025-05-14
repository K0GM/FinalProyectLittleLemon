from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Reservas
from django.utils import timezone


class ReservasViewSetTest(APITestCase):

    def setUp(self):
        self.reserva = Reservas.objects.create(name="John Doe", no_of_guests=4, bookingdate=timezone.now())
        self.url = reverse('reservas-list')  # URL name registered in your router

    def test_get_reservas_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_reserva(self):
        data = {
            "name": "Jane Doe",
            "no_of_guests": 2,
            "bookingdate": "2024-10-12T12:00:00Z"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservas.objects.count(), 2)

    def test_update_reserva(self):
        url = reverse('reservas-detail', args=[self.reserva.id])
        data = {
            "name": "Updated Doe",
            "no_of_guests": 5,
            "bookingdate": "2024-10-15T14:00:00Z"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.reserva.refresh_from_db()
        self.assertEqual(self.reserva.name, "Updated Doe")

    def test_delete_reserva(self):
        url = reverse('reservas-detail', args=[self.reserva.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reservas.objects.count(), 0)

