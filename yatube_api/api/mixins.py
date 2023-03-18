from rest_framework import mixins, viewsets


class ListCreateViewset(viewsets.GenericViewSet,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    pass
