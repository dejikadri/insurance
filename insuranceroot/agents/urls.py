from django.conf.urls import url
from .views import (AnyPage, AgentLogin, AgentLogout,
                    RegAgentDjangoForm, AgentRegistration, AgentListView)


urlpatterns = [
    # url(r'^$', RegisterPageView.as_view()),
    url(r'^agentdjangofrm/', RegAgentDjangoForm.as_view(), name='agentdjangofrm'),
    url(r'^agentregistration', AgentRegistration.as_view(), name='agentregistration' ),
    url(r'^agentslist', AgentListView.as_view(), name='agentslist'),
    url(r'^agentslogin', AgentLogin.as_view(), name='agentslogin'),
    url(r'^agentslogout', AgentLogout.as_view(), name='agentslogout'),
    url(r'^anypage', AnyPage.as_view(), ),
    url(r'^$', AnyPage.as_view(), )

]