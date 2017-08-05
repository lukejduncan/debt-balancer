import numpy as np
import queue as Q


def balance(names, paid):
    """Given a list of payments, determine the minimal number of
    transfers to have everyone pay an equal number of shares.

    Example Input:
    John $100
    Luke $50

    The expected amount paid is $75, so Luke owes John $25.

    Parameters
    ----------
    names: list[string]
        The names of the people paying into the pot. The indexs
        are aligned with the paid.
    paid : list[float]
        A list of payments made. Each row is a distinct person.
        and each value is the total payments they made.
  """

    result = []

    expected_payment = float(sum(paid)) / max(len(paid), 1)
    delta_payments = np.array(paid) - expected_payment
    delta_payments = list(zip(delta_payments, names))
    debtors = [(x[0]*-1, x[1]) for x in delta_payments if x[0] < 0]
    lenders = [x for x in delta_payments if x[0] > 0]

    debt_q = Q.PriorityQueue()
    lend_q = Q.PriorityQueue()

    for d in debtors:
        debt_q.put(d)

    for l in lenders:
        lend_q.put(l)

    while not lend_q.empty():
        # TODO consider the waiting
        # Check if both queues are the appropriate size
        lent = lend_q.get()
        debt = debt_q.get()

        to_pay = min(debt[0], lent[0])
        print(to_pay)
        lent = (lent[0] - to_pay, lent[1])
        debt = (debt[0] - to_pay, debt[1])

        result.append((debt[1], lent[1], to_pay))

        if lent[0] > 0:
            lend_q.put(lent)

        if debt[0] > 0:
            debt_q.put(debt)

    return result
