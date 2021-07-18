# from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Note, Section, Tag
from .serializers import NoteSerializer, SectionSerializer, \
                         TagSerializer


class BaseViewSet(ModelViewSet):
    def get_queryset(self):
        section = self.kwargs.get('section')

        if section == 'all':
            return self.model.objects.all()

        return self.model.objects.filter(section=self.kwargs.get('section')).all()


class NoteSectionViewSet(BaseViewSet):
    model = Note
    serializer_class = NoteSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class TagSectionViewSet(BaseViewSet):
    model = Tag
    serializer_class = TagSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]


class HealthView(APIView):
    def get(self, request):
        return Response({'healthy': True})
