Event IDs: A SOC Analyst’s Practical Guide (Third Person)
This repository documents Windows Security Event IDs from a SOC analyst’s perspective. How events are interpreted, why they matter, and how to triage by correlation.

What this repository provides

A concise cheat sheet of common Windows Security Event IDs and what they signify.

Practical notes and “fun facts” that SOC analysts know from field work (still suitable for onboarding and training).

A lightweight Python utility to analyze a small sample dataset of Event IDs.

Structure

events_ids.md: A quick reference cheat sheet for common Event IDs.

data/sample_events.csv: A tiny, illustrative dataset for practice.

scripts/parse_logs.py: A minimal analyzer to summarize Event IDs, logon types, and accounts.

LICENSE, CONTRIBUTING.md, .gitignore: project governance and hygiene.


How to use the cheat sheet


Analysts should map Event IDs to a hypothesis (e.g., suspicious logon activity, new service installation, or a cleared audit log).

Correlate Event IDs with host, user, and time to uncover attacker techniques and pivot paths.

Always verify if an Event ID is enabled by policy; a lack of events is itself a signal to confirm telemetry is running.

Fun facts and insights (SOC-analyst flavor)


Fact: The audit log being cleared (Event ID 1102) is a red flag when paired with suspicious logon bursts (4624/4625) and no legitimate maintenance window.

Fact: A cluster of 4625 failures from a single IP or account often hints at credential stuffing or brute force attempts; look for 4624 successes at odd hours to confirm credential reuse.

Fact: 4688 (process creation) with a rare parent process (e.g., not explorer.exe or cmd.exe) or with unusual command lines can indicate living-off-the-land techniques.

Fact: 4648 (explicit credentials) paired with 4624 (logon) can signal Pass-the-Hash or Credential Dumping activity if seen at odd times or on endpoints that don’t typically require explicit creds.

Fact: Special privileges (4672) on a new logon can indicate privilege escalation tracks; correlate with Process creation (4688) and Service activity (4697) for a chain of escalation.

How this repo can be evolved


Replace sample_events.csv with your own exported CSV from a SIEM or EDR tool.

Extend scripts/parse_logs.py to handle EVTX->CSV exports, JSON logs, or Sysmon data.

Add a small Jupyter notebook to visualize event timelines and correlations.

Notes


Event IDs vary by OS version and auditing policy. Always adapt the cheat sheet to your environment.
