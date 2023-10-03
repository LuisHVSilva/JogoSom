# 6ª corda (Mais grossa) - Mi (E) abaixo do meio C (frequência aproximada de 82.41 Hz)
# 5ª corda - Lá (A) abaixo do meio C (frequência aproximada de 110.00 Hz)
# 4ª corda - Ré (D) acima do meio C (frequência aproximada de 146.83 Hz)
# 3ª corda - Sol (G) acima do meio C (frequência aproximada de 196.00 Hz)
# 2ª corda - Si (B) acima do meio C (frequência aproximada de 246.94 Hz)
# 1ª corda (Mais fina) - Mi (E) acima do meio C (frequência aproximada de 329.63 Hz)

class Nota:
    # Método especial chamado de construtor, usado para inicializar os atributos do objeto
    def __init__(self, frequency, duration):
        self._frequency = frequency
        self._duration = duration
        self.volume = 0.5

    # Getter
    @property
    def frequency(self):
        return self._frequency

    @property
    def duration(self):
        return self._duration

    # Setter
    @duration.setter
    def duration(self, duration):
        self._duration = duration


