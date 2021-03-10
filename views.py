from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView
from django.core.mail import send_mail
from BAP.forms import EmailForm
from .models import Publisher, Author, Book


class HomePageView(TemplateView):
    template_name = "BAP/home.html"


# --------------------------------------------------------------------------PUBLISHER
class PublisherList(ListView):
    model = Publisher
    template_name = "BAP/publisher/list.html"


class PublisherDetail(DetailView):
    model = Publisher
    template_name = "BAP/publisher/detail.html"


def sharePublisherViaEmail(request, publisher_id):
    publisher = get_object_or_404(Publisher, id=publisher_id, status='posted')
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            publisher_url = request.build_absolute_uri(publisher.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['fromWho'], cd['fromEmail'], publisher.name)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(publisher.name, publisher_url, cd['fromWho'],
                                                                     cd['mailContent'])
            send_mail(subject, message, 'admin@myblog.com', [cd['toEmail']])
            sent = True
    else:
        form = EmailForm()
    return render(request,
                  'BAP/shareViaEmail.html',
                  {'obj': publisher,
                   'form': form,
                   'sent': sent}
                  )


# ---------------------------------------------------------------------------AUTHOR
class AuthorList(ListView):
    model = Author
    template_name = "BAP/author/list.html"


class AuthorDetail(DetailView):
    model = Author
    template_name = "BAP/author/detail.html"


def shareAuthorViaEmail(request, author_id):
    author = get_object_or_404(Author, id=author_id, status='posted')
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            author_url = request.build_absolute_uri(author.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['fromWho'], cd['fromEmail'], author.name)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(author.name, author_url, cd['fromWho'],
                                                                     cd['mailContent'])
            send_mail(subject, message, 'admin@myblog.com', [cd['toEmail']])
            sent = True
    else:
        form = EmailForm()
    return render(request,
                  'BAP/shareViaEmail.html',
                  {'obj': author,
                   'form': form,
                   'sent': sent}
                  )


# -----------------------------------------------------------------------------BOOK
class BookList(ListView):
    model = Book
    template_name = "BAP/book/list.html"


class BookDetail(DetailView):
    model = Book
    template_name = "BAP/book/detail.html"


# ---------------------------------------------------------------
def shareBookViaEmail(request, book_id):
    book = get_object_or_404(Book, id=book_id, status='posted')
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            book_url = request.build_absolute_uri(book.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['fromWho'], cd['fromEmail'], book.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(book.title, book_url, cd['fromWho'],
                                                                     cd['mailContent'])
            send_mail(subject, message, 'admin@myblog.com', [cd['toEmail']])
            sent = True
    else:
        form = EmailForm()
    return render(request,
                  'BAP/shareViaEmail.html',
                  {'obj': book,
                   'form': form,
                   'sent': sent}
                  )


# ------------------------------------------------------------------------------------------------
def sendAuthorMail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            subject = 'Mail from {} ({})'.format(cd['fromWho'], cd['fromEmail'])
            message = '{}'.format(cd['mailContent'])
            send_mail(subject, message, 'admin@myblog.com', [author.email])
            sent = True
    else:
        form = EmailForm()
    return render(request,
                  'BAP/shareViaEmail.html',
                  {'obj': author,
                   'form': form,
                   'sent': sent}
                  )


def sendPublisherMail(request, publisher_id):
    publisher = get_object_or_404(Publisher, id=publisher_id)
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            subject = 'Mail from {} ({})'.format(cd['fromWho'], cd['fromEmail'])
            message = '{}'.format(cd['mailContent'])
            send_mail(subject, message, 'admin@myblog.com', [publisher.email])
            sent = True
    else:
        form = EmailForm()
    return render(request,
                  'BAP/shareViaEmail.html',
                  {'obj': publisher,
                   'form': form,
                   'sent': sent}
                  )


