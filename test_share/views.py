from django.shortcuts import render, redirect, get_object_or_404
from app.models import Subject, Like
from django.contrib.auth.decorators import login_required
from .forms import TestImageForm
from django.contrib.auth import login, authenticate
from app.forms import CustomUserCreationForm

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
                return redirect('test_share:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'test_share/signup.html', {'form': form})


def index(request):
    subjects = Subject.objects.order_by('college').order_by('school')
    return render(request, 'test_share/index.html', {'subjects': subjects})

def subject_detail(request, subject_pk):
    subject = Subject.objects.get(pk=subject_pk)
    test_images = subject.test_image_set.all().order_by('-like__num')
    done = False
    test_image_pk = -1
    for test_image in test_images:
        if request.user == test_image.user:
            done = True
            test_image_pk = test_image.pk
    context = {
        'subject': subject,
        'test_images': test_images,
        'done': done,
        'test_images_pk': test_image_pk,
    }
    return render(request, 'test_share/subject_detail.html', context)






@login_required
def test_add(request, subject_pk):
    subject = Subject.objects.get(pk=subject_pk)
    if request.method == "POST":
        form = TestImageForm(request.POST, request.FILES)
        if form.is_valid():
            test_image = form.save(commit=False)
            test_image.user = request.user
            test_image.subject = subject
            test_image.like = Like.objects.create()
            test_image.save()
        return redirect('test_share:subject_detail', subject_pk=subject_pk)
    else:
        form = TestImageForm()
    return  render(request, 'test_share/test_add.html', {'form': form, 'subject_pk': subject_pk})


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
    return redirect('test_share:subject_detail', subject_pk=subject_pk)
