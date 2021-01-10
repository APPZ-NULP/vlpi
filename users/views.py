from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    @action(detail=False, methods=["post"])
    def sign_in(self, request):
        username = request.data.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
