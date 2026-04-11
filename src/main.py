import sys
from core.voip_engine import process_voip_capture

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <pcap_file>")
        return

    file_path = sys.argv[1]

    print("\n🔍 Running VoIP Analysis...\n")

    result = process_voip_capture(file_path)

    print(result)


if __name__ == "__main__":
    main()
