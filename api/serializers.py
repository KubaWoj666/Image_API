from rest_framework import serializers
from core.models import Images, Thumbnail
from django.core.validators import FileExtensionValidator


class BasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ["thumbnail_200"]

class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ["thumbnail_200", "thumbnail_400"]

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ["image", "thumbnail_200", "thumbnail_400"]


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg'])])
    thumbnail_url = serializers.HyperlinkedIdentityField(view_name="detail-view", lookup_field="pk")
    class Meta:
        model = Images
        fields = ["pk", "image", "thumbnail_url"]