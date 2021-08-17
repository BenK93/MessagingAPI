from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers.UserSerializers import UserGetSerializer, UserCreateSerializer
from Messages.serializers.MessageSerializers import MessageViewSerializer
from Messages.models import Message
from .models import CustomUser
from rest_framework import permissions, status, viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_permissions(self):
        if self.action == 'registration':
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, ]
        return super(UserViewSet, self).get_permissions()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserGetSerializer

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def registration(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = request.data
        """
        unfortunately self.perform_create(serializer) did not do the job
        """
        user = CustomUser.objects.create(
            username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        response = serializer.data
        get_user = CustomUser.objects.get(username=request.data['username'])
        if not get_user:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        token = Token.objects.get(user=get_user)
        response['token'] = token.key
        return Response(response, status=status.HTTP_201_CREATED)

    @action(detail=True)
    def received_messages(self, request, *args, **kwargs):
        """
            accessable through: /api/users/<pk>/received_messages/  (pk = username)
        """
        user = self.get_object()
        token_of_user = Token.objects.get(user=user).key
        if request.auth.key != token_of_user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        messages = Message.objects.filter(receiver=user)
        serialized_messages = MessageViewSerializer(messages, many=True)
        return Response(serialized_messages.data, status=status.HTTP_200_OK)

    @action(detail=True)
    def sent_messages(self, request, *args, **kwargs):
        """
            accessable through: /api/users/<pk>/sent_messages/  (pk = username)
        """
        user = self.get_object()
        token_of_user = Token.objects.get(user=user).key
        if request.auth.key != token_of_user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        messages = Message.objects.filter(sender=user)
        serialized_messages = MessageViewSerializer(messages, many=True)
        return Response(serialized_messages.data, status=status.HTTP_200_OK)

    @action(detail=True)
    def received_unread_messages(self, request, *args, **kwargs):
        """
            accessable through: /api/users/<pk>/received_unread_messages/  (pk = username)
        """
        user = self.get_object()
        token_of_user = Token.objects.get(user=user).key
        if request.auth.key != token_of_user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        messages = Message.objects.filter(receiver=user, unread=True)
        serialized_messages = MessageViewSerializer(messages, many=True)
        return Response(serialized_messages.data, status=status.HTTP_200_OK)
