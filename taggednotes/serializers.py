from rest_framework.serializers import ModelSerializer, SlugRelatedField, \
                                       PrimaryKeyRelatedField
from .models import Note, Section, Tag


class SectionSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'rank', 'name', 'tag_rank', 'note_rank')
        model = Section


class TagSerializer(ModelSerializer):
    notes = PrimaryKeyRelatedField(many=True, queryset=Note.objects.all(),
                                   required=False)

    class Meta:
        fields = ('id', 'rank', 'label', 'section', 'notes')
        model = Tag


class NoteSerializer(ModelSerializer):
    tag_set = PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), 
                                     required=False)

    class Meta:
        fields = ('id', 'rank', 'title', 'content', 'section', 'tag_set')
        model = Note
