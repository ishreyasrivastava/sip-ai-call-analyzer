def parse_sip_messages(capture, file_path):
    sip_messages = []

    # Try pyshark first (real PCAP)
    if capture:
        try:
            for packet in capture:
                if hasattr(packet, 'sip'):
                    sip_messages.append(packet)
        except:
            pass

    # Fallback: raw file read (for demo/testing)
    try:
        with open(file_path, "r") as f:
            content = f.read()
            if "SIP" in content or "sip" in content:
                sip_messages.append(content)
    except:
        pass

    return sip_messages
