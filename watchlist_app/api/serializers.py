from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, StreamDetail

class WatchListSerializer(serializers.ModelSerializer):
    
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields ="__all__"
        # exclude = ['active', 'name']


class StreamPlatformSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = StreamPlatform
        fields ="__all__" 
        
        
class StreamDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StreamDetail
        fields ="__all__"
         

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Movie name is too short")
#     else:
#         return value

    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Decription should be different ")
#         else:
#             return data     