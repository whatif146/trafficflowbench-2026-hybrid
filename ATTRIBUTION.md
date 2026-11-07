# Attribution and provenance

This work builds on two kinds of material and this file records both, so the
final report and code package can be honest about what is ours and what is public.

## 1. Public pipeline used as a baseline (disclosed)

The primary submission candidate is derived from the public Kaggle notebook

* **CatBoost + LGBM + NNLS Pipeline | Top 50 | 0.86517** by **anubisyy**
  (kernel `anubisyy/catboost-lgbm-nnls-pipeline-top-50-0-86517`)
* Its public assets dataset `anubisyy/trafficflowbench-086517-public-assets`
  (models, priors, and source helpers) is attached under the Kaggle terms.

We reproduced it ourselves in our own private kernel
`hsuyooyoo/tfb-public-0-86517-reproduction-run` (GPU, inference-only, internet
off), and validated the produced `submission.csv` with our own format checker.
Our changes on top of the public output are limited to:

* blending the public Task-1 state with our own LightGBM+U-Net state model
  (50/50 and 70/30 variants), and
* blending the public Task-4 path flows with our NNLS solution (50/50 and 70/30
  variants).

We did **not** modify, retrain or redistribute the public models; the public
pipeline remains the property of its author. The reproduction kernel and the
blend scripts are kept in our package so the exact contribution boundary is
auditable.

## 2. Our own work

Everything else in this repository/package is ours: the Task-1 LightGBM + U-Net
pipeline, the Task-2 long-history queue models and the structural empty-window
fallback analysis, the Task-3 physics proxy and mechanism analysis, the Task-4
NNLS solver, the single-variable A/B protocol, the exact single-task score
inversion, the negative results, the report, and the reproducibility package.

## 3. What the final package will say

In the report/README:

> The primary submission uses the public 0.86517 pipeline as its Task-1/2/4
> base. We reproduced it in our own kernel, validated its output, and layered
> our state/ODME blending on top. The public notebook and assets belong to their
> author; our contribution is the blending, validation and reproducibility layer
> plus the independent Task-1/2/3/4 analyses.

If a competition rule or the organizers require the submission to be entirely our
own work, the fallback is our own best submission (`q_unet2_w05`, public LB
0.84052), which is fully our own pipeline.
