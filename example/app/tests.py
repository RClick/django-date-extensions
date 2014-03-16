import unittest

from django_date_extensions.fields import ApproximateDate

from app.models import ApproximateTimeDelta


class PastAndFuture(unittest.TestCase):

    def test_simple(self):
        ApproximateTimeDelta.objects.create(
            date_from=ApproximateDate(2000, 1),
            date_to=ApproximateDate(2000, 2)
        )

        approximate_delta = ApproximateTimeDelta.objects.get(id=1)
        self.assertEqual(approximate_delta.date_from, ApproximateDate(2000, 1),)
        self.assertEqual(approximate_delta.date_to, ApproximateDate(2000, 2),)


if __name__ == "__main__":
    unittest.main()
