# Lokale TTS-Lösungen für Python (2026)

> Recherche-Datum: 2026-03-14
> Kontext: Lokale Nutzung mit Python, NVIDIA GPU, Ollama-Integration

---

## Überblick

| TTS System       | Status        | CUDA GPU        | Deutsch       | Qualität        | Geschwindigkeit | Lizenz           | pip-Install            |
|------------------|---------------|-----------------|---------------|-----------------|-----------------|------------------|------------------------|
| Coqui / XTTS v2  | Fork (Idiap)  | Ja              | Ja            | Sehr gut        | Mittel          | Non-Commercial   | `pip install coqui-tts` |
| Piper TTS        | Aktiv         | CPU-optimiert   | Sehr gut      | Gut             | Sehr schnell    | MIT              | `pip install piper-tts` |
| Kokoro TTS       | Aktiv         | Ja              | Eingeschränkt | Sehr gut (EN)   | Schnell         | Apache 2.0       | `pip install kokoro`    |
| StyleTTS2        | Forschung     | Ja              | Nein          | Ausgezeichnet   | Mittel          | MIT              | Manuell                |
| Bark             | Veraltet      | Ja (VRAM-hoch)  | Teilweise     | Expressiv       | Sehr langsam    | MIT              | pip + git              |
| Tortoise TTS     | Veraltet      | Ja              | Nein          | Gut (EN)        | Sehr langsam    | Apache 2.0       | `pip install tortoise-tts` |
| F5-TTS           | Aktiv         | Ja              | Teilweise     | Sehr gut        | Schnell         | CC-BY-NC-4.0     | `pip install f5-tts`    |
| MeloTTS          | Aktiv         | Ja              | Eingeschränkt | Gut             | Schnell         | MIT              | `pip install melotts`   |
| OpenVoice v2     | Aktiv         | Ja              | Ja            | Gut             | Mittel          | MIT              | pip + git              |

---

## Detailbeschreibungen

### 1. Coqui TTS / XTTS v2 (Empfehlung: Deutsch + GPU)

- **Status:** Coqui Inc. aufgelöst Jan 2024. Offizielle Repo archiviert. Community-Fork: `idiap/coqui-ai-tts` (aktiv gewartet)
- **GPU:** Vollständige CUDA-Unterstützung via PyTorch — GPU dringend empfohlen
- **Deutsch:** Ja — XTTS v2 unterstützt 17 Sprachen inkl. Deutsch
- **Besonderheit:** Voice Cloning mit nur 3–6 Sek. Referenzaudio; Streaming-API für LLM-Pipelines
- **Geschwindigkeit:** ~1–3x Echtzeit auf moderner GPU (RTX 3090/4090)
- **Lizenz:** Code MPL-2.0; XTTS v2 Modellgewichte: Non-Commercial

```python
from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")
tts.tts_to_file(text="Hallo Welt!", language="de", file_path="output.wav")
```

```bash
pip install coqui-tts
```

---

### 2. Piper TTS (Empfehlung: Echtzeit / LLM-Pipeline)

- **Status:** Aktiv (Rhasspy / Home Assistant Community)
- **GPU:** CPU-optimiert (auch auf Raspberry Pi), PyTorch-Backend kann CUDA nutzen
- **Deutsch:** Ausgezeichnet — viele deutsche Stimmen (männlich/weiblich)
- **Besonderheit:** Schnellste Option für Echtzeit-LLM-Streaming; weit verbreitet in Home Automation
- **Lizenz:** MIT

```python
import wave
from piper import PiperVoice

voice = PiperVoice.load("de_DE-thorsten-high.onnx")
with wave.open("output.wav", "w") as wav_file:
    voice.synthesize("Hallo Welt!", wav_file)
```

```bash
pip install piper-tts
```

---

### 3. Kokoro TTS (Empfehlung: Englisch Hochqualität)

- **Status:** Aktiv, starke HuggingFace-Community (2025)
- **GPU:** Ja — PyTorch, CUDA
- **Deutsch:** Eingeschränkt (primär Englisch), Multilingual-Erweiterung in Entwicklung
- **Modell:** Kokoro-82M — exzellentes Qualitäts-/Geschwindigkeitsverhältnis
- **Lizenz:** Apache 2.0

```python
from kokoro import KPipeline
pipeline = KPipeline(lang_code='a')
audio, sr = pipeline("Hello World")
```

```bash
pip install kokoro
```

---

### 4. F5-TTS / E2-TTS (Empfehlung: Voice Cloning Neu-Generation)

- **Status:** Aktiv — Flow-Matching-Architektur, neueste Generation
- **GPU:** Ja — PyTorch, CUDA
- **Deutsch:** Mehrsprachige Modelle verfügbar, Deutsch verbessernd
- **Besonderheit:** Zero-Shot Voice Cloning aus kurzem Referenzaudio; konsistenter als autoregressive Modelle
- **Lizenz:** CC-BY-NC-4.0 (Non-Commercial)

```bash
pip install f5-tts
f5-tts_infer-cli --model F5TTS_v1_Base \
  --ref_audio ref.wav --ref_text "Referenztext" \
  --gen_text "Zu sprechender Text"
```

---

### 5. Bark (Suno AI)

- **Status:** Original-Repo weitgehend ungewartet seit mid-2024; Community-Forks vorhanden
- **GPU:** Ja — Multi-GPU, aber VRAM-intensiv (Vollmodell ~12 GB VRAM; `bark-small` reduziert Bedarf)
- **Deutsch:** Ja — aber inkonsistent
- **Besonderheit:** Einzigartig für expressive/emotionale Sprache, Lachen, Geräusche
- **Problem:** Sehr langsam — nicht für Echtzeit-Pipelines geeignet
- **Lizenz:** MIT

```python
from bark import SAMPLE_RATE, generate_audio, preload_models
preload_models()
audio_array = generate_audio("Hallo! [lacht]")
```

---

### 6. StyleTTS2

- **Status:** Forschungsprojekt — keine saubere pip-Installation
- **GPU:** Ja — GPU zwingend erforderlich
- **Deutsch:** Keine offiziellen deutschen Modelle (Fine-Tuning nötig)
- **Besonderheit:** Beste Qualität für Englisch unter Open-Source-TTS
- **Lizenz:** MIT

---

### 7. OpenVoice v2 (MyShell AI)

- **Status:** Aktiv
- **GPU:** Ja
- **Deutsch:** Ja — Cross-Lingual Voice Cloning
- **Besonderheit:** Zero-Shot, sprachübergreifendes Voice Cloning
- **Lizenz:** MIT

---

## Ollama-Integration

Kein TTS-System integriert sich nativ mit Ollama (Stand 2025). Folgende Muster sind etabliert:

### Pattern 1: Ollama + Piper (Echtzeit, vollständig offline)

```python
import ollama
import subprocess

def speak(text: str):
    subprocess.run(
        ["piper", "--model", "de_DE-thorsten-high.onnx", "--output_file", "/tmp/speech.wav"],
        input=text.encode()
    )
    subprocess.run(["aplay", "/tmp/speech.wav"])

stream = ollama.chat(model="llama3", messages=[{"role": "user", "content": "Hallo!"}], stream=True)
sentence = ""
for chunk in stream:
    sentence += chunk["message"]["content"]
    if sentence.rstrip().endswith((".", "!", "?")):
        speak(sentence.strip())
        sentence = ""
```

### Pattern 2: Ollama + XTTS v2 (hohe Qualität + Voice Cloning)

```python
import ollama
from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")

response = ollama.chat(model="llama3", messages=[{"role": "user", "content": "Erkläre Quantencomputing."}])
text = response["message"]["content"]
tts.tts_to_file(text=text, language="de", file_path="output.wav")
```

### Pattern 3: OpenedAI-Speech (OpenAI-kompatibler lokaler Endpunkt)

`matatonic/openedai-speech` — stellt einen `/v1/audio/speech` REST-Endpunkt bereit, der von lokalen TTS-Engines (Piper, Coqui) bedient wird. Drop-in-Ersatz für OpenAI TTS in jeder LLM-Anwendung.

```bash
# Server starten
docker run -p 8000:8000 matatonic/openedai-speech

# Nutzung (OpenAI-kompatibel)
curl http://localhost:8000/v1/audio/speech \
  -d '{"model":"tts-1","input":"Hallo Welt","voice":"alloy"}' \
  --output speech.mp3
```

---

## Empfehlungen nach Anwendungsfall

| Anwendungsfall                             | Empfehlung              | Begründung                                        |
|--------------------------------------------|-------------------------|---------------------------------------------------|
| Deutsch + hohe Qualität + NVIDIA GPU       | **XTTS v2** (Idiap Fork) | Beste deutsche Qualität, Streaming-fähig         |
| Echtzeit LLM-Pipeline (niedrige Latenz)    | **Piper TTS**            | Schnellste Option, MIT, exzellente DE-Stimmen    |
| Voice Cloning aus Referenzaudio            | **F5-TTS** oder XTTS v2 | Zero-Shot, konsistente Qualität                  |
| Englisch-only Hochqualität                 | **Kokoro TTS**           | Apache 2.0, sehr natürlich                       |
| Expressive/emotionale Sprache              | **Bark**                 | Einzigartige Fähigkeiten (Latenz akzeptieren)    |
| Vollständig offline Home Assistant         | **Piper + openedai-speech** | MIT, REST-API, Ollama-kompatibel              |
| Mehrsprachiges Voice Cloning               | **OpenVoice v2**         | MIT, Cross-Lingual                               |

---

## Hinweise

- **Lizenz-Warnung:** XTTS v2 und F5-TTS haben Non-Commercial-Lizenzen für Modellgewichte. Für kommerzielle Nutzung: Piper, Kokoro oder MeloTTS bevorzugen.
- **VRAM-Bedarf:** XTTS v2 ~4–6 GB; Bark (voll) ~12 GB; Piper/Kokoro < 1 GB.
- **Wissensstand:** August 2025 — aktuelle GitHub-Aktivität vor Projekteinsatz prüfen.

---

*Quellen: GitHub-Projektseiten — `idiap/coqui-ai-tts`, `rhasspy/piper`, `hexgrad/kokoro`, `yl4579/StyleTTS2`, `SWivid/F5-TTS`, `suno-ai/bark`, `myshell-ai/MeloTTS`, `myshell-ai/OpenVoice`, `matatonic/openedai-speech`*
