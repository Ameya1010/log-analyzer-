import sys


def analyze_log(file_path):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "FAIL": 0,
        "EXCEPTION": 0,
        "CRITICAL": 0,
        "TRACEBACK": 0
}
        
    

    with open(file_path, "r") as file:
        for line in file:
            for level in counts:
                if line.startswith(level):
                    counts[level] += 1

    return counts


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    result = analyze_log(log_file)
    print("\n================ LOG ANALYSIS SUMMARY =================")

total_logs = sum(result.values())

for level, count in result.items():
    print(f"{level:<12}:{count}")
    

print("------------------------------------------------------")

if total_logs > 0:
    for level, count in result.items():
        percentage = (count / total_logs) * 100
        print(f"{level:<12}: {percentage:.2f}%")

most_common = max(result, key=result.get)

print(f"\n{most_common} occurred most frequently.")

if result["ERROR"] > 0:
    print("\nBUILD STATUS: FAILED")
    print("Errors detected in log file. Failing build.")
    sys.exit(1)

else:
    print("\nBUILD STATUS : SUCCESS")
    print("No critical errors found. Build successful.")