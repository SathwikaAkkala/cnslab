# List of suspicious patterns to detect (basic for example)
suspicious_patterns = [
    "DROP TABLE",       # SQL Injection
    "<script>",         # Cross-Site Scripting (XSS)
    "' OR '1'='1",      # SQL Injection
    "sudo rm -rf /",    # Command Injection
    "curl http://"      # Malicious HTTP request
]

# Function to simulate packet analysis
def analyze_packet(packet_data):
    """Analyze packet data for suspicious patterns."""
    for pattern in suspicious_patterns:
        if pattern in packet_data:
            return True, pattern
    return False, None

print("Basic Intrusion Detection System (IDS)")

# Accept dynamic input packets from the user
while True:
    # Simulate packet data input
    packet_data = input("Enter packet data (or type 'exit' to quit): ")
    if packet_data.lower() == "exit":
        break
    
    # Analyze the packet for suspicious content
    is_suspicious, pattern = analyze_packet(packet_data)
    if is_suspicious:
        print(f"Alert! Suspicious pattern detected: '{pattern}' in packet data.")
    else:
        print("Packet is clean.")

print("IDS Simulation Ended.")
