from django.test import TestCase
from ..models import Vehicles


class AgentModelTest(TestCase):
    def setUp(self):
        agent_mike = Vehicles.objects.create(
            registration_no='Reg8',
            agent_id=1,
            customer_id=1,
            vehicle_make='Honda',
            vehicle_model='civic',
            policy_number='pol88'
        )
        agent_mike.save()

    def test_create_vehicle(self):
        new_agent = Vehicles.objects.create(
            registration_no='Reg9',
            agent_id=1,
            customer_id=1,
            vehicle_make='Honda',
            vehicle_model='Accord',
            policy_number='pol99'

        )
        new_agent.save()

        count_agent = Vehicles.objects.all()
        self.assertEqual(2, count_agent.count())

    def test_retrieve_vehicle(self):
        get_vehicle = Vehicles.objects.get(registration_no='Reg8')
        self.assertEqual('Honda', get_vehicle.vehicle_make)
