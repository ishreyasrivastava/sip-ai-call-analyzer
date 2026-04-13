import sys
from core.voip_engine import process_voip_capture

# 👇 ADD THIS IMPORT
from ai.ai_engine import generate_ai_analysis


import sys
from core.voip_engine import process_voip_capture
from ai.ai_engine import generate_ai_analysis


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <pcap_file>")
        return

    file_path = sys.argv[1]

    print("\n🔍 Running VoIP Analysis...\n")

    result = process_voip_capture(file_path)
    print(result)

    print("\n🤖 AI Analysis...\n")

    ai_result = generate_ai_analysis(result)
    print(ai_result)


if __name__ == "__main__":
    main()
