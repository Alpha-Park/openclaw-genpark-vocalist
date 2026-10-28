# -*- coding: utf-8 -*-
"""
Example usage of OpenClawGenParkVocalist
Demonstrates pitch tracking, jitter, shimmer, and vocal tone stability analysis.
"""

from client import OpenClawGenParkVocalist

def main():
    vocalist = OpenClawGenParkVocalist(sample_rate_hz=16000)

    res = vocalist.track_pitch_and_stability(duration_sec=1.2)

    print("================================================================")
    print("OpenClaw GenPark Vocalist - Live Acoustic Pitch Analysis")
    print("================================================================\n")
    print(f"Fundamental Pitch (F0): {res['fundamental_frequency_f0_hz']} Hz (Lag: {res['period_lag_samples']} samples)")
    print(f"Autocorrelation Peak  : {res['autocorrelation_peak']}")
    print(f"Vocal Stability Score : {res['vocal_stability_score']} / 100 [{res['vocal_quality_tier']}]")
    print(f"Acoustic Jitter       : {res['jitter_relative_pct']}% (Frequency perturbation)")
    print(f"Acoustic Shimmer      : {res['shimmer_relative_pct']}% (Amplitude perturbation)")
    print(f"Diagnostic Verdict    : {res['diagnostic_verdict']}\n")

if __name__ == "__main__":
    main()
