from django.db import models
from Users.models import CustomUser


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, null=False, on_delete=models.CASCADE, related_name='senders')
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="receivers")
    message = models.CharField(max_length=1000, null=False)
    subject = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return ("{} {} --> {}").format(self.subject[0:10], self.sender, self.receiver)
