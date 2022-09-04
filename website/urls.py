from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name="index"),
    path('price-prediction/', views.Prediction, name="price_prediction"),
    path('showalldata/', views.ShowAllDataView, name="show_all_data"),
    path('showplot/', views.show_plot, name="show_plot")
]
