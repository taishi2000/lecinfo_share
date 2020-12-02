from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, CommentForm
from .models import Subject, Comment, Like
from django.contrib.auth.decorators import  login_required

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_email = form.cleaned_data['email']
            input_password = form.cleaned_data['password1']
            input_username = form.cleaned_data['username']
            new_user = authenticate(email=input_email, password=input_password)
            if new_user is not None:
                login(request, new_user)
                return redirect('app:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'form': form})


def index(request):
    subjects = Subject.objects.order_by('college').order_by('school')
    return render(request, 'app/index.html', {'subjects': subjects })


@login_required
def comment_add(request, subject_pk):
    subject = get_object_or_404(Subject, pk=subject_pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.subject = subject
            comment.user = request.user
            comment.like = Like.objects.create()
            comment.save()
            return redirect('app:subject_detail', subject_pk=subject_pk)
    else:
        form = CommentForm
    return render(request, 'app/comment_add.html', {'form': form, 'subject': subject})

@login_required
def edit(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('app:subject_detail', subject_pk=comment.subject.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'app/edit.html', {'comment': comment, 'form': form})

def subject_detail(request, subject_pk):
    subject = Subject.objects.get(pk=subject_pk)
    comments = subject.comment_set.all().order_by('-like__num')
    done = False
    comment_pk = -1
    for comment in comments:
        if request.user == comment.user:
            done = True
            comment_pk = comment.pk
    context = {
        'subject': subject,
        'comments': comments,
        'done': done,
        'comment_pk': comment_pk,
    }
    return render(request, 'app/subject_detail.html', context)

@login_required
def push_like(request, subject_pk, like_pk, do):
    like = get_object_or_404(Like, pk=like_pk)
    if request.method == "POST":
        if do == "like":
            like.user.add(request.user)
            like.num += 1
            like.save()
        else:
            like.user.remove(request.user)
            like.num -= 1
            like.save()
    return redirect('app:subject_detail', subject_pk=subject_pk)






