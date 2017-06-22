from django.shortcuts import render

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, context=context, template_name='subscriptions/subscription_form.html')