import numpy as np

def test_numpy_works():
    assert np.dot(np.eye(2), np.ones(2)).sum() == 2.0