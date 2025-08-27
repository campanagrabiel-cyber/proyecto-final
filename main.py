"""
CLI del proyecto integrador.
"""
import argparse, csv
from pathlib import Path
from typing import Dict, List
from .visualization import read_csv_dict, line_chart
from .forecast import forecast_years, linear_regression

ASSETS = Path(__file__).resolve().parents[1] / "assets" / "charts"
DATA = Path(__file__).resolve().parents[1] / "data" / "tech_trends.csv"

def make_charts():
    series = read_csv_dict(str(DATA))
    line_chart(series, str(ASSETS))
    print(f"Gráficos generados en: {ASSETS}")

def make_forecast(years_ahead: int = 3):
    series = read_csv_dict(str(DATA))
    years = series["year"]
    print("Proyección (regresión lineal mínima):")
    for tech, vals in series.items():
        if tech == "year":
            continue
        preds = forecast_years(years, vals, years_ahead=years_ahead)
        print(f"  - {tech}: {preds}")

def main():
    parser = argparse.ArgumentParser(description="Proyecto Integrador - Visualización del futuro tecnológico")
    parser.add_argument("--make-charts", action="store_true", help="Genera gráficos por tecnología")
    parser.add_argument("--forecast", action="store_true", help="Imprime proyecciones simples")
    parser.add_argument("--years-ahead", type=int, default=3, help="Años a proyectar")
    args = parser.parse_args()

    if args.make_charts:
        make_charts()
    if args.forecast:
        make_forecast(args.years_ahead)
    if not args.make_charts and not args.forecast:
        parser.print_help()

if __name__ == "__main__":
    main()
