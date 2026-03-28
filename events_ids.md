Windows Security Event IDs Cheat Sheet (SOC Analyst Perspective)
Common IDs (with quick notes)


4624: An account was successfully logged on

Look at Logon Type to understand how the login happened (Interactive, Network, Service, etc.)



4625: An account failed to log on

Key for detecting brute force or misconfigurations; correlate with IPs and times



4634: An account was logged off

Often benign; use to build a full login/logout timeline



4647: User-initiated logoff

Can appear after a failed logon; helps confirm session lifecycle



4648: A logon was attempted using explicit credentials

Critical for credential abuse detection



4672: Special privileges assigned to new logon

Must be correlated with the process tree and service activity



4688: A new process has been created

Core for spotting lateral movement or exploitation



4697: A service was installed in the system

Look for unexpected services and their startup types



4698: A scheduled task was created

Often used for persistence; check the program and legitimacy



1102: The audit log was cleared

Strong red flag when paired with suspicious activity or inconsistent timing



4670: Permissions on an object were changed

Could indicate tampering with critical files or ACLs



4720: A user account was created

On endpoint or AD; validate origin and owner



4740: A user account was locked out

Repeated lockouts can indicate brute force or credential stuffing



4768: A Kerberos service ticket (TGT) was requested

Important in lateral movement detection



4769: A Kerberos service ticket request

Related to Kerberos authentication flow; correlate with source host



Tips


Always consider Logon Type alongside Event ID 4624/4625; different Logon Types reveal different attack vectors.

Use a baseline: what is normal on a given host? Sudden spikes in 4688 or 4697 can indicate compromise.

Build a timeline: map event IDs across time to reveal a possible attack chain.

