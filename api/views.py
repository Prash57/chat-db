from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import * 
from base.models import * 

@api_view(['GET'])
def getRoutes(request):
    routes = [
        # {'GET': '/api/'},
    ]
    return Response(routes)