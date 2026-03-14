"""
Snippet: Whisper Transkription
Erstellt: 2025-03-14
Tags: #python #whisper #stt
"""

import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()


async def transcribe(audio_path: str, language: str = "de") -> str:
    """
    Transkribiert eine Audiodatei via OpenAI Whisper.

    Args:
        audio_path: Pfad zur Datei (.webm, .mp3, .wav, .m4a)
        language:   ISO-639-1 Code

    Returns:
        Transkribierter Text
    """
    with open(audio_path, "rb") as f:
        response = await client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language=language,
            response_format="text",
        )
    return str(response).strip()


# Beispiel
if __name__ == "__main__":
    result = asyncio.run(transcribe("recording.webm"))
    print(result)
