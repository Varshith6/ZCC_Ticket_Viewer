from django.test import TestCase
from django.urls import reverse
#Includes basic unit tests to check for errors
def test_zendesk_list_view(self):
    url = reverse("zendesk_ticket_viewer.views.view_tickets")
    resp = self.client.get(url)

    self.assertEqual(resp.status_code, 200)
    self.assertIn(resp.content)

def test_view_url_accessible_by_name(self):
    response = self.client.get(reverse('view_tickets'))
    self.assertEqual(response.status_code, 200)

def test_view_uses_correct_template(self):
    response = self.client.get(reverse('view_tickets'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'templates/tickets.html')