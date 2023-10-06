from rest_framework.response import Response
from rest_framework import generics

from core.models import Images, Thumbnail
from .serializers import ImageSerializer, BasicSerializer, PremiumSerializer, EnterpriseSerializer



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

        try:
            thumbnail = Thumbnail.objects.get(image=image_id) 
            if account_tiers.name == "Basic":
                serializer = BasicSerializer(thumbnail)
                return Response(serializer.data)
            
            if account_tiers.name == "Premium":
                serializer = PremiumSerializer(thumbnail)
                return Response(serializer.data)
            
            if account_tiers.name == "Enterprise":
                serializer = EnterpriseSerializer(thumbnail)
                return Response(serializer.data)
            
        except Thumbnail.DoesNotExist:
            return Response({"error": "Thumbnail dose not exist!"}, status=404)
  

    



