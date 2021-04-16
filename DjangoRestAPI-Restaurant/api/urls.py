from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('restaurants/', views.Restaurants.as_view()),
    path('restaurants/<str:restaurant_id>/', views.RestaurantDetail.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/', views.Recipes.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/<str:recipe_id>/', views.RecipeDetail.as_view()),
]
