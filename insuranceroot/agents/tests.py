from django.conf import settings

from django.test import TestCase
from .models import Agent


class AgentModelTest(TestCase):
    def setUp(self):
        agent_mike = Agent.objects.create(
            first_name='Mike',
            last_name='Smith',
            email='msmith@insure-i.com',
            phone_number='0800-000-0002',
        )
        agent_mike.save()

    def test_create_agent(self):
        new_agent = Agent.objects.create(
            first_name='Emeka',
            last_name='George',
            email='egeorge@abc.com',
            phone_number='0800-111-0002',
        )
        new_agent.save()

        count_agent = Agent.objects.all()
        self.assertEqual(2, count_agent.count())

    def test_retrieve_agent(self):
        get_agent_mike = Agent.objects.get(email='msmith@insure-i.com')
        self.assertEqual('msmith@insure-i.com', get_agent_mike.email)
