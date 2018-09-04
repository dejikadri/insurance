from django.shortcuts import render, redirect


class AgentIsLoggedInMixin(object):
        def dispatch(self, request, *args, **kwargs):
            #if 'agent_id' in request.session:
            if not request.session.get('agent_id', None):
                print("yyyyyyyyyyy")
                return redirect('agentslogin')
            return super(AgentIsLoggedInMixin, self).dispatch(request, *args, **kwargs)

