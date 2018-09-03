from tastypie.resources import ModelResource
from tastypie.constants import ALL

from .models import Vehicles


class VehicleResource(ModelResource):
    class Meta:
        queryset = Vehicles.objects.all()
        resource_name = 'vehicle'
        allowed_methods = ['get']
        filtering = {'registration_no': ALL}
