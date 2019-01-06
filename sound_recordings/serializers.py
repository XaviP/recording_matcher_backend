from django.db.models import Q

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from sound_recordings.models import SoundRecording, SoundRecordingInput


class SoundRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundRecording
        fields = ('id', 'artist', 'title', 'isrc', 'duration', )


class SoundRecordingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SoundRecording.objects.all()
    serializer_class = SoundRecordingSerializer

    @action(methods=['get'], detail=True)
    def search_match(self, request, pk=None, *args, **kwargs):
        try:
            input = SoundRecordingInput.objects.get(pk=pk)
        except SoundRecordingInput.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        Q_objects = Q()
        if input.title:
            Q_objects |= Q(title__icontains=input.title)
        if input.artist:
            Q_objects |= Q(artist__icontains=input.artist)
        if input.isrc:
            Q_objects |= Q(isrc__icontains=input.isrc)
        if input.duration:
            Q_objects |= Q(duration__icontains=input.duration)

        queryset = SoundRecording.objects.filter(Q_objects)
        serializer = SoundRecordingSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

class SoundRecordingInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundRecordingInput
        fields = ('id', 'artist', 'title', 'isrc', 'duration',
                  'matched_sound_recording', )


class SoundRecordingInputViewSet(viewsets.ModelViewSet):
    queryset = SoundRecordingInput.objects.filter(matched_sound_recording__isnull=True)
    serializer_class = SoundRecordingInputSerializer
