from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Customer
from . import forms
from django.views.generic import View, TemplateView, FormView, ListView, DetailView, UpdateView
from apputils.mixins import AgentIsLoggedInMixin


class AddCustomer(AgentIsLoggedInMixin, View):
    def get(self, request):
        form = forms.CustomerForm()
        context = {'form': form}
        return render(request, 'customers/customer_info.html', context)

    def post(self, request):
        form = forms.CustomerForm(request.POST)
        if form.is_valid():
            agent_id = request.session['agent_id']
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')

            # TODO - add vehicle and payment details in one go ????

            Customer.objects.create(agent_id=agent_id, first_name=first_name, last_name=last_name,
                                    email=email, phone_number=phone_number)
            return redirect('customerlist')


class ListCustomerByAgent(AgentIsLoggedInMixin, ListView):
    # model = Customer
    context_object_name = 'customers'
    template_name = 'customers/customer_list_by_agent.html'

    def get_queryset(self):
        return Customer.objects.filter(agent_id=self.request.session['agent_id'])


class CustomerDetail(AgentIsLoggedInMixin, DetailView):
    model = Customer

    # template_name = 'customers/customer_detail.html'
    # context_object_name = 'customer'

    # def get_queryset(self):
    # return Customer.objects.filter(id=self.request['pk'])


class EditUpdateCustomer(AgentIsLoggedInMixin, UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'phone_number', 'email', ]
    template_name = 'common/form_info.html'

    def form_valid(self, form):
        post = form.save()
        post.save()
        return redirect('customerlist')

class FindCustomer(AgentIsLoggedInMixin, View):
    def post(self, request):
        v_number = request.POST['q']
        print(request.POST['q'])
        customers = Customer.objects.filter(Q(first_name__istartswith=v_number) | Q(last_name__istartswith=v_number))
        return render(request, 'customers/customer_list_by_agent.html', {'customers': customers})