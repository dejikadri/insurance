from tastypie.resources import ModelResource
from tastypie.constants import ALL

from .models import Agent


class VehicleResource(ModelResource):
    class Meta:
        queryset = Agent.objects.all()
        resource_name = 'agent'
        allowed_methods = ['get']
        filtering = {'registration_no': ALL}
