from django.conf.urls import url
from .views import AddCustomer, ListCustomerByAgent, CustomerDetail


urlpatterns = [
    # url(r'^$', RegisterPageView.as_view()),
    url(r'^addcustomer/', AddCustomer.as_view(), name='addcustomer'),
    url(r'^customerlist/', ListCustomerByAgent.as_view(), name='customerlist'),
    url(r'^customerdetail/(?P<pk>[0-9]+)$', CustomerDetail.as_view(), name='customerdetail'),

]