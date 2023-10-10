from django.views.generic import TemplateView
from django.views import View
from django_tables2 import SingleTableView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from blog.models import Category, Post
from events.models import Event
from newsletter.forms import SubscribeForm
from polls.models import Question
from .tables import PollsTable, PostTable, EventsTable
from accounts.forms import CustomSignupForm


class HomePageView(TemplateView):
    template_name = 'home.html'
    extra_context = {'title': {"app": "FOSSFA", "page": " home"}}

# Main index page


def index(request):

    form = SubscribeForm

    context = {'form': form}
    return render(request, 'index.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')


class News(View):
    def get(self, request):
        posts = Post.objects.filter(PostStatus=1, Approval=1, category=1)[:25]
        params = {
            'posts': posts,
        }
        return render(request, 'news.html', params)

# Login page


@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    return redirect('/accounts/login')

# Logout function. Redirects user to index page on logout


def logoutPage(request):
    logout(request)
    return redirect('/accounts/login')


class SignupPageView(TemplateView):
    form = CustomSignupForm
    initial = {'key': 'value'}
    template_name = "signup.html"

    def get(self, request, *args, **kwargs):
        form = self.form(initial=self.initial)
        return render(request, self.template_name, {'form': form})


@login_required(login_url='/')
def home(request):
    return render(request, 'landing.html')


class DashboardListView(SingleTableView):
    model = Post
    table_class = PostTable
    template_name = 'landing.html'

    def get_queryset(self):
        return super().get_queryset().filter(Author=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)
        context['table_polls'] = PollsTable(
            Question.objects.filter(author=self.request.user.id), prefix="1-")
        context['table_events'] = EventsTable(
            Event.objects.filter(author=self.request.user.id), prefix="1-")
        return context
