from rest_framework import serializers, viewsets
from .models import Note, PersonalNote
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'content')

class NoteViewset(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        field = ('title', 'content')

    def create(self, validated_data):
        import pdb; pdb.set_trace()
        

class PersonalNoteViewset(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = PersonalNote.objects.all()