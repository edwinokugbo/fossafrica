# tables.py
import django_tables2 as tables
from django_tables2.utils import A
from blog.models import Post
from polls.models import Question


class PostTable(tables.Table):
    Edit = tables.LinkColumn('blog:editpost', text='Edit', args=[A('pk')], attrs={
        'a': {'class': 'btn', 'style': 'color: purple; width:100%;'}
    })
    Del = tables.LinkColumn('blog:delpost', text='Del', args=[A('pk')], attrs={
        'a': {'class': 'btn', 'style': 'color: red; width:100%;'}
    })

    class Meta:
        model = Post
        template_name = "django_tables2/bootstrap.html"
        fields = ("Title", "Subtitle", "DateCreated", "PostStatus", "Approval")


class PollsTable(tables.Table):
    Edit = tables.LinkColumn('polls:edit_poll', text='Edit', args=[A('pk')], attrs={
        'a': {'class': 'btn', 'style': 'color: purple; width:100%;'}
    })
    Del = tables.LinkColumn('polls:del_poll', text='Del', args=[A('pk')], attrs={
        'a': {'class': 'btn', 'style': 'color: red; width:100%;'}
    })

    class Meta:
        model = Question
        template_name = "django_tables2/bootstrap.html"
        fields = ("question_text", "pub_date",
                  "author", "privacy", "poll_status")


class EventsTable(tables.Table):
    Edit = tables.LinkColumn('events:edit_event', text='Edit', args=[A('pk')], attrs={
        'a': {'class': 'btn', 'style': 'color: purple; width:100%;'}
    })
    Del = tables.LinkColumn('events:del_event', text='Del', args=[A('pk')], attrs={
        'a': {'class': 'btn', 'style': 'color: red; width:100%;'}
    })

    class Meta:
        model = Question
        template_name = "django_tables2/bootstrap.html"
        fields = ("title", "date_created",
                  "author", "privacy", "event_status")
