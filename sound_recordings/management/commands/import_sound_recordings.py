import os, csv
from django.conf import settings
from django.core.management import BaseCommand

from sound_recordings.models import SoundRecording, SoundRecordingInput


class Command(BaseCommand):
    help = 'Import sound recordings from csv'
    sr_file = 'sound_recordings/management/commands/sound_recordings.csv'
    srir_file = 'sound_recordings/management/commands/sound_recordings_input_report.csv'

    def get_data_from_csv(self, filepath):
        data_from_csv = []
        with open(filepath, newline='') as csvfile:
            filereader = csv.DictReader(csvfile)
            for row in filereader:
                data_from_csv.append(row)
        return data_from_csv

    def handle(self, *args, **options):
        # Sound recordings
        sound_recordings_csv = self.get_data_from_csv(
            filepath = os.path.join(settings.BASE_DIR, self.sr_file))

        imported_sound_recordings = 0
        for r in sound_recordings_csv:
            sr, created = SoundRecording.objects.get_or_create(
                artist=r['artist'].strip() if r['artist'] else None,
                title=r['title'].strip() if r['title'] else None,
                isrc=r['isrc'].strip() if r['isrc'] else None,
                duration=r['duration'].strip() if r['duration'] else None,
            )
            if created:
                imported_sound_recordings += 1

        # Inputs from report
        inputs_csv = self.get_data_from_csv(
            filepath = os.path.join(settings.BASE_DIR, self.srir_file))

        imported_inputs = 0
        for i in inputs_csv:
            sri, created = SoundRecordingInput.objects.get_or_create(
                artist=i['artist'].strip() if i['artist'] else None,
                title=i['title'].strip() if i['title'] else None,
                isrc=i['isrc'].strip() if i['isrc'] else None,
                duration=i['duration'].strip() if i['duration'] else None,
            )
            if created:
                imported_inputs += 1

        self.stdout.write(self.style.SUCCESS('Imported sound recordings: %s\n'
                                             'Imported inputs: %s\n'
                                             % (imported_sound_recordings,
                                             imported_inputs)))
