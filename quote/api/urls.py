from rest_framework.urls import path

from quote.api.views import QuoteListCreateAPIView, QuoteDetailAPIView


urlpatterns = [
    path('quotes/', QuoteListCreateAPIView.as_view(), name='quote-list'),
    path('quotes/<int:pk>/', QuoteDetailAPIView.as_view(), name='quote-detail'),
]