from rest_framework.routers import SimpleRouter
from django.urls import path

from . import views

router = SimpleRouter()
# router.register("note", views.NoteViewSet, "note")
router.register("note/(?P<section>[^/.]+)", views.NoteSectionViewSet, "notesection")
router.register("section", views.SectionViewSet, "section")
# router.register("tag", views.TagViewSet, "tag")
router.register("tag/(?P<section>[^/.]+)", views.TagSectionViewSet, "tagsection")
# router.register("user", views.UserViewSet, "user")

urlpatterns = [
    path('health/', views.HealthView.as_view(), name="health")
]

urlpatterns += router.urls
