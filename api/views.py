from rest_framework.response import Response
from rest_framework import generics

from core.models import Images, CustomUser
from .serializers import ImageSerializer, ImageBasicDetailSerializer, ImagePremiumDetailSerializer, ImageEnterpriseDetailSerializer


class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Images.objects.filter(owner=self.request.user)
    

class ImageDetailAPIView(generics.RetrieveAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageBasicDetailSerializer

  
    def get_serializer_class(self):
        user = CustomUser.objects.get(username=self.request.user.username)

        
        if user.account_tiers == 'BASIC':
            return ImageBasicDetailSerializer
        if user.account_tiers == 'PREMIUM':
            return ImagePremiumDetailSerializer
        if user.account_tiers == 'ENTERPRISE':
            return ImageEnterpriseDetailSerializer