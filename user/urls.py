from django.urls import path
from .views import (
                        ProfileView,
                        ProfileImageView,
                        ProfileDataView,
                    )

urlpatterns = [
    path('/profile', ProfileView.as_view()),
    path('/profileimage', ProfileImageView.as_view()),
    path('/profiledata', ProfileDataView.as_view()),
]