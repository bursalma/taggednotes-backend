from rest_framework.routers import SimpleRouter
from django.urls import path

from . import views

router = SimpleRouter()
router.register("note/(?P<section>[^/.]+)", views.NoteSectionViewSet, "notesection")
router.register("section", views.SectionViewSet, "section")
router.register("tag/(?P<section>[^/.]+)", views.TagSectionViewSet, "tagsection")

urlpatterns = [
    path('health/', views.HealthView.as_view(), name="health")
]

urlpatterns += router.urls
