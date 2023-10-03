from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play
import random


def generate_note(frequency, duration, volume=-20, intensity_variation=2):
    sine_wave = Sine(frequency)
    audio_segment = sine_wave.to_audio_segment(duration=duration * 1000)
    audio_segment = audio_segment - volume  # Ajusta o volume (negativo para aumentar)

    # Variação na intensidade da nota
    intensity = random.randint(-intensity_variation, intensity_variation)
    audio_segment = audio_segment + intensity

    # Variação no tempo de início da nota
    start_variation = random.uniform(0, 0.01)
    audio_segment = audio_segment.fade_in(start_variation * 1000)

    return audio_segment


def generate_chord(chord_notes, duration):
    chord_waveform = AudioSegment.silent(duration=duration * 1000)
    for note, frequency in chord_notes.items():
        note_waveform = generate_note(frequency, duration)
        chord_waveform = chord_waveform.overlay(note_waveform)
    return chord_waveform


if __name__ == "__main__":
    # Frequências das notas do acorde de Dó maior (C)
    chord_notes = {
        'C': 261.63,  # Frequência do Dó
        'E': 329.63,  # Frequência do Mi
        'G': 392.00  # Frequência do Sol
    }

    # Duração do acorde em segundos
    duration = 2.0

    # Gera o waveform do acorde
    chord_waveform = generate_chord(chord_notes, duration)

    # Reproduz o acorde
    play(chord_waveform)
