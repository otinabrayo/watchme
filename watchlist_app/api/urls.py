from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>',WatchDetailAV.as_view(), name='movie_details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('detail/', StreamDetailAV.as_view(), name='detail'),
    path('<int:pk>',StreamDetailAV.as_view(), name='stream_details'),
]