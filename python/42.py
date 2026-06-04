import statistics
import os

def process_sales(filename="sales.txt"):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("100\n200\n300\n150\n250")
            
    data = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                try:
                    data.append(float(line.strip()))
                except ValueError:
                    pass
    except FileNotFoundError:
        print("File not found")
        return

    if data:
        mean_val = statistics.mean(data)
        median_val = statistics.median(data)
        print(f"Sales Data Mean: {mean_val}, Median: {median_val}")
    else:
        print("No valid data found")

process_sales()
