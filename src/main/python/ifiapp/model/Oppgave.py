import datetime

class Oppgave:
    def __init__(self, navn: str, beskrivelse: str, dato: datetime):
        self._navn = navn
        self._beskrivelse = beskrivelse
        self._dato = dato

    def __str__(self) -> str:
        return f"{self.navn}"
