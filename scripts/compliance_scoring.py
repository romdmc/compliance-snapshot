#!/usr/bin/env python3
"""CLI pour calculer un score Compliance Snapshot.

Usage:
    python scripts/compliance_scoring.py --region eu --industry saas --customers 150 --incidents 1 --policies full
"""

from dataclasses import dataclass

REGION = {"eu": 0, "us": -5, "multi": -8}
INDUSTRY = {"saas": 0, "fintech": -6, "health": -4, "other": -2}
POLICIES = {"full": 8, "partial": -4, "light": -10}


def score_incidents(count: int) -> int:
    if count <= 0:
        return 6
    if count == 1:
        return 0
    if count <= 3:
        return -8
    return -15


def score_customers(count: int) -> int:
    if count < 50:
        return 6
    if count < 200:
        return 2
    if count < 1000:
        return -4
    return -10


def clamp(value: int) -> int:
    return max(5, min(99, value))


@dataclass
class SnapshotInput:
    region: str
    industry: str
    customers: int
    incidents: int
    policies: str

    def compute(self) -> int:
        base = 80
        base += REGION.get(self.region, 0)
        base += INDUSTRY.get(self.industry, 0)
        base += POLICIES.get(self.policies, 0)
        base += score_incidents(self.incidents)
        base += score_customers(self.customers)
        return clamp(round(base))


STATUS = [
    (85, "Ready pour Series B"),
    (70, "Maturité contrôlée"),
    (55, "Risque moyen, chantiers à lancer"),
    (0, "Zone critique, plan d’urgence requis"),
]


def label(score: int) -> str:
    for threshold, text in STATUS:
        if score >= threshold:
            return text
    return STATUS[-1][1]


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Calcule un score Compliance Snapshot")
    parser.add_argument("--region", choices=REGION.keys(), required=True)
    parser.add_argument("--industry", choices=INDUSTRY.keys(), required=True)
    parser.add_argument("--customers", type=int, required=True)
    parser.add_argument("--incidents", type=int, required=True)
    parser.add_argument("--policies", choices=POLICIES.keys(), required=True)

    args = parser.parse_args()
    snap_input = SnapshotInput(
        region=args.region,
        industry=args.industry,
        customers=args.customers,
        incidents=args.incidents,
        policies=args.policies,
    )
    score = snap_input.compute()
    print(f"Score: {score}")
    print(f"Statut: {label(score)}")


if __name__ == "__main__":
    main()
