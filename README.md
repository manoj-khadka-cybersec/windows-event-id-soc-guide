🛡️ Windows Event ID SOC Guide

Tier-2 SOC Analyst Edition — A practical cheat sheet for monitoring Windows Event Logs efficiently.

“In cybersecurity operations, every Event ID tells a story — understanding them enables faster detection, response, and defense.”

👀 Overview

Windows Event Logs are critical for threat detection and incident investigation. Each Event ID provides a footprint of system activity, from routine logins to potential malicious behavior. This guide:

Highlights key Windows Event IDs relevant to SOC operations.
Provides context on why each ID matters.
Shares practical insights for monitoring, alerting, and investigation.

Fun fact: Stuxnet, the infamous industrial malware, was discovered in part due to unusual Windows Event Logs.

⚡ Key Event ID Categories
👤 Authentication & Logon
Event ID	Description	SOC Insight
4624	Successful logon	Used to monitor normal vs. suspicious logins; unusual times or sources may indicate compromise.
4625	Failed logon	High counts often indicate brute-force attempts.
4648	Logon with explicit credentials	Attackers may use explicit credentials to move laterally.
4672	Special privileges assigned	Sudden admin privileges could indicate privilege escalation.

SOC Tip: Correlating 4625 spikes with 4672 events often reveals ongoing attacks.

🛠 Account Management
Event ID	Description	SOC Insight
4720	User account created	Unexpected account creation requires immediate review.
4722	Account enabled	Dormant accounts enabled unexpectedly may indicate malicious activity.
4723 / 4724	Password change/reset	Could signal credential compromise.
4726 / 4738	Account deleted/modified	May indicate insider threat or attacker activity.

Fun fact: Accounts enabled outside maintenance windows frequently correspond with active attacks.

🛡 Security & Audit
Event ID	Description	SOC Insight
1102	Audit log cleared	Indicates potential log tampering; should trigger investigation.
4719	Audit policy changed	Malicious actors may attempt to disable security tracking.

SOC Insight: A sequence of 1102 + 4720 + 4672 often signals active intrusion.

⚙️ System & Persistence
Event ID	Description	SOC Insight
6005 / 6006 / 6008	Startup, shutdown, unexpected shutdown	Unexpected shutdowns may indicate malware activity or system instability.
7045	New service installed	Often used by malware for persistence; must be monitored.

Tip: New services installed outside maintenance windows are high-priority alerts.

📂 Object Access
Event ID	Description	SOC Insight
4656	Handle requested	Tracks access requests to sensitive files.
4663	Object accessed	Unusual access patterns indicate potential insider or attacker activity.
4660	Object deleted	Often used by attackers to cover tracks.

Fun fact: Object access events function like digital CCTV — every access leaves a trace.

🌐 Network & Authentication
Event ID	Description	SOC Insight
4768 / 4769	Kerberos TGT/service ticket requests	Useful for detecting lateral movement inside domains.
4776	NTLM authentication	Legacy protocol use may indicate attacker activity.

SOC Tip: Sudden spikes in these events can indicate brute-force or Pass-the-Ticket attacks.

💡 Tier-2 Insights
Correlate events: Single Event IDs rarely reveal full attack context.
Monitor timestamps: Activity outside normal hours is suspicious.
Investigate anomalies quickly: Prompt analysis reduces dwell time.
Use SIEM effectively: Combining multiple Event IDs improves detection accuracy.

Fun fact: Attackers often leave obvious patterns. Context-aware monitoring enables Tier-2 analysts to detect stealthy activity before it escalates.

🚀 Additional Resources
Microsoft Windows Security Log Events
SOC Prime Blog

“Event logs are more than data points — they are actionable intelligence. Analyzing them systematically strengthens security operations and incident response.”


If you want, I can also add badges, a Table of Contents, and emojis to make it visually more attractive and GitHub-friendly.

Do you want me to do that next?
