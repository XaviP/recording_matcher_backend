from django.db import models

class SoundRecording(models.Model):
    artist = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    isrc = models.CharField(max_length=15, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)

class SoundRecordingInput(models.Model):
    artist = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    isrc = models.CharField(max_length=15, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    matched_sound_recording = models.ForeignKey(SoundRecording,
                                                null=True, blank=True,
                                                on_delete=models.SET_NULL)
