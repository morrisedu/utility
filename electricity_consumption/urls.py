from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    path("", views.index, name = 'index'),
    path('add/new-reading', views.readingInput, name = "add_unit"),
    path("delete/reading/<int:uid>", views.deleteUnit, name = "delete_unit"),
    path('get/readings', views.getReadings, name = "get_readings"),
    path("get/latest-reading", views.getLatestReading, name = "get_latest_reading"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)