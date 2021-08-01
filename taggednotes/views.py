from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Note, Section, Tag
from .serializers import NoteSerializer, SectionSerializer, \
                         TagSerializer


class BaseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user)
        user = self.request.user
        section = self.kwargs.get('section')
        objects = self.model.objects

        if section == 'all':
            return objects.filter(user=user).all()

        return objects.filter(user=user).filter(section=section).all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SectionViewSet(BaseViewSet):
    model = Section
    serializer_class = SectionSerializer

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user).all()


class TagSectionViewSet(BaseViewSet):
    model = Tag
    serializer_class = TagSerializer


class NoteSectionViewSet(BaseViewSet):
    model = Note
    serializer_class = NoteSerializer


class HealthView(APIView):
    def get(self, request):
        return Response({'healthy': True})
