from datetime import date
from allocation import Batch, OrderLine


def test_cannot_allocate_if_available_less_than_required():
    batch = Batch("reference", "test", 2, date.today() )
    orderline = OrderLine("id", "sku", 10)
    

    assert batch.can_allocate(orderline) is False