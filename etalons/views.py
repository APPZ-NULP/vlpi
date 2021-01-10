from rest_framework import viewsets

from .models import Etalon
from .serializers import EtalonSerializer


class EtalonViewSet(viewsets.ModelViewSet):
    queryset = Etalon.objects.all()
    serializer_class = EtalonSerializer
    lookup_field = "pk"


# {
#     "nodes": [
#         { "key": 0, "text": "Alpha", "color": "lightblue", "loc": "0 0" },
#         { "key": 1, "text": "Beta", "color": "orange", "loc": "150 0" },
#         { "key": 2, "text": "Gamma", "color": "lightgreen", "loc": "0 150" },
#         { "key": 3, "text": "Delta", "color": "pink", "loc": "150 150" }
#     ],
#     "links": [
#         { "key": -1, "from": 0, "to": 1 },
#         { "key": -2, "from": 0, "to": 2 },
#         { "key": -3, "from": 1, "to": 1 },
#         { "key": -4, "from": 2, "to": 3 },
#         { "key": -5, "from": 3, "to": 0 }
#     ]
# }
