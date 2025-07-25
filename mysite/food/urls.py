from . import views
from django.urls import path
urlpatterns = [
   #  food
   path('',views.IndexClassView.as_view(),name = 'index'),
   # food/1
   path('<int:pk>/', views.FoodDetails.as_view(), name = 'detail'),
   path('item/', views.item, name = 'item'),
   # add
   path('add/', views.create_item, name='create_item'),
   # edit
   path('update/<int:item_id>/', views.update_item, name='update_item'),
   # delete
   path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
