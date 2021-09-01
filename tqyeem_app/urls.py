from django.urls import path
from django.views.generic import TemplateView
from .views import signup_view, dashboard_view, product_view

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'),name='home'),
    path('dashboard/',dashboard_view,name="dashboard"),
    path('signup/',signup_view.as_view(),name='signup'),
    # path('product/', addReview_view, name='addReview'),
    path('product/<int:product_id>/',product_view,name="product"),
    
]
