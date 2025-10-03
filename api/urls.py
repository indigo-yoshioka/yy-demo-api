from django.contrib import admin
from django.urls import path
from api.views.todo import TodoViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user", TodoViewSet.as_view({"get": "list", "post": "create"})),
]
