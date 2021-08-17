from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers.MessageSerializers import MessageCreateSerializer, MessageViewSerializer
from .models import Message
from Users.models import CustomUser
from rest_framework import permissions, status, viewsets


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def __get_user_from_token(self, token):
        email = Token.objects.get(key=token).user
        user = CustomUser.objects.get(email=email)
        return user

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MessageViewSerializer
        return MessageCreateSerializer

    def create(self, request, *args, **kwargs):
        """
            /api/messages/ with all Message attributes
            users can only send messages if they are the sender otherwise 403
        """
        user = self.__get_user_from_token(request.auth.key)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = request.data
        if user.username != validated_data['sender']:
            response = {
                "detail": "You can not send messages by someone else name"}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        self.perform_create(serializer)
        response = {"detail": "created successfully"}
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
            /api/messages/<pk>/
            response will only be available is the user is the sender/receiver if he is receiver Unread = False
        """
        instance = self.get_object()
        user = self.__get_user_from_token(request.auth.key)
        sender = instance.sender
        receiver = instance.receiver
        if user != receiver and user != sender:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if user == receiver:
            if instance.unread:
                instance.unread = False
                instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
            /api/messages/<pk>/
            users can only delete if he either the sender or receiver
        """
        instance = self.get_object()
        user = self.__get_user_from_token(request.auth.key)
        if user != instance.receiver and user != instance.sender:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        """
            to not respond to http://127.0.0.1:8000/api/messages/
            so when there a lot of messages it can take time
        """
        return Response(status=status.HTTP_403_FORBIDDEN)
