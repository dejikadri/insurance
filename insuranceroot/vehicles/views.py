from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, FormView, ListView, UpdateView
from django.db.models import Q

from apputils import appmessages as msg
from apputils.mixins import AgentIsLoggedInMixin

from . import forms
from .models import Vehicles, Product, Agent, Customer, Payment

from . import v_helper


class VehicleInfo(AgentIsLoggedInMixin, View):
    def get(self, request, customer_id):
        form = forms.VehiclesForm()

        context = {'form': form, 'customer_id': customer_id}
        return render(request, 'vehicles/vehicle_info.html', context)

    def post(self, request, customer_id):
        form = forms.VehiclesForm(request.POST)
        if form.is_valid():
            policy_number="pol111"
            agent_id = request.session['agent_id']
            engine_no = form.cleaned_data.get('engine_no')
            registration_no = form.cleaned_data.get('registration_no')
            vehicle_make = form.cleaned_data.get('vehicle_make')
            vehicle_model = form.cleaned_data.get('vehicle_model')

            Vehicles.objects.create(policy_number=policy_number, customer_id=customer_id, agent_id=agent_id,
                                    engine_no=engine_no, registration_no=registration_no, vehicle_make=vehicle_make,
                                    vehicle_model=vehicle_model)
            # TODO redirect to vehicle-list
            # TODO pass customer_id via query string
            # return render(request, 'customers/customer_list_by_agent.html')
            return redirect('vehiclelist')
        else:
            return render(request, 'vehicles/vehicle_info.html', {'form': form, })


class ListVehicleByAgent(AgentIsLoggedInMixin, ListView):
    # model = Customer
    context_object_name = 'vehicles'
    template_name = 'vehicles/vehicle_list_by_agent.html'

    def dispatch(self, *args, **kwargs):
        return super(ListVehicleByAgent, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Vehicles.objects.filter(agent_id=self.request.session['agent_id'])

class ListPaymentsByAgent(AgentIsLoggedInMixin, ListView):
    # model = Customer
    context_object_name = 'payments'
    template_name = 'payments/payment_list_by_agent.html'

    def get_queryset(self):
        return Payment.objects.filter(agent_id=self.request.session['agent_id'])


class MakePayment(AgentIsLoggedInMixin, TemplateView):
    def get(self, request, vehicle_id):
        form = forms.PaymentForm()
        products = Product.objects.all()
        vehicle = Vehicles.objects.filter(id=vehicle_id).values()
        #customer = Customer.objects.filter(id-customer_id)

        #product_dict = model_to_dict(Product.objects.filter(id=1).first())

        context = {'form': form,  'products': products, 'vehicle': vehicle }
        return render(request, 'payments/payment_info.html', context)

    def post(self, request, vehicle_id):
        form = forms.PaymentForm(request.POST)
        if form.is_valid():
            agent_id = request.session['agent_id']
            product_code = form.cleaned_data.get('product')
            amount = request.POST['product']
            # TODO - get policy number and update vehicle data
            policy_number = v_helper.gen_policy_number()
            # TODO - create new payment record
            # TODO - calculate expiry date
            # TODO - get customer_id using vehicle_id
            customer_id = Vehicles.objects.get(id=vehicle_id).customer_id
            product_id = Product.objects.get(product_code=product_code).id

            Payment.objects.create(policy_number=policy_number, amount=amount, product_id=product_id, agent_id=agent_id,
                                   customer_id=customer_id, vehicle_id=vehicle_id)

            vehicle = Vehicles.objects.get(id=vehicle_id)
            vehicle.policy_number = policy_number
            vehicle.save(update_fields=['policy_number'])

            return redirect('vehiclelist')


class EditUpdatePayment(AgentIsLoggedInMixin, UpdateView):
    model = Payment
    fields = ['policy_number', 'amount', ]
    template_name = 'common/form_info.html'

    def form_valid(self, form):
        post = form.save()
        post.save()
        return redirect('paymentlist')


class EditUpdateVehicle(AgentIsLoggedInMixin, UpdateView):
    model = Vehicles
    fields = ['policy_number', 'engine_no', 'registration_no', 'vehicle_make', 'vehicle_model', ]
    template_name = 'common/form_info.html'

    def form_valid(self, form):
        post = form.save()
        post.save()
        return redirect('vehiclelist')

class FindVehicle(AgentIsLoggedInMixin, View):
    def post(self, request):
        v_number = request.POST['q']
        print(request.POST['q'])
        vehicles = Vehicles.objects.filter(Q(policy_number__istartswith=v_number) | Q(registration_no__istartswith=v_number))
        return render(request, 'vehicles/vehicle_list_by_agent.html', {'vehicles': vehicles})


# def get_recipes():
#     # Queries 3 tables: cookbook_recipe, cookbook_ingredient,
#     # and cookbook_food.
#     return list(Recipe.objects.prefetch_related('ingredient_set__food'))
#
# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
#
#
# @cache_page(CACHE_TTL)
# def recipes_view(request):
#     return render(request, 'cookbook/recipes.html', {
#         'recipes': get_recipes()
#     })