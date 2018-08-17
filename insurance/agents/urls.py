from django.conf.urls import url
from .views import (AnyPage, BaseTemplate,
                    RegAgentDjangoForm, AgentRegistration, AgentListView)


urlpatterns = [
    # url(r'^$', RegisterPageView.as_view()),
    url(r'^basetemplate/', BaseTemplate.as_view(), name='basetemplate'),
    url(r'^agentdjangofrm/', RegAgentDjangoForm.as_view(), name='agentdjangofrm'),
    url(r'^agentregistration', AgentRegistration.as_view(), name='agentregistration' ),
    url(r'^agentslist', AgentListView.as_view(), name='agentslist')

]