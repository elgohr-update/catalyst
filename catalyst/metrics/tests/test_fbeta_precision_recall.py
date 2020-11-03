import pytest  # noqa: F401

import torch

from catalyst.metrics import f1_score, fbeta_score, precision, recall


def test_precision_recall_f_binary_single_class() -> None:
    """Metrics test"""
    # Test precision, recall and F-scores behave with a single positive
    assert 1.0 == precision([1, 1], [1, 1])[1]
    assert 1.0 == recall([1, 1], [1, 1])[1]
    assert 1.0 == f1_score([1, 1], [1, 1])[1]
    assert 1.0 == fbeta_score([1, 1], [1, 1], 0)[1]
    # test with several classes
    assert 3.0 == f1_score([0, 1, 2], [0, 1, 2]).sum().item()
    assert 3.0 == precision([0, 1, 2], [0, 1, 2]).sum().item()
    assert 3.0 == recall([0, 1, 2], [0, 1, 2]).sum().item()

    assert 0.0 == f1_score(torch.arange(10), torch.arange(10)[::-1]).sum()
