from django.test import TestCase, Client
from django.contrib.auth.models import User
from stcalander.models import Events
from django.urls import reverse
from django.utils import timezone
import pytz

class EventsCRUDTest(TestCase): 

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.event = Events.objects.create(
            user=self.user,
            name='Test Event',
            start=timezone.make_aware(timezone.datetime(2023, 5, 30, 10, 0, 0), timezone=pytz.UTC),
            end=timezone.make_aware(timezone.datetime(2023, 5, 30, 12, 0, 0), timezone=pytz.UTC),
            client_name='Test Client',
            client_phone='1234567890',
            client_address='123 Test Street',
            additional_info='Test additional info'
        )
    
# Test the login functionality
    def test_login(self):
        """
        Test that a user can log in successfully.
        """
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)

# Test adding a new event
    def test_add_event(self):
        """
        Test that a new event can be added successfully.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_event'), {
            'title': 'New Test Event',
            'start': '2023-06-01T10:00:00Z',
            'end': '2023-06-01T12:00:00Z',
            'client_name': 'New Test Client',
            'client_phone': '0987654321',
            'client_address': '456 Test Street',
            'additional_info': 'New Test additional info'
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'Success', 'msg': 'Event added successfully'})

# Test updating an existing event
    def test_update_event(self):
        """
        Test that an existing event can be updated successfully.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('update'), {
            'id': self.event.id,
            'title': 'Updated Test Event',
            'start': '2023-06-02T10:00:00Z',
            'end': '2023-06-02T12:00:00Z',
            'client_name': 'Updated Test Client',
            'client_phone': '1122334455',
            'client_address': '789 Test Street',
            'additional_info': 'Updated Test additional info'
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'Success', 'msg': 'Event updated successfully'})

# Test deleting an event
    def test_delete_event(self):
        """
        Test that an event can be deleted successfully.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('remove'), {'id': self.event.id})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'Success', 'msg': 'Event deleted successfully'})

# Test viewing all events for the logged-in user
    def test_view_all_events(self):
        """
        Test that all events for the logged-in user can be viewed successfully.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('all_events'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['title'], 'Test Event')

# Test unauthorized access
    def test_unauthorized_access(self):
        """
        Test that unauthorized users cannot access certain endpoints.
        """
        endpoints = [reverse('add_event'), reverse('update'), reverse('remove'), reverse('all_events')]
        for endpoint in endpoints:
            response = self.client.get(endpoint)
            self.assertEqual(response.status_code, 302)  #redirect to login

