from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, StreamDetailSerializer
from watchlist_app.models import WatchList, StreamPlatform, StreamDetail


class StreamPlatformAV(APIView):
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class StreamDetailAV(APIView):
    def get(self, request):
        detail = StreamDetail.objects.all()
        serializer = StreamDetailSerializer(detail, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors)
    

    def delete(self, request, pk):
        detail = StreamDetail.objects.get(pk=pk)
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
        if request.method == 'GET':
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
