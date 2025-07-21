# CountdownTimer.py
# Simple countdown from 10 to 0 with a 1-second delay between numbers.

import time

def main():
    print("=== Countdown Timer ===")
    for i in range(10, -1, -1):   # 10 → 0 inclusive
        print(i, end="", flush=True)
        if i != 0:
            print("...", end="\n", flush=True)
            time.sleep(1)
        else:
            print("\nTime’s up!")

if __name__ == "__main__":
    main()