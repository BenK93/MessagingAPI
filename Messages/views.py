from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers.MessageSerializers import MessageCreateSerializer
from .models import Message
from Users.models import CustomUser
from rest_framework import permissions, status, viewsets


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    # serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def __get_user_from_token(self, token):
        email = Token.objects.get(key=token).user
        user = CustomUser.objects.get(email=email)
        return user

    def get_serializer_class(self):
        if self.action == 'create':
            return MessageCreateSerializer
        elif self.action == 'retrieve':
            return MessageCreateSerializer
        return MessageCreateSerializer

    def create(self, request, *args, **kwargs):
        user = self.__get_user_from_token(request.auth.key)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(user.username)
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass
