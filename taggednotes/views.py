from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Note, Section, Tag
from .serializers import NoteSerializer, SectionSerializer, \
                         TagSerializer

# from django.contrib.auth.models import User

class BaseViewSet(ModelViewSet):
    def get_queryset(self):
        print(self.request.user)

        section = self.kwargs.get('section')

        if section == 'all':
            return self.model.objects.all()

        return self.model.objects.filter(section=section).all()


class NoteSectionViewSet(BaseViewSet):
    model = Note
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


class SectionViewSet(ModelViewSet):
    model = Section
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.all()


class TagSectionViewSet(BaseViewSet):
    model = Tag
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class HealthView(APIView):
    def get(self, request):
        return Response({'healthy': True})
