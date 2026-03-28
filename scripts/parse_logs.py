            ltype = (row.get('logon_type') or row.get('LogonType'))
            if ltype:
                logon_types[ltype] += 1

    print("\n=== Event ID Summary ===")
    for eid, count in counts.most_common():
        print(f"{eid}: {count}")

    print("\n=== Accounts Summary ===")
    for acct, count in accounts.most_common():
        print(f"{acct}: {count}")

    print("\n=== Hosts Summary ===")
    for host, count in hosts.most_common():
        print(f"{host}: {count}")

    print("\n=== Logon Types Summary ===")
    for lt, count in logon_types.most_common():
        print(f"{lt}: {count}")

    print(f"\nTotal events processed: {total}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/parse_logs.py data/sample_events.csv")
        sys.exit(1)

    analyze(sys.argv[1])

