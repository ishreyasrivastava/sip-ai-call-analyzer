from core.pcap_reader.reader import load_voip_capture
from core.sip_parser.parser import parse_sip_messages
from core.report.generator import generate_voip_report


def process_voip_capture(file_path):
    # Temporary stable demo output (replace later with real parsing)
    return """
❌ Issue: Call Busy
📍 Cause: SIP 486 Busy Here response detected
💡 Fix: Retry call or check callee availability
"""
