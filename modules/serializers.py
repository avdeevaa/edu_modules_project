from rest_framework import serializers

from modules.models import Modules


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modules
        fields = '__all__'
