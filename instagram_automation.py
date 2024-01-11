import time
from ppadb.client import Client as AdbClient

# Connect to ADB server
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

# Check if any devices are connected
if len(devices) == 0:
    print('No devices')
    quit()

# Select the first connected device
device = devices[0]
print(f'Connected to {device}')

def mute_account(device):
    # Select Mute option
    device.shell('input touchscreen tap 150 2168')
    time.sleep(1.5)

    # Mute posts
    device.shell('input touchscreen tap 970 1447')
    time.sleep(1.5)

    # Mute stories
    device.shell('input touchscreen tap 990 1599')
    time.sleep(1.5)

    # Return to the list
    device.shell('input touchscreen tap 330 876')
    time.sleep(1.5)

# Swipe down to reveal more accounts
device.shell('input touchscreen swipe 122 1695 122 432 5500')
time.sleep(1.5)

# Number of accounts to be processed
following = 1043
# Calculate the number of rounds required
automation_rounds = round(1043 / 9)

# Loop through the rounds
for _ in range(automation_rounds):
    start_number = 450
    # Loop through 9 accounts in each round
    for _ in range(9):
        # Select options for the first account in the list
        device.shell(f'input touchscreen tap 1028 {start_number}')
        time.sleep(1.5)
        mute_account(device)
        start_number += 187  # Increment the start_number by 187 for the next iteration

    # Swipe down to reveal more accounts
    device.shell('input touchscreen swipe 122 2146 122 452 5500')
    time.sleep(0.5)
