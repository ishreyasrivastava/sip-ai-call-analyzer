import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_analysis(raw_output):
    text = raw_output.lower()

    if "busy" in text or "486" in text:
        return """
❌ Issue: Call could not be completed because the recipient is busy
📍 Cause: SIP server returned a 486 Busy Here response
💡 Fix: Retry the call later or implement call queuing
"""

    if "not found" in text or "404" in text:
        return """
❌ Issue: Destination user not found
📍 Cause: Invalid SIP address or unregistered user
💡 Fix: Verify SIP URI and registration status
"""

    return """
❌ Issue: Unknown VoIP failure
📍 Cause: Unable to determine exact cause
💡 Fix: Check logs and retry with detailed diagnostics
"""
