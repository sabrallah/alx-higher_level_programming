#!/usr/bin/python3
"""
    101-lazy_matrix_mul Mode
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        Multiplies 2 matrix

        Args:
            m_a: first matrixe(2D List)
            m_b: second matrixe(2D List)

        Returns:
            the product of two matrix
    """
    return np.matmul(m_a, m_b)
