import subprocess
import sys

# run different number of threads and delta
T = [0, 4, 8, 16]
N = 100000
D = [2000000000, 300000000, 100000000, 100000, 5000]

data = dict()
index = []

print("\nRun extra2 exper\n")
for d in D:
    cur_array = []
    for t in T:
        cur = subprocess.run(["java", "SSSP_extra", "-a", "0", "-n", f"{N}", "-t", f"{t}", "-D", f"{d}"], capture_output=True)
        cur_array.append(float(cur.stdout.decode('utf-8')))
        print(f"node: {N}, delta: {d}, t: {t}, time: {cur.stdout.decode('utf-8')}\n")
    data[d] = cur_array

final = pd.DataFrame(data, index=T).T
final.to_csv("extra2_experiment.csv")