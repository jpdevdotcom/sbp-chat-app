from django.db import models
from conversation.models import Conversation
from django.conf import settings

class Membership(models.Model):
    class MembershipRole(models.TextChoices):
        ADMIN = "admin", "Admin"
        MEMBER = "member", "Member"
    
    id = models.AutoField(primary_key=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="memberships")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="conversation_memberships")
    role = models.CharField(max_length=10, choices=MembershipRole.choices, default=MembershipRole.MEMBER)
    last_read = models.DateTimeField(null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} in {self.conversation.name} as {self.role}"
    
    class Meta:
        db_table = "membership"
        constraints = [
            models.UniqueConstraint(fields=['conversation', 'user'], name='unique_conversation_membership')
        ]