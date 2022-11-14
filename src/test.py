import sys
import subprocess

N = int(sys.argv[1])
T = [0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48]

with open("log", "w") as out:
    for t in T:
        cur = subprocess.run(["java", "SSSP", "-a", "0", "-n", f"{N}", "-t", f"{t}"], capture_output=True)
        out.write(cur.stdout.decode('utf-8') + "\n")