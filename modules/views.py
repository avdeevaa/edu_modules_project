from rest_framework import generics
from modules.models import Modules
from modules.paginators import ModulesPagination
from modules.serializers import ModuleSerializer


class ModuleCreateAPIview(generics.CreateAPIView):
    serializer_class = ModuleSerializer


class ModuleListAPIview(generics.ListAPIView):
    serializer_class = ModuleSerializer
    queryset = Modules.objects.all()
    pagination_class = ModulesPagination


class ModuleRetrieveAPIview(generics.RetrieveAPIView):
    serializer_class = ModuleSerializer
    queryset = Modules.objects.all()


class ModuleUpdateAPIview(generics.UpdateAPIView):
    serializer_class = ModuleSerializer
    queryset = Modules.objects.all()


class ModuleDestroyAPIview(generics.DestroyAPIView):
    queryset = Modules.objects.all()

