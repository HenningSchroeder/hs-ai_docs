# Übersicht: Vierbeinige Roboter (Quadrupeds)

> Stand: 2026-03-14 | Recherche-Status: Basisversion (Internetaktualisierung verweigert)

---

## Kommerzielle Systeme

### Boston Dynamics – Spot
- **Hersteller:** Boston Dynamics (Hyundai-Tochter), USA
- **Gewicht:** ~32 kg
- **Nutzlast:** 14 kg
- **Geschwindigkeit:** bis 1,6 m/s
- **Akkulaufzeit:** ~90 Minuten
- **Besonderheiten:** Arm-Aufsatz verfügbar, SDK für Entwickler, weit verbreitet in Industrie & Inspektion
- **Anwendungen:** Fabrikinspektion, Bauwesen, Gefahrengebiete, Forschung
- **Preis:** ~75.000 USD

### ANYbotics – ANYmal
- **Hersteller:** ANYbotics, Schweiz (ETH-Spin-off)
- **Modelle:** ANYmal C, ANYmal D
- **Gewicht:** ~50 kg (ANYmal D)
- **Besonderheiten:** IP67-wasserdicht, Gasdetektoren, thermische Kameras, autonome Inspektion
- **Anwendungen:** Öl & Gas, Bergbau, Energieversorgung
- **Website:** anybotics.com

### Unitree Robotics
- **Hersteller:** Unitree, China
- **Modelle:**
  - **Go1** – Einsteiger, ~12 kg, ~2.700 USD
  - **Go2** – Verbesserte Version mit GPT-Integration, ~1.500–3.500 USD
  - **B2** – Industrieversion, ~60 kg Nutzlast
  - **H1** – Humanoid (Übergang zu Bipedal)
- **Besonderheiten:** Preis-Leistungs-Führer, große Community, ROS-kompatibel

### Agility Robotics – Cassie / Digit
- **Hersteller:** Agility Robotics, USA
- **Hinweis:** Cassie ist streng genommen bipedal, aber häufig im Quadruped-Kontext diskutiert

### Ghost Robotics – Vision 60
- **Hersteller:** Ghost Robotics, USA
- **Gewicht:** ~51 kg
- **Nutzlast:** 10 kg
- **Besonderheiten:** Militärischer Einsatz (US Air Force), robust, modular
- **Anwendungen:** Militär, Überwachung, Sicherheit

### Xiaomi – CyberDog 1 & 2
- **Hersteller:** Xiaomi, China
- **CyberDog 1 (2021):** Open-Source, 3,3 kg, ~1.500 USD, NVIDIA Jetson Xavier
- **CyberDog 2 (2023):** 3,5 kg, verbesserte Motorik, günstiger
- **Besonderheiten:** Für Entwickler & Enthusiasten, günstigster Einstieg in leistungsfähige Plattformen

### Spot Micro (Open Source)
- **Typ:** DIY / Open-Source-Community-Projekt
- **Basis:** 3D-gedruckte Teile + Servomotoren
- **Kosten:** ~250–600 USD
- **GitHub:** spotmicro.org / diverse Repos

---

## Forschungsplattformen

### MIT Cheetah (Mini Cheetah)
- **Hersteller:** MIT CSAIL, USA
- **Gewicht:** ~9 kg
- **Besonderheiten:** Kann Saltos ausführen, sehr schnell (bis 9 m/s bei Cheetah 3), Open-Source-Design
- **Publikationen:** Zahlreiche Reinforcement-Learning-Paper

### ETH Zürich – ANYmal (Forschung)
- Grundlage für ANYbotics-Produkte
- Fokus: Lernbasierte Lokomotion, Hindernisse überwinden

### IIT (Istituto Italiano di Tecnologia) – HyQ / HyQReal
- Hydraulischer Antrieb, sehr robust
- Kann ein Auto ziehen

### Stanford Doggo
- Open-Source, günstig (~3.000 USD), 8 Motoren
- Für Forschung & Bildung

---

## Militärische & Sicherheits-Systeme

| Roboter         | Hersteller      | Besonderheit                              |
|-----------------|-----------------|-------------------------------------------|
| Vision 60       | Ghost Robotics  | US Air Force Einsatz, modular             |
| MRZR-Alpha      | Polaris / DARPA | Hybrid Quadruped/Fahrzeug                 |
| Spot (modifiz.) | Boston Dynamics | Bewaffneter Prototyp (kontrovers, 2021)   |

---

## Vergleichstabelle

| Modell         | Gewicht | Preis (ca.)  | Zielgruppe         | Besonderheit              |
|----------------|---------|--------------|---------------------|---------------------------|
| Spot           | 32 kg   | 75.000 USD   | Industrie/Forschung | Ausgereifteste Plattform  |
| ANYmal D       | 50 kg   | >100.000 USD | Industrie           | IP67, autonome Inspektion |
| Vision 60      | 51 kg   | ~150.000 USD | Militär/Sicherheit  | Modular, robust           |
| Unitree Go2    | 15 kg   | ~3.500 USD   | Forschung/Hobby     | Bestes Preis-Leistung     |
| Unitree B2     | 60 kg   | ~20.000 USD  | Industrie           | Hohe Nutzlast             |
| CyberDog 2     | 3,5 kg  | ~1.500 USD   | Enthusiasten        | Open, günstig             |
| MIT Mini Cheetah | 9 kg  | N/A (Forsch.)| Forschung           | Saltos, schnell           |
| Spot Micro     | ~2 kg   | ~400 USD     | DIY/Lernen          | Open-Source               |

---

## Technologie-Trends (bis 2025)

- **Reinforcement Learning:** Zunehmend lernen Quadrupeds komplexe Bewegungen durch RL (ETH, MIT, CMU)
- **Legged locomotion on unstructured terrain:** Treppsteigen, Geröll, Schnee
- **Integration von LLMs:** Sprachsteuerung (Unitree Go2 + ChatGPT, Spot + GPT-4)
- **Manipulation:** Roboterarme auf Quadrupeds (Spot Arm, Unitree Z1)
- **Schwarmrobotik:** Mehrere Quadrupeds koordiniert
- **Energieversorgung:** Längere Akkulaufzeiten durch effizientere Antriebe

---

## Quellen & Links

- Boston Dynamics Spot: https://www.bostondynamics.com/products/spot
- ANYbotics: https://www.anybotics.com
- Unitree Robotics: https://www.unitree.com
- Ghost Robotics: https://www.ghostrobotics.io
- MIT Cheetah: https://biomimetics.mit.edu
- Spot Micro Community: https://spotmicroai.readthedocs.io

---

*Hinweis: Internetaktualisierung war bei Erstellung nicht verfügbar. Preise und Spezifikationen können abweichen. Für aktuelle Daten bitte direkt beim Hersteller anfragen.*
