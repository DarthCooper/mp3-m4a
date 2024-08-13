from pydub import AudioSegment
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.mp3'):
            path = root + '/' + str(file)
            print (f"Converting {path}")
            audio = AudioSegment.from_file(path)
            audio.export(path.removesuffix(".mp3") + "_Output.m4a")