import time
from scopes100 import scopes100
'''
while True:

    try:
        # Your main script logic here
        print("Running script...")
        for k in range(1, 20000000):
            scopes100(k)
        # Simulate an error for demonstration
        raise ValueError("Simulated error!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Restarting script in 5 seconds...")
        time.sleep(5)  # Wait before restarting

'''


for k in range(1, 20000000):
            scopes100(k)

