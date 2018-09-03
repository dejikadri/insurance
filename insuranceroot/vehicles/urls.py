from django.conf.urls import url, include
from .views import VehicleInfo, ListVehicleByAgent,ListPaymentsByAgent, MakePayment, \
    EditUpdatePayment, EditUpdateVehicle, FindVehicle

from tastypie.api import Api
from .api import VehicleResource

v1_api = Api(api_name='v1')
v1_api.register(VehicleResource())


urlpatterns = [
    url(r'^addvehicle/(?P<customer_id>\d+)/', VehicleInfo.as_view(), name='addvehicle'),
    url(r'^api/', include(v1_api.urls) ),
    url(r'^findvehicle/', FindVehicle.as_view(), name='findvehicle'),
    url(r'^cert/', FindVehicle.as_view(), name='cert'),
    url(r'^vehiclelist/', ListVehicleByAgent.as_view(), name='vehiclelist'),
    url(r'^updatevehicle/(?P<pk>\d+)/', EditUpdateVehicle.as_view(), name='updatevehicle'),
    url(r'^paymentlist/', ListPaymentsByAgent.as_view(), name='paymentlist'),
    url(r'^addpayment/(?P<vehicle_id>\d+)/', MakePayment.as_view(), name='addpayment'),
    url(r'^updatepayment/(?P<pk>\d+)/', EditUpdatePayment.as_view(), name='updatepayment'),
    # url(r'^customerdetail/(?P<pk>[0-9]+)$', CustomerDetail.as_view(), name='customerdetail'),

]