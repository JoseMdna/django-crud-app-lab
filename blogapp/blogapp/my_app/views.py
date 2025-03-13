from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm, CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'my_app/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'my_app/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('post_detail', pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'my_app/post_confirm_delete.html', {'post': post})


@login_required
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'my_app/comment_form.html', {'form': form, 'post': post})

@login_required
def comment_update(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk, post_id=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'my_app/comment_form.html', {'form': form})

@login_required
def comment_delete(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk, post_id=post_pk)
    post = comment.post
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', pk=post_pk)
    return render(request, 'my_app/comment_confirm_delete.html', {'comment': comment, 'post': post})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    return render(request, 'my_app/home.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'my_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()
    return render(request, 'my_app/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
