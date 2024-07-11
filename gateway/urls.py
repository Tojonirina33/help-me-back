from django.urls import include, path
from rest_framework.routers import DefaultRouter

from gateway.views import IdentityView

router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path(
        "identity/",
        IdentityView.as_view({"get": "list", "post": "create"}),
        name="identity-list",
    ),
    path(
        "identity/<int:pk>/",
        IdentityView.as_view({"get": "retrieve", "put": "update"}),
        name="identity-detail",
    ),
]
