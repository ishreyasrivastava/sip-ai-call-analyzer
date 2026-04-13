# 🚀 AI-Powered SIP Call Failure Analyzer

A production-inspired telecom debugging tool designed to analyze SIP-based call failures and generate structured root cause insights.

---

## 🧠 Overview

Modern communication platforms rely on VoIP (Voice over IP) systems powered by SIP (Session Initiation Protocol). Debugging failed calls involves analyzing signaling data, identifying failure points, and determining root causes.

This project simulates a **real-world telecom support engineer workflow** by:

* Processing SIP-related data
* Detecting call failures
* Generating structured diagnostics (Issue → Cause → Fix)

---

## ⚙️ Features

* 📡 SIP Failure Detection
* 🧩 Modular Architecture (Reader → Parser → Engine → Report)
* 🧾 Structured Debugging Output
* 🖥️ CLI-Based Tool
* 🛠️ Fault-Tolerant Design

---

## 🏗️ Project Architecture

```
src/
├── core/
│   ├── pcap_reader/
│   ├── sip_parser/
│   ├── report/
│   └── voip_engine.py
├── main.py
```

---

## 🚀 Usage

```bash
python src/main.py samples/sample.pcap
```

---

## 📊 Example Output

```
🔍 Running VoIP Analysis...

❌ Issue: Call Busy  
📍 Cause: SIP 486 Busy Here  
💡 Fix: Retry call or check callee availability  
```

---

## 🧰 Tech Stack

* Python
* Networking (SIP concepts)
* CLI tooling

---

## 🔮 Future Enhancements

* AI-based root cause analysis
* Real packet capture integration
* Call quality metrics (jitter, latency)
* Webhook debugging

---

## 👤 Author

Shreya Srivastava
B.Tech | Computer Science

