import pyshark

def load_voip_capture(file_path):
    try:
        capture = pyshark.FileCapture(file_path)
        return capture
    except Exception:
        return None
