# Electroretinogram Photopic Negative Response (PhNR) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive analysis of Electroretinogram Photopic Negative Response (PhNR), retinal ganglion cell health, and ocular strain.

```mermaid
flowchart TD
    PhotopicFlash["Photopic Light Stimulus"] --> ERG_Waveform["Full-Field Electroretinogram Recording"]
    ERG_Waveform --> FeatureExtract["Extraction: a-wave, b-wave, PhNR Trough & Latency"]
    FeatureExtract --> RatioCalc["PhNR/b-wave Ratio & Retinal Ganglion Engine"]
    RatioCalc --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **ISCEV Standard Electrophysiology**: Implements clinical electroretinography standards for photopic negative response quantification.
- **Retinal Ganglion Strain Stratification**: Quantitative detection of inner retinal stress before irreversible visual loss.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import ElectroretinogramPhNRClient

client = ElectroretinogramPhNRClient()
result = client.evaluate_phnr(
    b_wave_amplitude_uv=118.0,
    phnr_amplitude_uv=46.5,
    phnr_latency_ms=71.5
)
print("PhNR/b-wave Ratio:", result["phnr_b_wave_ratio"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
