from django.urls import path, include
from watchlist_app.api.views import  WatchListAV, WatchDetailAV, StreamPlatformAV, StreamDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('list/<int:pk>/',WatchDetailAV.as_view(), name='movie_details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream_list'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='streamplatform-detail'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    
    # path('stream/<int:pk>/review', StreamDetailAV.as_view(), name='streamplatform-detail'),
    # path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]