from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    # def __init__(self, data, **kwargs):
    #     content = JSONRenderer().render(data)
    #     kwargs['content_type'] = 'application/json'
    #     super(JSONResponse, self).__init__(content, **kwargs)

    @api_view(['GET','POST'])
    def snippet_list(request,format=None):
        """
        列出所有的code snippet，或创建一个新的snippet。
        """
        if request.method == 'GET':
            snippets = Snippet.objects.all()
            serializer = SnippetSerializer(snippets, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

    @api_view(['GET','PUT','DELETE'])
    def snippet_detail(request, pk):
        """
        获取，更新或删除一个 code snippet。
        """
        try:
            print(request)
            print('pk值是:',pk)
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Response(status=404)

        if request.method == 'GET':
            serializer = SnippetSerializer(snippet)
            return Response(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(snippet, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        elif request.method == 'DELETE':
            snippet.delete()
            return Response(status=204)
