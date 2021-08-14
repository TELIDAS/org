from rest_framework import generics, mixins

from npo_icnl.models import ICNL
from npo_icnl.serializers import ICNLSerializer


class ICNLAPIView(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = ICNL.objects.all()
    serializer_class = ICNLSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)

class ICNLDetailAPIView(generics.GenericAPIView,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = ICNL.objects.all()
    serializer_class = ICNLSerializer
    lookup_field = 'id'


    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)