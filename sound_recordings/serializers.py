from rest_framework import serializers, viewsets

from sound_recordings.models import SoundRecording, SoundRecordingInput


class SoundRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundRecording
        fields = ('id', 'artist', 'title', 'isrc', 'duration', )


class SoundRecordingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SoundRecording.objects.all()
    serializer_class = SoundRecordingSerializer


class SoundRecordingInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundRecordingInput
        fields = ('id', 'artist', 'title', 'isrc', 'duration',
                  'matched_sound_recording', )


class SoundRecordingInputViewSet(viewsets.ModelViewSet):
    queryset = SoundRecordingInput.objects.all()
    serializer_class = SoundRecordingInputSerializer
