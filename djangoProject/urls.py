# djangoProject/urls.py

from django.urls import path
from djangoProject.views.views import (
    BridgeAdministrationListView,
    BridgeAdministrationDetailView,
    bridge_administration_create,
    bridge_administration_update,
    bridge_administration_delete
)

urlpatterns = [
    path('bridge_administrations/', BridgeAdministrationListView.as_view(), name='bridge_administration_list'),
    path('bridge_administrations/<int:pk>/', BridgeAdministrationDetailView.as_view(), name='bridge_administration_detail'),
    path('bridge_administrations/new/', bridge_administration_create, name='bridge_administration_create'),
    path('bridge_administrations/<int:pk>/edit/', bridge_administration_update, name='bridge_administration_update'),
    path('bridge_administrations/<int:pk>/delete/', bridge_administration_delete, name='bridge_administration_delete'),
]
