from django.shortcuts import get_object_or_404
from rest_framework import status, generics, viewsets, permissions, renderers
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.decorators import action

from watchlist_app.api.serializers import (WatchListSerializer, StreamPlatformSerializer,
                                           ReviewSerializer)
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer 
    
    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        movie = WatchList.objects.get(pk=pk)
        
        serializer.save(watchlist=movie)
        
class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
     
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class StreamPlatformVS(viewsets.ModelViewSet):
        queryset = StreamPlatform.objects.all()
        serializer_class = StreamPlatformSerializer
        # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        
        # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
        # def highlight(self, request, *args, **kwargs):
        #     snippet = self.get_object()
        #     return Response(snippet.highlighted)

        # def perform_create(self, serializer):
        #     serializer.save(owner=self.request.user)

# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)     
      
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchList = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchList,  context={'request': request})
#         return Response(serializer.data)  
    
#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)     
     
# class StreamPlatformAV(APIView):
                 
#     def get(self, request):
#         platform = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
        
class StreamDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(platform, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        detail = StreamPlatform.objects.get(pk=pk)
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
 
        
class WatchListAV(APIView):
    
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)        

class WatchDetailAV(APIView):
    
    def get(self, request, pk):
        # if request.method == 'GET':
            try:  
                movie = WatchList.objects.get(pk=pk)
            except WatchList.DoesNotExist:
                return Response({'error': 'Not Found'},status=status.HTTP_404_NOT_FOUND)
            
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
        
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
    