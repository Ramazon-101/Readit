from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializer import ArticleSerializer, ArticleGEtSerializer
from ..models import Article


@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error: Method net allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def article_create(request):
    if request.method == 'POST':
        data = request.data
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Successfully created"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "credentials are not valid"}, status=status.HTTP_400_BAD_REQUEST)
