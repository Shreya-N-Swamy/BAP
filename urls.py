from django.conf.urls import url
from django.urls import path
from .views import HomePageView, PublisherList, PublisherDetail, AuthorList, AuthorDetail, BookList, BookDetail, \
    shareBookViaEmail, shareAuthorViaEmail, sharePublisherViaEmail, sendAuthorMail, sendPublisherMail

app_name = 'BAP'
urlpatterns = (
    path('', HomePageView.as_view(), name='home'),
    path('publishers/', PublisherList.as_view(), name='publishers'),
    path('publishers/<int:pk>/', PublisherDetail.as_view(), name='PublisherDetail'),

    path('authors/', AuthorList.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='AuthorDetail'),

    path('books/', BookList.as_view(), name='books'),
    path('books/<int:pk>/', BookDetail.as_view(), name='BookDetail'),

    # email_share view as a function
    url(r'^(?P<book_id>\d+)/share/$',
        shareBookViaEmail, name='shareBookViaEmail'),
    url(r'^(?P<publisher_id>\d+)/share/$',
        sharePublisherViaEmail, name='sharePublisherViaEmail'),
    url(r'^(?P<author_id>\d+)/share/$',
        shareAuthorViaEmail, name='shareAuthorViaEmail'),

    url(r'^(?P<author_id>\d+)/sendmail/$',
        sendAuthorMail, name='sendAuthorMail'),
    url(r'^(?P<publisher_id>\d+)/sendmail/$',
        sendPublisherMail, name='sendPublisherMail'),
)
