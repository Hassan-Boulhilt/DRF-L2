from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from quote.api.pagination import SmallSetPagination

from quote.models import Quote
from quote.api.serializers import QuoteSerializer
from quote.api.permissions import IsAdminUserOrReadOnly

class QuoteListCreateAPIView(ListCreateAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    
    
class QuoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination
    
    def perform_create(self, serializer):
        quote_author = self.request.user
        serializer.save(quote_author=quote_author)
        
    
       
    