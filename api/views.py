from rest_framework.response import Response
from rest_framework import generics

from core.models import Images, CustomUser, AccountTiers, Thumbnail
from .serializers import ImageSerializer, BasicSerializer, PremiumSerializer, EnterpriseSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Images.objects.filter(owner=self.request.user)
    

class ImageDetailAPIView(generics.RetrieveAPIView):
    queryset = Thumbnail.objects.all()
    serializer_class = BasicSerializer


    def retrieve(self, request, *args, **kwargs):
        image_id = kwargs.get('pk')  
        user = self.request.user
        account_tiers = user.account_tiers
        print(account_tiers)
        try:
            thumbnail = Thumbnail.objects.get(image_id=image_id) 
            if account_tiers == "Basic":
                print("basic")
                serializer = BasicSerializer(thumbnail)
                return Response(serializer.data)
            if account_tiers == "Premium":
                print(" if premium")
                serializer = PremiumSerializer(thumbnail)
                return Response(serializer.data)
            if account_tiers == "Enterprise":
                serializer = EnterpriseSerializer(thumbnail)
                return Response(serializer.data)
            
        except Thumbnail.DoesNotExist:
            return Response({'error': 'Miniatura o podanym ID nie istnieje.'}, status=404)
  

    



