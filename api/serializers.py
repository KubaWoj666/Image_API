from rest_framework import serializers
from django.core.validators import FileExtensionValidator

from core.models import Images, Thumbnail


class BasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ["thumbnail_200"]
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["image"]

class PremiumSerializer(serializers.ModelSerializer):
    image = ImageSerializer("image", read_only=True)
    
    class Meta:
        model = Thumbnail
        fields = ["thumbnail_200", "thumbnail_400", "image"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        image_data = representation.pop('image')
        representation.update(image_data)
        return representation



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