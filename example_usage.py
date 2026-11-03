"""
Example Usage: Electroretinogram Photopic Negative Response (PhNR) Evaluation.
Demonstrates non-invasive analysis of retinal ganglion cell integrity and PhNR/b-wave ratio.
"""

from client import ElectroretinogramPhNRClient


def main():
    client = ElectroretinogramPhNRClient()
    print("=== Electroretinogram Photopic Negative Response (PhNR) Demo ===")

    # Test Case 1: Healthy retinal ganglion cell function
    res1 = client.evaluate_phnr(
        b_wave_amplitude_uv=118.0,
        phnr_amplitude_uv=46.5,
        phnr_latency_ms=71.5,
        a_wave_amplitude_uv=38.0
    )
    print("\nTest Case 1: Healthy Retinal Electrophysiology")
    print(f"  b-wave: {res1['b_wave_amplitude_uv']} uV | PhNR: {res1['phnr_amplitude_uv']} uV")
    print(f"  PhNR/b-wave Ratio: {res1['phnr_b_wave_ratio']}")
    print(f"  Latency: {res1['phnr_latency_ms']} ms")
    print(f"  Retinal Ganglion Score: {res1['retinal_ganglion_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Selective PhNR depression / inner retinal axonal strain
    res2 = client.evaluate_phnr(
        b_wave_amplitude_uv=112.0,
        phnr_amplitude_uv=24.0,
        phnr_latency_ms=89.0
    )
    print("\nTest Case 2: Inner Retinal Ganglion Strain")
    print(f"  b-wave: {res2['b_wave_amplitude_uv']} uV | PhNR: {res2['phnr_amplitude_uv']} uV")
    print(f"  PhNR/b-wave Ratio: {res2['phnr_b_wave_ratio']}")
    print(f"  Latency: {res2['phnr_latency_ms']} ms")
    print(f"  Retinal Ganglion Score: {res2['retinal_ganglion_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
