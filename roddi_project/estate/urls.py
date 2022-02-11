from django.urls import path
from . import views as estate_views, views
from . views import Dashboard, EstateDetailView

urlpatterns = [
    path('', estate_views.homepage, name="homepage"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('estate/<int:pk>', EstateDetailView.as_view(), name="estate_detail"),
]