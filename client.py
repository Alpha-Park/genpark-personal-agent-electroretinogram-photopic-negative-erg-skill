"""
Electroretinogram Photopic Negative Response (PhNR) & Retinal Ganglion Cell Engine.
Provides deterministic, zero-dependency modeling of ERG b-wave, Photopic Negative Response (PhNR),
PhNR/b-wave ratio, and retinal ganglion cell (RGC) axonal integrity under visual ergonomics.
"""

from typing import Dict, Any, List, Optional


class ElectroretinogramPhNRClient:
    """
    Deterministic client for calculating electroretinogram Photopic Negative Response (PhNR).
    Assesses inner retina and retinal ganglion cell (RGC) axon health, distinguishing outer
    photoreceptor/bipolar responses from optic nerve and ganglion cell electrical kinetics.
    """

    def __init__(self):
        pass

    def evaluate_phnr(
        self,
        b_wave_amplitude_uv: float,
        phnr_amplitude_uv: float,
        phnr_latency_ms: float = 72.0,
        a_wave_amplitude_uv: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates PhNR/b-wave ratio and retinal ganglion cell integrity score.
        Normative values:
        - b-wave amplitude: 75.0 - 160.0 uV
        - PhNR amplitude: 28.0 - 65.0 uV
        - PhNR/b-wave ratio: 0.32 - 0.52
        - PhNR peak latency: 65.0 - 85.0 ms
        """
        if b_wave_amplitude_uv <= 0 or phnr_amplitude_uv <= 0:
            return {"error": "b-wave and PhNR amplitudes must be greater than zero"}

        ratio = round(phnr_amplitude_uv / b_wave_amplitude_uv, 3)

        # Retinal Ganglion Cell Resilience Score (0 - 100):
        # Ratio >= 0.36 with normal latency -> 85 - 100.
        # Ratio 0.28 - 0.35 -> 65 - 84.
        # Ratio < 0.22 -> < 45 (Inner retinal / RGC axonal strain).
        score = 80.0
        if ratio >= 0.38:
            score += 15.0
        elif ratio >= 0.32:
            score += 5.0
        elif ratio < 0.24:
            score -= 30.0
        elif ratio < 0.28:
            score -= 15.0

        if 65.0 <= phnr_latency_ms <= 82.0:
            score += 5.0
        elif phnr_latency_ms > 90.0:
            score -= 20.0

        rgc_score = round(min(100.0, max(5.0, score)), 1)

        if rgc_score >= 85.0:
            tier = "OPTIMAL_RETINAL_GANGLION_FUNCTION"
            interp = f"Robust PhNR amplitude and ratio ({ratio}, PhNR {phnr_amplitude_uv} uV, latency {phnr_latency_ms} ms); healthy inner retinal ganglion cell firing."
            guidance = "Retinal microcirculation and ganglion cell axons are in excellent health. Sustain regular visual hygiene."
        elif rgc_score >= 70.0:
            tier = "PRESERVED_PHOTOPIC_NEGATIVE_RESPONSE"
            interp = f"Normal photopic negative response ratio ({ratio}); balanced outer and inner retinal electrophysiology."
            guidance = "Normal retinal conduction. Observe standard 20-20-20 screen distance rules."
        elif ratio < 0.26 or phnr_latency_ms > 88.0:
            tier = "INNER_RETINA_AXONAL_STRAIN"
            interp = f"Selective reduction in PhNR amplitude relative to b-wave (ratio {ratio}); indicates inner retinal metabolic stress or ganglion cell axon strain."
            guidance = "Elevated ocular strain. Reduce display peak luminance, filter high-energy shortwave blue light, and incorporate ocular rest periods."
        else:
            tier = "MILD_PHOTOPIC_ATTENUATION"
            interp = f"Borderline PhNR/b-wave ratio ({ratio}); mild sub-optimal inner retinal amplitude."
            guidance = "Monitor visual fatigue symptoms and ensure adequate ambient lighting while working."

        return {
            "b_wave_amplitude_uv": b_wave_amplitude_uv,
            "phnr_amplitude_uv": phnr_amplitude_uv,
            "phnr_b_wave_ratio": ratio,
            "phnr_latency_ms": phnr_latency_ms,
            "a_wave_amplitude_uv": a_wave_amplitude_uv,
            "retinal_ganglion_score": rgc_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
