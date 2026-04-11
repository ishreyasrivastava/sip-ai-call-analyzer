def detect_sip_issues(sip_messages):
    for msg in sip_messages:
        text = str(msg)

        if "486" in text:
            return "❌ Issue: Call Busy\n📍 Cause: User unavailable\n💡 Fix: Retry later"

        if "404" in text:
            return "❌ Issue: User Not Found\n📍 Cause: Invalid SIP address\n💡 Fix: Check SIP URI"

    return None


def generate_voip_report(sip_messages):
    if not sip_messages:
        return "❌ Issue: No SIP traffic\n📍 Cause: Empty capture\n💡 Fix: Verify PCAP"

    issue = detect_sip_issues(sip_messages)

    if issue:
        return issue

    return f"""
📊 SIP Analysis Summary

✅ Messages analyzed: {len(sip_messages)}

🔍 Status: No critical errors detected
💡 Suggestion: Run deeper diagnostics (AI layer)
"""
