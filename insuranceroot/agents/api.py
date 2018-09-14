from tastypie.resources import ModelResource
from tastypie.constants import ALL

from .models import Agent


class AgentResource(ModelResource):
    class Meta:
        queryset = Agent.objects.all()
        resource_name = 'agent'
        allowed_methods = ['get']
        filtering = {'agent_number': ALL}
        excludes = ['password']

