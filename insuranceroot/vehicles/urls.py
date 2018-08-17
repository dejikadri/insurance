from django.conf.urls import url
from .views import VehicleInfo, ListVehicleByAgent,ListPaymentsByAgent, MakePayment


urlpatterns = [
    url(r'^addvehicle/(?P<customer_id>\d+)/', VehicleInfo.as_view(), name='addvehicle'),
    url(r'^vehiclelist/', ListVehicleByAgent.as_view(), name='vehiclelist'),
    url(r'^paymentlist/', ListPaymentsByAgent.as_view(), name='paymentlist'),
    url(r'^addpayment/(?P<vehicle_id>\d+)/', MakePayment.as_view(), name='addpayment'),
    # url(r'^customerdetail/(?P<pk>[0-9]+)$', CustomerDetail.as_view(), name='customerdetail'),

]