import h5py

try:
    with h5py.File("tsp_serial_results.h5", "r") as f:
        print(list(f.keys()))
except Exception as e:
    print("Error:", e)

