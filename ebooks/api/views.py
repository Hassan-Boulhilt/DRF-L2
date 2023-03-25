from rest_framework import generics
from rest_framework import mixins

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer

class EbookListCreateAPIView(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)