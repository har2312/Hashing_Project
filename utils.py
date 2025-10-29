"""
Utility functions for hashing and key conversion.

Provides:
- string_to_int_polynomial: Convert string to integer via polynomial rolling hash
- hash1: Primary hash function h1(key) = key % m
- hash2: Secondary hash function for double hashing h2(key) = 1 + (key % (m-1))

These helpers centralize hashing logic and produce explainable strings for UI.
"""
from typing import Tuple

P_BASE = 131  # small prime base for polynomial rolling
P_MOD = 10**9 + 7  # mod for intermediate accumulation to avoid overflow


def string_to_int_polynomial(s: str) -> Tuple[int, str]:
    """
    Convert a string to an integer using a simple polynomial rolling hash.

    Returns the numeric value and a human-readable explanation string.
    """
    total = 0
    power = 1
    parts = []
    for i, ch in enumerate(s):
        val = ord(ch)
        contrib = (val * power) % P_MOD
        parts.append(f"ord('{ch}')*{P_BASE}^{i}={val}*{P_BASE}^{i}")
        total = (total + contrib) % P_MOD
        power = (power * P_BASE) % P_MOD
    explanation = f" + ".join(parts) + f" = {total} (mod {P_MOD})"
    return total, explanation


def normalize_key(key) -> Tuple[int, str]:
    """Normalize a key (int or str) to an integer value with explanation."""
    if isinstance(key, int):
        return key, f"int({key})"
    try:
        # Allow numeric strings
        ik = int(key)
        return ik, f"int('{key}')={ik}"
    except Exception:
        val, exp = string_to_int_polynomial(str(key))
        return val, f"poly('{key}') -> {exp}"


def hash1(key_int: int, m: int) -> Tuple[int, str]:
    """Primary hash h1 = key % m with explanation."""
    idx = key_int % m
    return idx, f"h1({key_int}) = {key_int} % {m} = {idx}"


def hash2(key_int: int, m: int) -> Tuple[int, str]:
    """Secondary hash h2 = 1 + (key % (m-1)) with explanation; ensures non-zero."""
    if m <= 1:
        return 1, f"h2({key_int}) = 1 (m<=1)"
    val = 1 + (key_int % (m - 1))
    return val, f"h2({key_int}) = 1 + ({key_int} % {m-1}) = {val}"
