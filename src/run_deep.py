import sys
import subprocess
import pandas as pd

T = [0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48]

data = dict()
index = []

print("\nRun deep exper\n")
for d in range(1, 50, 10):
    cur_array = []
    for t in T:
        cur = subprocess.run(["java", "SSSP", "-a", "0", "-n", "24", "-t", f"{t}", "-d", f"{d}"], capture_output=True)
        cur_array.append(cur.stdout.decode('utf-8'))
        print(f"node: {24}, deepth: {d}, t: {t}, time: {cur.stdout.decode('utf-8')}\n")
    data[d] = cur_array

final = pd.DataFrame(data, index=T).T
final.to_csv("experiment_deepth.csv")