from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import Note, Section, Tag


class SectionSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'rank', 'name', 'tag_rank', 'note_rank')
        model = Section


class TagSerializer(ModelSerializer):
    notes = SlugRelatedField(many=True, read_only=True, slug_field='id')

    class Meta:
        fields = ('id', 'rank', 'label', 'section', 'notes')
        model = Tag


class NoteSerializer(ModelSerializer):
    tag_set = SlugRelatedField(many=True, read_only=True, slug_field='id')

    class Meta:
        fields = ('id', 'rank', 'title', 'content', 'section', 'tag_set')
        model = Note


# class UserSerializer(ModelSerializer):
#     class Meta:
#         fields = ('id', 'email', 'password')
#         model = User
