from django.urls import path

from . import views

urlpatterns = [
    path(r'validate_finite_values',views.validate_finite_values_entity,name="finite_validation"),
    path(r'validate_numeric_entity',views.validate_numeric_entity,name="numeric_validation"),
]