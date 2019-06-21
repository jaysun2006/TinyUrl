from .serializers import URLSerializer
from .services import create_tiny_url
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateLink(APIView):
    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            url = create_tiny_url(serializer.data.get('url'))
            return Response({"tiny_url": url},
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
