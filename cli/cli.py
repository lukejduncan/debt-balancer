import argparse
from balancer.balancer import balance


def main():
    """A command line driver for calculating transactions"""
    parser = argparse.ArgumentParser(
    description="Given a list of people and payments they made returns a list of transactions that ensures everyone shared expenses evenly.")

    parser.add_argument("--names",
                        help="csv list of names of people on trip")

    parser.add_argument("--paid",
                        help="csv list of amounts paid by the people in the corresponding names list")

    args = parser.parse_args()

    names = args.names.split(',')
    paid = args.paid.split(',')
    paid = [float(i) for i in paid]

    adjustments = balance(names, paid)

    if len(adjustments) == 0:
        print("No one owes anyone anything")
        exit(0)

    average = sum(paid) / max(1, len(paid))

    print("Amount everyone should have paid total: %.2f" % (average))

    for adj in adjustments:
        print("%s should pay %s $%.2f" % adj)
