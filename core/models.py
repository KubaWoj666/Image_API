from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

from django_advance_thumbnail import AdvanceThumbnailField

import uuid


class CustomUser(AbstractUser):
    ACCOUNT_TIERS = [
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('ENTERPRISE', 'Enterprise')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account_tiers = models.CharField(max_length=10, choices=ACCOUNT_TIERS, default="BASIC")



class Images(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg'])])
    thumbnail_200 = AdvanceThumbnailField(source_field="image", upload_to="thumbnail_200", null=True, blank=True, size=(200, 200))
    thumbnail_400 = AdvanceThumbnailField(source_field="image", upload_to="thumbnail_400", null=True, blank=True, size=(400, 400))

    class Meta:
        verbose_name_plural = "Images"

    def __str__(self) -> str:
        return self.owner.username
    
    
    


