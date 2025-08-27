# El impacto de las nuevas tecnologías en la sociedad: visualización del futuro

**Autor:** Gabriel Campaña  
**Fecha:** 2025-08-26

## Objetivo
Desarrollar un software integrador que permita visualizar y reflexionar sobre el impacto de las nuevas tecnologías en la sociedad, proyectando escenarios futuros y utilizando contenidos de cuatro unidades (tecnologías emergentes, impacto social, ética y programación/visualización).

## Contenidos clave
- Tecnologías emergentes: IA, IoT, Big Data, RA/RV, Blockchain.
- Impacto social: educación, salud, economía, comunicación.
- Dimensión ética: privacidad, sesgos, sostenibilidad, regulación.
- Programación funcional y visualización de datos aplicada a tendencias tecnológicas.

## Estructura del repositorio
```
.
├── src/
│   ├── main.py               # Punto de entrada (CLI)
│   ├── functional.py         # Utilidades funcionales (map/filter/reduce/puras)
│   ├── visualization.py      # Gráficos (matplotlib)
│   └── forecast.py           # Proyección simple (regresión lineal mínima)
├── data/
│   └── tech_trends.csv       # Dataset de ejemplo con series de tiempo
├── reports/
│   ├── week1.md ... week8.md # Entregables parciales por semana
│   └── final_report.md       # Informe integrador
├── assets/
│   └── charts/               # Se guardarán las imágenes generadas
├── README.md
└── requirements.txt
```

## Requisitos
- Python 3.10+
- Paquetes: `numpy`, `matplotlib`, `pandas` (opcional para visualizar CSV en otros editores).

Instalación opcional:
```bash
pip install -r requirements.txt
```

## Cómo ejecutar
1. **Generar gráficos y pronósticos** con el dataset incluido:
```bash
python -m src.main --make-charts --forecast
```
Esto creará imágenes en `assets/charts/` y mostrará una tabla de proyección por tecnología.

2. **Ayuda del CLI**:
```bash
python -m src.main -h
```

## Programación funcional (en este proyecto)
- Se proveen **funciones puras**, transformaciones con `map`, `filter`, y agregaciones con `reduce` (vía `functools`).
- Se evita el estado compartido y los efectos colaterales en el módulo `functional.py`.
- Se documenta cómo integrar estas funciones al flujo de ETL y visualización.

## Licencia
Uso académico. Libre adaptación con atribución al autor del repositorio.

---

## Cronograma de 8 semanas (resumen)
| Semana | Tema | Entregable |
|--|--|--|
| 1 | Introducción y definición de tecnologías | `reports/week1.md` |
| 2 | Impacto social | `reports/week2.md` |
| 3 | Ética y riesgos | `reports/week3.md` |
| 4 | Programación funcional aplicada | `reports/week4.md` + `src/functional.py` |
| 5 | Visualización de datos | `reports/week5.md` + `src/visualization.py` |
| 6 | IA y futuro laboral (proyección) | `reports/week6.md` + `src/forecast.py` |
| 7 | Integración | `reports/week7.md` + versión integrada del código |
| 8 | Presentación final | `reports/week8.md` + `reports/final_report.md` |
