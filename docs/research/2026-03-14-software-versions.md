# Software Version Overview: Ubuntu, ROS2, Python, Linux Kernel
**Last updated:** 2026-03-14

---

## Ubuntu

| Version | Release Date | EOL | Type |
|---------|-------------|-----|------|
| **22.04 LTS (Jammy Jellyfish)** | Apr 2022 | Apr 2027 | ⭐ LTS |
| 22.10 (Kinetic Kudu) | Oct 2022 | Jul 2023 | Standard |
| 23.04 (Lunar Lobster) | Apr 2023 | Jan 2024 | Standard |
| 23.10 (Mantic Minotaur) | Oct 2023 | Jul 2024 | Standard |
| **24.04 LTS (Noble Numbat)** | Apr 2024 | Apr 2029 | ⭐ LTS |
| 24.10 (Oracular Oriole) | Oct 2024 | Jul 2025 | Standard |
| 25.04 (Plucky Puffin) | Apr 2025 | Jan 2026 | Standard |
| 25.10 (Questing Quetzal) | Oct 2025 | Jul 2026 | Standard |

> ⭐ LTS = Long Term Support (5 years standard, 10 years with ESM)

---

## ROS2 (Robot Operating System 2)

| Distribution | Release Date | EOL | Type |
|-------------|-------------|-----|------|
| Humble Hawksbill | May 2022 | May 2027 | ⭐ LTS |
| Iron Irwini | May 2023 | Nov 2024 | Standard |
| **Jazzy Jalisco** | May 2024 | May 2029 | ⭐ LTS |
| Kilted Kaiju | May 2025 | Nov 2026 | Standard |

> ⭐ LTS releases are supported for 5 years; Standard releases ~18 months.
> LTS ROS2 releases are aligned with Ubuntu LTS releases.

| ROS2 Distro | Target Ubuntu |
|-------------|--------------|
| Humble | 22.04 LTS |
| Iron | 22.04 LTS |
| Jazzy | 24.04 LTS |
| Kilted | 24.04 LTS / 25.04 |

---

## Python

| Version | Release Date | EOL | Type |
|---------|-------------|-----|------|
| 3.10 | Oct 2021 | Oct 2026 | Stable |
| 3.11 | Oct 2022 | Oct 2027 | Stable |
| 3.12 | Oct 2023 | Oct 2028 | Stable |
| 3.13 | Oct 2024 | Oct 2029 | Stable |
| 3.14 | Oct 2025 | Oct 2030 | Stable |

> Python does not have a formal LTS designation — all releases receive ~5 years of security support.
> **Recommended for production:** 3.12 or 3.13 (most widely adopted, full security support).

---

## Linux Kernel

| Version | Release Date | EOL | Type |
|---------|-------------|-----|------|
| **5.15** | Oct 2021 | Dec 2026 | ⭐ LTS |
| 5.16 | Jan 2022 | Mar 2023 | Standard |
| 5.17 | Mar 2022 | Jun 2022 | Standard (EOL) |
| 5.18 | May 2022 | Aug 2022 | Standard (EOL) |
| 5.19 | Jul 2022 | Oct 2022 | Standard (EOL) |
| **6.1** | Dec 2022 | Dec 2026 | ⭐ LTS |
| 6.2 | Feb 2023 | May 2023 | Standard (EOL) |
| 6.3 | Apr 2023 | Jul 2023 | Standard (EOL) |
| 6.4 | Jun 2023 | Sep 2023 | Standard (EOL) |
| **6.6** | Oct 2023 | Dec 2026 | ⭐ LTS |
| 6.7 | Jan 2024 | Apr 2024 | Standard (EOL) |
| 6.8 | Mar 2024 | Jun 2024 | Standard (EOL) |
| 6.9 | May 2024 | Aug 2024 | Standard (EOL) |
| **6.12** | Nov 2024 | Dec 2026 | ⭐ LTS |
| 6.13 | Jan 2025 | Apr 2025 | Standard (EOL) |
| 6.14 | Mar 2025 | Jun 2025 | Standard |
| **6.15** | May 2025 | Nov 2025 | Standard |

> ⭐ LTS kernels receive ~2–6 years of maintenance.
> Ubuntu LTS releases ship with and maintain their own kernel variants based on LTS kernels.

---

## Quick Reference: Recommended Stable Stack (2026)

| Component | Recommended Version | Notes |
|-----------|-------------------|-------|
| Ubuntu | **24.04 LTS** | Active LTS, supported until 2029 |
| ROS2 | **Jazzy Jalisco** | Active LTS, targets Ubuntu 24.04 |
| Python | **3.12 / 3.13** | Full security support, broad ecosystem compatibility |
| Linux Kernel | **6.6 / 6.12** | Active LTS kernels |
