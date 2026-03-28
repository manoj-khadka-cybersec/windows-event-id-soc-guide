# 🔐 Windows Event IDs Every SOC Analyst Should Know

[![SOC](https://img.shields.io/badge/Role-SOC-blue?style=for-the-badge)](https://github.com/) 
[![Windows](https://img.shields.io/badge/Platform-Windows-orange?style=for-the-badge)](https://www.microsoft.com/en-us/windows)
[![CyberSecurity](https://img.shields.io/badge/Topic-CyberSecurity-red?style=for-the-badge)](https://github.com/)

---

## 📌 Overview
Windows Event Logs are critical in Security Operations Centers (SOC) for detecting threats, monitoring authentication, and investigating incidents.  
This guide highlights **key Windows Event IDs** every SOC analyst should know.

---

## 🔑 Authentication & Logon Events
| Event ID | Description | Why It Matters |
|--------|------------|---------------|
| 4624 | Successful logon | Track normal and suspicious access |
| 4625 | Failed logon | Detect brute-force attacks |
| 4648 | Logon using explicit credentials | Credential abuse detection |
| 4672 | Special privileges assigned | Admin-level access detection |

---

## 👤 Account Management Events
| Event ID | Description | Why It Matters |
|--------|------------|---------------|
| 4720 | User account created | Detect unauthorized accounts |
| 4722 | Account enabled | Suspicious reactivation |
| 4723 | Password change attempt | Monitor user behavior |
| 4724 | Password reset | Potential takeover |
| 4726 | Account deleted | Cleanup by attacker |
| 4738 | Account modified | Privilege escalation clues |

---

## 🛡️ Security & Audit Events
| Event ID | Description | Why It Matters |
|--------|------------|---------------|
| 1102 | Audit log cleared | 🚨 Evidence tampering |
| 4719 | Audit policy changed | Logging disabled or modified |

---

## ⚙️ System & Persistence Events
| Event ID | Description | Why It Matters |
|--------|------------|---------------|
| 6005 | System startup | Timeline analysis |
| 6006 | System shutdown | Normal/expected behavior |
| 6008 | Unexpected shutdown | Potential crash or attack |
| 7045 | New service installed | 🚨 Malware persistence |

---

## 📂 Object Access Events
| Event ID | Description | Why It Matters |
|--------|------------|---------------|
| 4656 | Handle to object requested | File access attempt |
| 4663 | Object accessed | Sensitive file monitoring |
| 4660 | Object deleted | Data destruction tracking |

---

## 🌐 Network & Authentication Events
| Event ID | Description | Why It Matters |
|--------|------------|---------------|
| 4768 | Kerberos TGT request | Initial authentication |
| 4769 | Service ticket request | Lateral movement detection |
| 4776 | NTLM authentication | Legacy auth monitoring |

---

## 🧠 SOC Insight
Correlate events to detect attacks. Example:
