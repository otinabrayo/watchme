from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import  (ReviewList, ReviewDetail, ReviewCreate, 
                                      WatchListGV, WatchListAV, WatchDetailAV, UserReview, 
                                      StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform') 

urlpatterns = [
    # path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/',WatchDetailAV.as_view(), name='movie_details'),
    path('listy/', WatchListGV.as_view(), name='watch_list'),
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream_list'),
    # path('stream/<int:pk>/', StreamDetailAV.as_view(), name='streamplatform-detail'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
 
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),              
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    path('reviewer/', UserReview.as_view(), name='user_review_detail')
] 