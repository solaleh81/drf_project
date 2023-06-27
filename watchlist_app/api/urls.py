from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers





# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import (ReviewList, ReviewDetail, ReviewCreate,
                                    WatchListAV, WatchDetailAV, 
                                    # StreamPlatformAV, StreamDetailAV, 
                                    StreamPlatformVS, UserReview,
                                    WatchListGV)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),
    
    
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamDetailAV.as_view(), name="streamplatform-detail"),
    
    # path('review/', ReviewList.as_view(), name='review_detail'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    path('reviews/', UserReview.as_view(), name='user-review-detail'),

]