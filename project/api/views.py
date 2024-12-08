from rest_framework.decorators import api_view
from rest_framework.response import Response
from prject

@api_view(['GET'])
def getRoutes(reqeust):
    routes= [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)


def getRooms(request):
    return Response(rooms)