from django.contrib import admin
from sound_recordings.models import SoundRecording, SoundRecordingInput

class SoundRecordingAdmin(admin.ModelAdmin):
    pass
admin.site.register(SoundRecording, SoundRecordingAdmin)

class SoundRecordingInputAdmin(admin.ModelAdmin):
    pass
admin.site.register(SoundRecordingInput, SoundRecordingInputAdmin)
