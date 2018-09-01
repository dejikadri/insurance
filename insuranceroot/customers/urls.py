from django.conf.urls import url
from .views import AddCustomer, ListCustomerByAgent, CustomerDetail, EditUpdateCustomer, FindCustomer


urlpatterns = [
    # url(r'^$', RegisterPageView.as_view()),
    url(r'^addcustomer/', AddCustomer.as_view(), name='addcustomer'),
    url(r'^findcustomer/', FindCustomer.as_view(), name='findcustomer'),
    url(r'^customerlist/', ListCustomerByAgent.as_view(), name='customerlist'),
    url(r'^customerdetail/(?P<pk>[0-9]+)$', CustomerDetail.as_view(), name='customerdetail'),
    url(r'^updatecustomer/(?P<pk>\d+)/', EditUpdateCustomer.as_view(), name='updatecustomer'),

]