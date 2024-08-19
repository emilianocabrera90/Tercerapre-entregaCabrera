from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, PublisherForm
from .models import Author, Book, Publisher
from django.db.models import Q

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_publisher')
    else:
        form = PublisherForm()
    return render(request, 'add_publisher.html', {'form': form})

def search(request):
    query = request.GET.get('q', '')
    results = Author.objects.filter(
        Q(name__icontains=query) |
        Q(birth_date__icontains=query)
    )
    return render(request, 'search.html', {'results': results, 'query': query})
