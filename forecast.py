"""
Proyección simple por tecnología usando regresión lineal mínima (numpy).
Salida: dict con coeficientes, r2 y pronósticos.
"""
from __future__ import annotations
from typing import Dict, List, Tuple
import numpy as np

def linear_regression(x: List[float], y: List[float]) -> Tuple[float, float, float]:
    """
    Devuelve (pendiente, intercepto, r2).
    """
    X = np.array(x, dtype=float)
    Y = np.array(y, dtype=float)
    A = np.vstack([X, np.ones(len(X))]).T
    m, b = np.linalg.lstsq(A, Y, rcond=None)[0]
    y_pred = m*X + b
    ss_res = np.sum((Y - y_pred)**2)
    ss_tot = np.sum((Y - Y.mean())**2)
    r2 = 1 - ss_res/ss_tot if ss_tot != 0 else 0.0
    return float(m), float(b), float(r2)

def forecast_years(x_years: List[int], y_vals: List[float], years_ahead: int = 3) -> Dict[int, float]:
    m, b, _ = linear_regression(x_years, y_vals)
    last = max(x_years)
    preds = {}
    for y in range(last+1, last+1+years_ahead):
        preds[y] = m*y + b
    return preds
