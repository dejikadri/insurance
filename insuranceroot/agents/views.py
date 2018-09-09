from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from django.contrib.auth import logout
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, FormView, ListView, UpdateView
from vehicles.models import Vehicles

from apputils import appmessages as msg
from apputils.mixins import AgentIsLoggedInMixin
from customers.models import Customer

from . import forms
from . import helper_utils
from .models import Agent

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class AgentRegistration(View):
    def get(self, request):
        form = forms.AgentForm()
        context = {'form': form}
        return render(request, 'agents/agent_registration.html', context)

    # Agent registration
    def post(self, request):
        form = forms.AgentForm(request.POST)

        if form.is_valid():
            email_exists_status = helper_utils.check_if_email_exists(form.cleaned_data.get('email'))
            if not email_exists_status:
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                agent_number = helper_utils.gen_agent_number(first_name, last_name)

                email = form.cleaned_data.get('email')
                password = helper_utils.sha512_crypt.encrypt(form.cleaned_data.get('password'))
                phone_number = form.cleaned_data.get('phone_number')

                Agent.objects.create(first_name=first_name, last_name=last_name, agent_number=agent_number,
                                     email=email, password=password, phone_number=phone_number)
                # TODO redirect to an appropriate file e.g agent landing
                # TODO set the necessary session values, agentid, names, isloggedin and email as in AgentLogin Below
                return redirect('customerlist')
            else:
                return render(request, 'agents/agent_registration.html',
                              {'form': form, "error_message":  msg.EMAIL_EXISTS})
        return render(request, 'agents/agent_registration.html', {'form': form})

    def put(self, request):
        pass


class SiteIndex(TemplateView):
    template_name = 'agents/site_home.html'


class AgentLogin(View):
    def get(self, request):
        form = forms.AgentLoginForm()
        context = {'form': form}
        return render(request, 'agents/agent_login.html', context)

    def post(self, request):
        form = forms.AgentLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            auth_response = helper_utils.authenticate_user(email, password)

            if auth_response:
                request.session['email'] = form.cleaned_data.get('email')
                agent_info = Agent.objects.get(email=form.cleaned_data.get('email'))
                request.session['agent_id'] = agent_info.id
                request.session['names'] = f'{agent_info.first_name} - {agent_info.last_name}'
                request.session['agent_islogged_in'] = True
                return redirect('customerlist')
            else:
                return render(request, 'agents/agent_login.html', {'form': form, "error_message":  msg.INVALID_LOGIN})

        else:
            return render(request, 'agents/agent_login.html', {'form': form})


class AgentLogout(View):
    def get(self, request):
        form = forms.AgentLoginForm()
        logout(request)
        #request.session.flush()
        return redirect('agentslogin')


class EditUpdateAgent(AgentIsLoggedInMixin, UpdateView):
    model = Agent
    fields = ['first_name', 'last_name',  'email', 'phone_number', ]
    template_name = 'common/form_info.html'

    def form_valid(self, form):
        post = form.save()
        post.save()
        return redirect('vehiclelist')

class RegAgentDjangoForm(FormView):
    model = Agent
    template_name = 'agents/agent_reg_django_frm.html'
    form_class = forms.AgentForm

    def get_context_data(self, **kwargs):
        context = super(RegAgentDjangoForm, self).get_context_data(**kwargs)
        context['form'] = forms.AgentForm()
        return context


def register_agent(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        # redirect to show
        return HttpResponse("Saved")
    else:
        return render(request, 'agents/register_agent.html')


def base2(request):
    return render(request, 'common/base2.html')


class AgentListView(AgentIsLoggedInMixin,  ListView):
    model = Agent
    context_object_name = 'agents'
    template_name = 'agents/agent_list.html'

# class LoginNeededMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if not request.session['agent_islogged_in']:
#             HttpResponse


#  class SnippetListByUser(ListView):
 #       template_name = "my_templates/show_snippets.html"

 #       def get_queryset(self):
 #           return Snippet.objects.filter(user=self.request.user)


class FindInfo(TemplateView):
    template_name = 'agents/find.html'


class FindVehicle(AgentIsLoggedInMixin, View):
    def post(self, request):
        v_number = request.POST['q']
        vehicles = Vehicles.objects.filter(Q(policy_number__istartswith=v_number) | Q(registration_no__istartswith=v_number))
        return render(request, 'vehicles/vehicle_list_by_agent.html', {'vehicles': vehicles})

class Certificate(AgentIsLoggedInMixin, View):
    def get(self, request, id):

        vehicles = Vehicles.objects.get(id=id)
        customer = Customer.objects.get(id=vehicles.customer_id)
        cert_info = {'customer': customer, 'vehicles': vehicles}

        return render(request, 'vehicles/cert.html', cert_info)
        #return  HttpResponse(str(vehicles)+'  ---  '+str(customer))

def get_cars():
    # Queries 3 tables: cookbook_recipe, cookbook_ingredient,
    # and cookbook_food.
    return Vehicles.objects.all()

@cache_page(CACHE_TTL)
def car_view(request):
    return render(request, 'agents/cars.html', {
        'cars': get_cars()
    })
# psql postgresql://insurance_user:!#Postgres!#@localhost:5432/insurance_db


