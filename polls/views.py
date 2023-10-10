from secrets import choice
from django.shortcuts import redirect, render
from .models import Question, Choice, Vote
from .forms import ChoiceForm, QuestionForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import F


def index(request):

    questions = Question.objects.filter()[:25]

    context = {'questions': questions}
    return render(request, 'polls.html', context)


# class PollChoicesView(TemplateView):
#     model = Choice
#     poll_id = 1
#     # table_class = PostTable
#     template_name = "poll_choices.html"

#     def get_queryset(self):
#         return super().get_queryset().filter(Question=self.poll_id)

@login_required(login_url='/login')
def pollChoices(request, pk):
    print('Here...')
    choices = Choice.objects.filter(question=pk)

    try:
        haveVoted = Vote.objects.filter(question=pk, author=request.user)

        if haveVoted:
            return redirect('/polls/vote_now/' + str(haveVoted[0].choice.id))
    except:
        # Do nothig. Jst continue
        Nothing = 0

    if choices:
        question = Question.objects.get(id=pk)
        context = {'choices': choices, 'question': question}
    else:
        return redirect('/polls')

    return render(request, 'poll_choices.html', context)


@ login_required(login_url='/')
def voteNow(request, pk):

    choice = Choice.objects.get(id=pk)
    question = Question.objects.get(id=choice.question.id)

    choices = Choice.objects.filter(question=choice.question.id)
    votes = Vote.objects.filter(question=choice.question.id).count()
    context = {'choices': choices, 'question': question, 'votes': votes}

    haveVoted = Vote.objects.filter(question=question, author=request.user)

    if not haveVoted:
        vote = Vote(question=choice.question, choice=choice,
                    author=request.user, vote_date=timezone.now())
        vote.save()

        choice_count = Choice.objects.filter(id=pk).update(votes=F('votes')+1)

        if question.show_result == 1:

            context = {}
            return render(request, 'poll_result.html', context)
    else:
        return render(request, 'poll_result.html', context)

    return redirect('/polls')


@login_required(login_url='/')
def addPoll(request):

    form = QuestionForm

    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            # form.save()
            print(request.POST)
            return redirect('/home')
        else:
            print('Poll not saved')
            print(form.errors)

    context = {'form': form}
    return render(request, 'add_poll.html', context)


@login_required(login_url='/')
def editPoll(request, pk):

    poll = Question.objects.get(id=pk)
    choices = Choice.objects.filter(question=poll.id)
    form = QuestionForm(instance=poll)
    choice_form = ChoiceForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=poll)

        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            print('Poll not saved')
            print(form.errors)

    context = {'form': form, 'choice_form': choice_form,
               'id': pk, 'choices': choices}

    return render(request, 'edit_poll.html', context)


@ login_required(login_url='/')
def delPoll(request, pk):

    poll = Question.objects.get(id=pk)

    if request.method == 'POST':
        poll.delete()
        return redirect('/home')

    context = {'poll': poll, 'pk': pk}
    return render(request, 'delete_poll.html', context)


def addChoice(request, pk):
    form = ChoiceForm

    if request.method == 'POST':
        form = ChoiceForm(request.POST, request.FILES,)
        poll = Question.objects.get(id=pk)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.question = poll
            new_form.save()
            # form.save()
            print(request.POST)
            return redirect('/polls/edit_poll/' + str(pk))
        else:
            print('Poll not saved')
            print(form.errors)

    print('Choices')
    context = {'id': pk}
    return redirect('/polls/edit_poll/' + str(pk))


def editChoice(request, pk):

    context = {}
    return render(request, 'add_poll.html', context)


def delChoice(request, pk):

    choice = Choice.objects.get(id=pk)

    if request.method == 'POST':
        choice.delete()
        return redirect('/home')

    context = {'choice': choice, 'pk': pk}
    return render(request, 'delete_choice.html', context)
