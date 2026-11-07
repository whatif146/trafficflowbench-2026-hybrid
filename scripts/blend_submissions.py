"""Stream-blend two merged submissions (row-aligned by submission_id).

Only the selected tasks are blended; everything else is copied from the base file.
"""
from __future__ import annotations

import argparse
import os

import numpy as np
import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)      # copied for non-blended tasks
    ap.add_argument("--other", required=True)
    ap.add_argument("--tasks", nargs="+", default=["state"])
    ap.add_argument("--w", type=float, default=0.5, help="weight of base")
    ap.add_argument("--out", required=True)
    ap.add_argument("--chunk", type=int, default=1_000_000)
    a = ap.parse_args()
    first = True
    n = 0
    for ca, cb in zip(pd.read_csv(a.base, chunksize=a.chunk),
                      pd.read_csv(a.other, chunksize=a.chunk)):
        assert (ca.submission_id.to_numpy() == cb.submission_id.to_numpy()).all(), "row misalignment"
        assert (ca.task.to_numpy() == cb.task.to_numpy()).all(), "task misalignment"
        for t in a.tasks:
            m = ca.task.to_numpy() == t
            if t == "state":
                ca.loc[m, "speed_kmh"] = (a.w * ca.loc[m, "speed_kmh"].to_numpy()
                                          + (1 - a.w) * cb.loc[m, "speed_kmh"].to_numpy()).round(3)
                ca.loc[m, "flow_vph"] = (a.w * ca.loc[m, "flow_vph"].to_numpy()
                                         + (1 - a.w) * cb.loc[m, "flow_vph"].to_numpy()).round(1)
            elif t == "odme":
                ca.loc[m, "path_flow"] = (a.w * ca.loc[m, "path_flow"].to_numpy()
                                          + (1 - a.w) * cb.loc[m, "path_flow"].to_numpy()).round(6)
            elif t == "queue":
                ca.loc[m, "queue_pred"] = np.round(a.w * ca.loc[m, "queue_pred"].to_numpy()
                                                   + (1 - a.w) * cb.loc[m, "queue_pred"].to_numpy()).astype(int)
        ca.to_csv(a.out, mode="w" if first else "a", header=first, index=False)
        first = False
        n += len(ca)
    print(f"blended {n:,} rows -> {a.out} ({os.path.getsize(a.out)/1e6:.1f} MB)")


if __name__ == "__main__":
    main()
