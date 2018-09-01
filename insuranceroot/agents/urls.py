from django.conf.urls import url
from .views import (AgentLogin, AgentLogout, FindInfo,
                    RegAgentDjangoForm, AgentRegistration, AgentListView, SiteIndex)


urlpatterns = [
    # url(r'^$', RegisterPageView.as_view()),
    url(r'^$', SiteIndex.as_view(), name='home'),
    url(r'^findinfo/', FindInfo.as_view(), name='findinfo'),
    url(r'^agentdjangofrm/', RegAgentDjangoForm.as_view(), name='agentdjangofrm'),
    url(r'^agentregistration', AgentRegistration.as_view(), name='agentregistration' ),
    url(r'^agentslist', AgentListView.as_view(), name='agentslist'),
    url(r'^agentslogin', AgentLogin.as_view(), name='agentslogin'),
    url(r'^agentslogout', AgentLogout.as_view(), name='agentslogout'),

]