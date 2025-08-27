"""
Gráficos con matplotlib (sin estilos ni colores específicos).
"""
import csv
from pathlib import Path
from typing import Dict, List
import matplotlib.pyplot as plt

def read_csv_dict(path: str) -> Dict[str, List[float]]:
    with open(path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    years = [int(r["year"]) for r in rows]
    series = {"year": years}
    for key in rows[0].keys():
        if key == "year":
            continue
        series[key] = [float(r[key]) for r in rows]
    return series

def line_chart(series: Dict[str, List[float]], out_path: str):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    years = series["year"]
    for tech, values in series.items():
        if tech == "year":
            continue
        plt.figure()
        plt.plot(years, values, marker="o")
        plt.title(f"Tendencia: {tech}")
        plt.xlabel("Año")
        plt.ylabel("Índice (normalizado)")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{out_path}/trend_{tech}.png", dpi=180)
        plt.close()
