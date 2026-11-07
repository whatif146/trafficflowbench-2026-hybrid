# TrafficFlowBench 2026 — hybrid submission

This repository documents the **selected primary submission** for the 2026 IEEE
Big Data Cup, Challenge 06, Track 2 (TrafficFlowBench), Kaggle team CAMPUS SUNNY.

## What the submission is

A **public baseline plus a clearly bounded original layer**:

| part | source | public LB contribution |
|---|---|---:|
| Task 1 base (CatBoost residual), Task 2 queue, Task 4 ODME | **public notebook** `anubisyy/catboost-lgbm-nnls-pipeline-top-50-0-86517` (MIT-style public Kaggle code) | 0.86515 |
| **Our layer**: 5-seed U-Net state ensemble blended at 60% ours / 40% public | this repository (`scripts/`) | **+0.00296 → 0.86811** |
| queue / ODME blending | tested and rejected (T4 blend −0.0002…−0.0005) | — |

The public notebook and its assets dataset belong to their author; we reproduce
them in our own Kaggle kernel and only add the state blend. See `ATTRIBUTION.md`
for the exact contribution boundary.

## Final results

| probe | public LB |
|---|---:|
| public 0.86517 pipeline, raw | 0.86515 |
| + our 2-seed U-Net state, 50/50 | 0.86799 |
| + our 2-seed U-Net state, 60% ours | 0.86808 |
| **+ our 5-seed U-Net state, 60% ours** | **0.86811** (selected) |
| + ODME blend | 0.86781 (rejected) |

Primary ref **58077892** (0.86811). Backup ref **58007101** (0.84052, our own
end-to-end pipeline; see the sibling repository `trafficflowbench-2026`).

## Reproduction

```
# 1) the public base: our private Kaggle kernel (inference-only, public assets attached)
kernel/kernel-metadata.json      # kernel id hsuyooyoo/tfb-public-0-86517-reproduction-run

# 2) the state blend (CPU):
python scripts/blend_submissions.py \
    --base  public_base/submission.csv \
    --other our_own/submission.csv \
    --tasks state --w 0.4 \
    --out   submission_hybrid.csv
```

`w=0.4` means 40% public / 60% ours. The resulting file is the selected upload
(validated with the organizer's `submission_key.csv` and sample submission).

## Contents

```
README.md                 this file
ATTRIBUTION.md            public-author attribution and contribution boundary
docs/TrafficFlowBench_Report.pdf   full report (section 10 = final addendum)
docs/FINAL_CHOICE.md      final probe ranking and selection rationale
kernel/kernel-metadata.json        the public-pipeline reproduction kernel
scripts/blend_submissions.py       the blend utility (our code)
scripts/make_unet_candidate.py     Task-1 state candidate builder (our code)
results/lb_progress.csv   final probe ladder
results/components.json   measured score decomposition (our inverse analysis)
```

## License

Our scripts and documentation: MIT. The public notebook code and assets remain
the property of their author; no data or models are redistributed here.
