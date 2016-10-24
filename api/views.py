# Create your views here.


from rest_framework import viewsets, permissions

from api.models import Event
from api.serializers import EventsSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
