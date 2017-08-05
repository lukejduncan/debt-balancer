import unittest

from balancer.balancer import balance


class TestBalancer(unittest.TestCase):
    def test_description_example(self):
        names = ['john', 'luke']
        paid = [100, 50]

        adjustments = balance(names, paid)

        self.assertEquals(1, len(adjustments))
        debtor = adjustments[0][0]
        lendor = adjustments[0][1]
        amount = adjustments[0][2]

        self.assertEquals(debtor, 'luke')
        self.assertEquals(lendor, 'john')
        self.assertEquals(amount, 25)

        self.assertAllPaidSame(names, paid, adjustments)

    def test_no_one_owes_anything(self):
        names = ['john', 'luke']
        paid = [100, 100]

        adjustments = balance(names, paid)
        self.assertEquals(0, len(adjustments))

    def test_one_person_paid_for_everything(self):
        names = ['john', 'luke', 'peter', 'joel']
        paid = [100, 0, 0, 0]

        adjustments = balance(names, paid)
        self.assertEquals(3, len(adjustments))

        # Everyone paying a single person back
        for adj in adjustments:
            self.assertEquals('john', adj[1])
            self.assertEquals(25, adj[2])

        self.assertAllPaidSame(names, paid, adjustments)

    def assertAllPaidSame(self, names, paid, adjustments):
        totals = dict(zip(names, paid))

        for ad in adjustments:
            totals[ad[0]] += ad[2]
            totals[ad[1]] -= ad[2]

        vals = list(totals.values())
        prev_val = vals[0]

        for v in vals:
            self.assertEquals(prev_val, v)
