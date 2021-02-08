from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import Img_to_Test
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
# router.register('books', post)

urlpatterns = [
    path('goldprice/', Img_to_Test.post, name='post'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)