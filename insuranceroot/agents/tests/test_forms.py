from unittest import TestCase
from django.test import Client
from ..forms import AgentForm
from ..models import Agent


class AgentFormTest(TestCase):
    def setUp(self):
        self.user = Agent.objects.create(email="user@mp.com", password="user", first_name="user", phone=12345678)


class UserFormTest(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = AgentForm(data={'email': "user@mp.com", 'password': "user", 'first_name': "user", 'phone': 12345678})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = AgentForm(data={'email': "", 'password': "mp", 'first_name': "mp", 'phone': ""})
        self.assertFalse(form.is_valid())