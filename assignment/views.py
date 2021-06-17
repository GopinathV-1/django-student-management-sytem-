from django.shortcuts import render
from .models import Assignment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def home(request):
    if 'tag' in request.GET:
        tag = request.GET['tag']
        posts = Assignment.objects.filter(title__icontains=tag)
    else:
        posts = Assignment.objects.all()
    page = request.GET.get('page', 3)

    paginator = Paginator(posts, 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'users': users})


@login_required
def subject(request):
    try:
        query = request.GET.get('subject')
        posts = Assignment.objects.filter(subject=query)
    except Exception as e:
        query = request.GET.get('staff')
        posts = Assignment.objects.filter(staff=query)
        print(query, posts, e)

    page = request.GET.get('page', 3)

    paginator = Paginator(posts, 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'subject.html', {'users': users})
