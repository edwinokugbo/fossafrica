from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from .models import Subscriber
from .forms import SubscribeForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class SubscribeView(View):
    # template_class = 'subscribed.html'
    model = Subscriber

    def post(self, request, *args, **kwargs):

        email = request.POST.get('email')

        subcr = Subscriber.objects.filter(email=email)

        if len(subcr) <= 0:

            form = SubscribeForm(request.POST)

            if form.is_valid:
                form.save()
                print('Subscriber saved')
        else:
            return redirect('/newsletter/already_subscribed')

        return redirect('/newsletter/thank_you')


class ThankYouView(TemplateView):
    """ Thank you page for newsletter subscribers """
    template_name = 'subscribed.html'


class AlreadySubscribed(TemplateView):
    """ Notification page for those already subscribed """
    template_name = 'already_subscribed.html'
