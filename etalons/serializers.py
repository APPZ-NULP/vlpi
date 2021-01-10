from rest_framework import serializers

from .models import Etalon


class EtalonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Etalon
        fields = ["pk", "nodes", "links"]
