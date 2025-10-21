#This was written by ChatGPT as I do not totally understand h5py and matplotlib just yet.
import h5py
import matplotlib.pyplot as plt
import re

filename = "tsp_serial_results.h5"

try:
    ns = []
    times = []
    distances = []

    with h5py.File(filename, "r") as f:
        for group_name in f.keys():
            group = f[group_name]
            # Extract numeric n value from group name
            n = int(re.findall(r"\d+", group_name)[0])

            # Read datasets
            distance = group["distance"][()][0]
            time_seconds = group["time_seconds"][()][0]
            path = group["path"][()]

            # Store for plotting
            ns.append(n)
            times.append(time_seconds)
            distances.append(distance)

            # Print formatted results
            print(f"\n=== {group_name} ===")
            print(f"Distance: {distance:,.5f}")
            print(f"Path: {list(path)}")
            print(f"Time (seconds): {time_seconds:.6f}")

    # Sort results by n
    ns, times, distances = zip(*sorted(zip(ns, times, distances)))

    # --- Matplotlib Visualization ---
    plt.figure(figsize=(8, 5))
    plt.plot(ns, times, marker="o", linestyle="-")
    plt.title("TSP Serial Solver Performance")
    plt.xlabel("Number of Points (n)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Error:", e)

