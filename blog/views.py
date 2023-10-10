from django.views.generic import TemplateView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment

from .forms import CommentForm, PostForm


class HomePageView(TemplateView):
    template_name = 'home.html'
    extra_context = {'title': {"app": "FOSSFA", "page": " home"}}


class Blog(View):
    def get(self, request):
        posts = Post.objects.filter(PostStatus=1, Approval=1)[:25]
        params = {
            'posts': posts,
        }
        return render(request, 'blog.html', params)


def post(request, post_id, post_title=None):
    if request.method == 'GET':

        comment = CommentForm

        try:
            post = Post.objects.get(id=post_id, PostStatus=1, Approval=1)
        except ObjectDoesNotExist:
            print('Post not found')
            return render(request, '404.html')

        try:
            comments = Comment.objects.filter(post=post_id)
        except:
            comments = None

        context = {
            'post': post,
            'commentForm': comment,
            'comments': comments,
            'page_title': post.Title,
            'meta_logo': post.FeatureImage,
        }

        print(post.FeatureImage)

    return render(request, 'post.html', context)


@login_required(login_url='/')
def addPost(request):

    form = PostForm

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            print('Post not saved')
            print(form.errors)

    context = {'form': form}
    return render(request, 'addpost.html', context)


@login_required(login_url='/')
def editPost(request, pk):

    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            print('Post not saved')
            print(form.errors)

    context = {'form': form, 'id': pk,
               'FeatureImage': post.FeatureImage}

    return render(request, 'edit_post.html', context)


@ login_required(login_url='/')
def delPost(request, pk):

    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('/home')

    context = {'post': post, 'pk': pk}
    return render(request, 'delete.html', context)


def postComment(request, pk):

    form = CommentForm
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            print(request.POST)
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.save()
            print('Saved Comment')
            # return redirect('/blog/post/' + pk + '/SDSSDSS')
        else:
            print('Comment not saved')
            print(form.errors)

    context = {'commentForm': 'form'}

    return redirect('/blog/post/' + pk + '/' + post.Title.replace(" ", "-").lower())
