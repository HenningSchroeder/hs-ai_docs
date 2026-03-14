# Konzept: Voice Doc Assistant Architektur

**Erstellt:** 2025-03-14  
**Status:** Entwurf  
**Autor:** Voice Doc Assistant (auto-generiert)

---

## Überblick

Sprachgesteuertes Dokumentenmanagement mit Claude Code als Automatisierungs-Layer
und GitHub als einzigem Document Store.

## Kernkomponenten

- **FastAPI Backend** – Async, Pydantic, Claude SDK
- **Claude Code (Headless)** – `claude -p` mit `--session-id` und `--allowedTools`
- **OpenAI Whisper** – Speech-to-Text, DE + EN
- **React PWA** – Cross-Platform, kein App Store
- **GitHub Repo** – Versionierung, kostenlos, überall

## Offene Fragen

- [ ] Redis für Session-Persistenz in Phase 3?
- [ ] Push Notifications für Background Tasks?
- [ ] Offline-Queue für Android ohne Verbindung?

## Nächste Schritte

1. POC: Textbefehl → Claude Code → Git Commit ✅
2. MVP: Audio → Whisper → Claude Code → PWA
3. Beta: Background Tasks + Android Optimierung
