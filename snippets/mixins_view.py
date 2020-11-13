from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

# 混入

class SnippetList(mixins.CreateModelMixin,
                  mixins.ListModelMixin,generics.GenericAPIView):


    queryset = Snippet.objects.all()

    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        print(self)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(self)

        return self.create(request, *args, **kwargs)



class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)