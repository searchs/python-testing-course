import logging
from pprint import pprint


def test_metrics(client):
    rows = client.metrics()
    # TODO: Remove pprint
    pprint(rows)
    assert len(rows) > 0