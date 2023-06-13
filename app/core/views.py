"""
Core views for app
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    """Return Successful response."""
    return Response({'healthy': True})
