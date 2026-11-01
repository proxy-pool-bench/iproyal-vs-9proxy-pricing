#!/usr/bin/env python3
"""
IPRoyal vs 9Proxy Bandwidth vs Pay-per-IP Comparison Calculator 2026.
Compares bandwidth-metered pricing against session-based pay-per-IP scraping workloads.
"""
import argparse

def calculate_comparison(sessions, gb_per_session, iproyal_gb_rate, nineproxy_ip_rate):
    total_gb = sessions * gb_per_session
    iproyal_total = total_gb * iproyal_gb_rate
    nineproxy_total = sessions * nineproxy_ip_rate
    net_savings = iproyal_total - nineproxy_total
    return {
        "sessions": sessions,
        "total_gb": total_gb,
        "iproyal_total": iproyal_total,
        "nineproxy_total": nineproxy_total,
        "net_savings": net_savings
    }

def main():
    parser = argparse.ArgumentParser(description="IPRoyal vs 9Proxy Scraping Cost Comparison")
    parser.add_argument("--sessions", type=int, default=50, help="Number of distinct scraping sessions (default: 50)")
    parser.add_argument("--gb-per-session", type=float, default=2.0, help="Average data consumed per session in GB (default: 2.0 GB)")
    parser.add_argument("--iproyal-gb-rate", type=float, default=7.0, help="IPRoyal cost per GB in USD (default: $7.00)")
    parser.add_argument("--nineproxy-ip-rate", type=float, default=0.30, help="9Proxy cost per IP session in USD (default: $0.30)")
    args = parser.parse_args()

    res = calculate_comparison(args.sessions, args.gb_per_session, args.iproyal_gb_rate, args.nineproxy_ip_rate)
    print(f"Scraping Workload:       {res['sessions']} sessions ({res['total_gb']:.1f} GB total)")
    print(f"IPRoyal Bandwidth Cost:  ${res['iproyal_total']:.2f}")
    print(f"9Proxy Pay-per-IP Cost:  ${res['nineproxy_total']:.2f}")
    print(f"Net Scraping Savings:    ${res['net_savings']:.2f}")

if __name__ == "__main__":
    main()
