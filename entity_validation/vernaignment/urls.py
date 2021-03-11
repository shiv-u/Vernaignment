from django.urls import path

from . import views

urlpatterns = [
    path(r'validate_finite_values_api',views.validate_finite_values_api,name="finite_validation"),
    path(r'validate_numeric_api',views.validate_numeric_api,name="numeric_validation"),
]