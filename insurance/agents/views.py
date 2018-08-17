from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView, FormView, ListView

from apputils import appmessages as msg
from . import forms
from . import helper_utils
from .models import Agent


class AgentRegistration(View):
    def get(self, request):
        form = forms.AgentForm()
        context = {'form': form}
        return render(request, 'agents/agent_registration.html', context)

    def post(self, request):
        form = forms.AgentForm(request.POST)
        d = helper_utils.compare_password("as", "asx")

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
                return redirect('base2')
            else:
                return render(request, 'agents/agent_registration.html',
                              {'form': form, "error_message":  msg.EMAIL_EXISTS})
        return render(request, 'agents/agent_registration.html', {'form': form})

    def put(self, request):
        pass


class AgentLogin(TemplateView):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass


class BaseTemplate(TemplateView):
    template_name = 'agents/base_template.html'
    success_url = '/thanks/'


class RegAgentDjangoForm(FormView):
    model = Agent
    template_name = 'agents/agent_reg_django_frm.html'
    form_class = forms.AgentForm

    def get_context_data(self, **kwargs):
        context = super(RegAgentDjangoForm, self).get_context_data(**kwargs)
        context['form'] = forms.AgentForm()
        return context


@csrf_exempt
def register_agent(request):

    if request.method == 'POST':
        print('HURAAAAY We Got A POST')
        first_name = request.POST.get('first_name')
        print(first_name)
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


#  class SnippetListByUser(ListView):
 #       template_name = "my_templates/show_snippets.html"

 #       def get_queryset(self):
 #           return Snippet.objects.filter(user=self.request.user)


class AnyPage(TemplateView):
    template_name = 'agents/register.html'

#psql postgresql://insurance_user:!#Postgres!#@localhost:5432/insurance_db


