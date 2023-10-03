import numpy as np
import pyaudio
from Nota import Nota


def generate_tone(frequency, duration, volume=1.0, sample_rate=44100):
    # Calcula o número de frames necessários para a duração especificada
    num_frames = int(sample_rate * duration)

    # Calcula o período da forma de onda
    T = int(sample_rate / frequency)

    # Cria uma forma de onda senoidal com a frequência desejada
    waveform = (volume * np.sin(2 * np.pi * frequency * np.arange(num_frames) / sample_rate)).astype(np.float32)

    return waveform


def play_tone(sound, sample_rate=44100):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # Reproduz a forma de onda
    stream.write(sound.tobytes())

    # Encerra a reprodução
    stream.stop_stream()
    stream.close()
    p.terminate()


duration = 20.0  # Duração em segundos
volume = 0.5  # Volume (de 0.0 a 1.0)
e_major = Nota(82.41, duration)  # Não toca
a = Nota(110.00, duration)  # Não toca
d = Nota(146.84, duration)
g = Nota(196.00, duration)
b = Nota(246.94, duration)
e_minor = Nota(329.63, duration)

# Gera a forma de onda
waveform = generate_tone(e_major.frequency, duration, volume)
# Reproduz o tom
play_tone(waveform)
# * (2 ** (1 / 12)) -> Meio tom acima
# / (2 ** (1 / 12)) -> Meio tom abaixo