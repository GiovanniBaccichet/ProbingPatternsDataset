import os
import hashlib
import random
from scapy.all import rdpcap, wrpcap
from scapy.layers.dot11 import Dot11, Dot11Elt

# Path to the Captures folder
captures_folder = "PCAP_original"

# Path to the Output folder
output_folder = "PCAP"

# Check if the output folder exists, and if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create a function to anonymize and save a PCAP file
def anonymize_and_save_pcap(input_file, output_file):
    try:
        # Read the PCAP file using Scapy
        packets = rdpcap(input_file)

        # Dictionary to store the mapping of original MAC addresses to generated random MAC addresses
        mac_address_mapping = {}

        # Anonymize MAC addresses and SSIDs
        for packet in packets:
            if Dot11 in packet and hasattr(packet[Dot11], 'addr2'):
                original_mac_address = packet[Dot11].addr2

                # Use the mapping to ensure consistent random MAC addresses for equal original MAC addresses
                if original_mac_address not in mac_address_mapping:
                    mac_address_mapping[original_mac_address] = generate_random_mac()

                packet[Dot11].addr2 = mac_address_mapping[original_mac_address]

            dot11_elt = packet.getlayer(Dot11Elt, ID=0)
            if dot11_elt and hasattr(dot11_elt, 'info'):
                ssid = dot11_elt.info.decode('UTF-8')
                if len(ssid) > 0:
                    dot11_elt.info = hashlib.sha256(ssid.encode('UTF-8')).hexdigest()[:len(ssid)]

        # Save the modified packets to a new PCAP file
        wrpcap(output_file, packets)

        print(f"Anonymized and saved to {output_file}")

    except Exception as e:
        print(f"Error processing {input_file}: {str(e)}")

# Function to generate a random MAC address
def generate_random_mac():
    return ':'.join([format(random.randint(0, 255), '02X') for _ in range(6)])

# Anonymize and save each PCAP file in the Captures folder
for filename in os.listdir(captures_folder):
    if filename.endswith(".pcap"):
        label = os.path.splitext(filename)[0]
        input_file = os.path.join(captures_folder, filename)
        output_file = os.path.join(output_folder, f"{label}_anonymized.pcap")

        anonymize_and_save_pcap(input_file, output_file)
