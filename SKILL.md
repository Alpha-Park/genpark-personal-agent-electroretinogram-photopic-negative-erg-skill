---
name: genpark-personal-agent-electroretinogram-photopic-negative-erg-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for evaluating electroretinogram photopic negative response (PhNR), retinal ganglion cell health, and ocular strain.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Electroretinogram Photopic Negative Response (PhNR) Skill

A sovereign personal agent capability for assessing inner retina and retinal ganglion cell (RGC) axonal integrity, visual strain, and optic nerve microcirculation via photopic electroretinography.

## Core Capabilities
- **Photopic Negative Response (PhNR)**: Quantifies the slow negative potential originating specifically from retinal ganglion cells.
- **PhNR/b-wave Ratio**: Standardizes ganglion cell output relative to pre-ganglionic bipolar cell amplitude.
- **Retinal Ganglion Score**: 0-100 index measuring ocular resilience against blue-light exhaustion and optic nerve fatigue.
- **Visual Ergonomics**: Actionable guidelines on ambient lighting, screen contrast, and ocular micro-breaks.

## Fast Invocation
```python
from client import ElectroretinogramPhNRClient

client = ElectroretinogramPhNRClient()
res = client.evaluate_phnr(
    b_wave_amplitude_uv=118.0,
    phnr_amplitude_uv=46.5,
    phnr_latency_ms=71.5
)
print("PhNR/b-wave Ratio:", res["phnr_b_wave_ratio"])
print("Retinal Ganglion Score:", res["retinal_ganglion_score"])
```
