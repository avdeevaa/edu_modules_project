from rest_framework import generics
from modules.models import Modules
from modules.paginators import ModulesPagination
from modules.serializers import ModuleSerializer


class ModuleCreateAPIview(generics.CreateAPIView):
    """Create an Educational Module"""
    serializer_class = ModuleSerializer


class ModuleListAPIview(generics.ListAPIView):
    """Check all Educational Modules"""
    serializer_class = ModuleSerializer
    queryset = Modules.objects.all()
    pagination_class = ModulesPagination


class ModuleRetrieveAPIview(generics.RetrieveAPIView):
    """ Check one Educational module"""
    serializer_class = ModuleSerializer
    queryset = Modules.objects.all()


class ModuleUpdateAPIview(generics.UpdateAPIView):
    """ Update an Educational module"""
    serializer_class = ModuleSerializer
    queryset = Modules.objects.all()


class ModuleDestroyAPIview(generics.DestroyAPIView):
    """ Delete an Educational module"""
    queryset = Modules.objects.all()

