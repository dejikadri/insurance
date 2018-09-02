from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, FormView, ListView
from django.db.models import Q

from apputils import appmessages as msg
from . import forms
from . import helper_utils
from .models import Agent
from vehicles.models import Vehicles
from customers.models import Customer


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
                email = form.cleaned_data.get('email')
                password = helper_utils.sha512_crypt.encrypt(form.cleaned_data.get('password'))
                phone_number = form.cleaned_data.get('phone_number')

                Agent.objects.create(first_name=first_name, last_name=last_name,
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


class AgentListView(ListView):
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


class FindVehicle(View):
    def post(self, request):
        v_number = request.POST['q']
        vehicles = Vehicles.objects.filter(Q(policy_number__istartswith=v_number) | Q(registration_no__istartswith=v_number))
        return render(request, 'vehicles/vehicle_list_by_agent.html', {'vehicles': vehicles})

class Certificate(View):
    def get(self, request, id):

        vehicles = Vehicles.objects.get(id=id)
        customer = Customer.objects.get(id=vehicles.customer_id)
        cert_info = {'customer': customer, 'vehicles': vehicles}

        return render(request, 'vehicles/cert.html', cert_info)
        #return  HttpResponse(str(vehicles)+'  ---  '+str(customer))


# psql postgresql://insurance_user:!#Postgres!#@localhost:5432/insurance_db


