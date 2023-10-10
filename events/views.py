from operator import imod
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import EventForm, ParticipantForm
from .models import Event, Participant
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class Events(View):
    def get(self, request):
        events = Event.objects.filter(event_status=1, approval=1)[:25]
        context = {
            'events': events,
        }
        return render(request, 'events.html', context)


def event(request, event_id, event_title=None):
    if request.method == 'GET':

        pform = ParticipantForm

        try:
            event = Event.objects.get(id=event_id, event_status=1, approval=1)
        except ObjectDoesNotExist:
            print('Post not found')
            return render(request, '404.html')

        try:
            participant = Participant.objects.filter(post=post_id)
        except:
            participant = None

        context = {
            'event': event,
            # 'commentForm': comment,
            'pform': pform,
            'page_title': event.title,
            # 'meta_logo': event.FeatureImage,
        }

    return render(request, 'event.html', context)


@login_required(login_url='/')
def addEvent(request):

    form = EventForm

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            print(request.POST)
            return redirect('/home')
        else:
            print('Event not saved')
            print(form.errors)

    context = {'form': form}

    return render(request, 'add_event.html', context)


@login_required(login_url='/')
def editEvent(request, pk):

    poll = Event.objects.get(id=pk)
    form = EventForm(instance=poll)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=poll)

        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            print('Event not saved')
            print(form.errors)

    context = {'form': form, 'id': pk}

    return render(request, 'edit_event.html', context)


@ login_required(login_url='/')
def delEvent(request, pk):

    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        event.delete()
        return redirect('/home')

    context = {'event': event, 'pk': pk}
    return render(request, 'delete_event.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class SubscribeView(View):
    # template_class = 'subscribed.html'
    model = Participant

    def post(self, request, *args, **kwargs):
        form = ParticipantForm(request.POST)

        email = request.POST.get('email')
        id = request.POST.get('event')
        event = Event.objects.get(id=id)
        subcr = Participant.objects.filter(email=email)

        if len(subcr) <= 0:

            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.event = event
                new_form.save()
                print('Subscriber saved')
        else:
            return redirect('/events/already_subscribed')

        return redirect('/events/thank_you')


class ThankYouView(TemplateView):
    """ Thank you page for newsletter subscribers """
    template_name = 'subscribed.html'


class AlreadySubscribed(TemplateView):
    """ Notification page for those already subscribed """
    template_name = 'already_subscribed.html'
