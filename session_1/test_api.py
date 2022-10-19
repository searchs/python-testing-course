import logging


def test_metrics(client):
    rows = client.metrics()
    print(rows)
    print("\n\tOTHERS:\n")
    assert len(rows) > 0