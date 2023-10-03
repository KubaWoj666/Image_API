from rest_framework import serializers
from core.models import Images
from django.core.validators import FileExtensionValidator

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg'])])
    thumbnail_url = serializers.HyperlinkedIdentityField(view_name="detail-view", lookup_field="pk")
    class Meta:
        model = Images
        fields = ["pk", "image", "thumbnail_url"]
    

class ImageBasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["thumbnail_200"]

class ImagePremiumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["thumbnail_200", "thumbnail_400"]

class ImageEnterpriseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["image", "thumbnail_200", "thumbnail_400"]