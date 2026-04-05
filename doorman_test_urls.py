"""Minimal URL config for Doorman tests."""

from django.urls import include, path

urlpatterns = [
    path("auth/", include("shopman.doorman.urls")),
]
