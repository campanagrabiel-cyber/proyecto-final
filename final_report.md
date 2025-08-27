# Informe Final — El impacto de las nuevas tecnologías en la sociedad: visualización del futuro

**Autor:** Gabriel Campaña  
**Fecha:** 2025-08-26

## 1. Introducción
Este proyecto integra investigación, análisis ético y desarrollo de software para comprender cómo tecnologías emergentes (IA, IoT, Big Data, Blockchain, RA/RV) impactan a la sociedad y cómo podrían evolucionar en el corto plazo.

## 2. Metodología
- Revisión temática por semanas (8 sprints).  
- Desarrollo incremental con programación funcional y visualización de datos.  
- Dataset sintético normalizado (2015–2025) para evidenciar tendencias.  
- Proyección por regresión lineal mínima como línea base (baseline).

## 3. Arquitectura del Software
- **functional.py** — Transformaciones puras, composición, agregaciones.  
- **visualization.py** — Generación de gráficos con matplotlib (una figura por serie).  
- **forecast.py** — Regresión y proyección por tecnología.  
- **main.py** — CLI de orquestación (ETL → gráficos → proyecciones).

## 4. Resultados (síntesis)
- Las cinco tecnologías muestran crecimiento sostenido en 2015–2025.  
- La IA y Big Data presentan mayor aceleración; IoT y AR/VR mantienen crecimiento constante; Blockchain avanza gradual.  
- Proyecciones lineales (baseline) indican continuidad de la tendencia a corto plazo; se recomienda complementar con modelos no lineales cuando haya más datos.

## 5. Impacto Social y Ético (hallazgos)
- **Educación**: personalización del aprendizaje y analítica educativa.  
- **Salud**: diagnóstico asistido y monitoreo remoto (IoT).  
- **Economía**: automatización y productividad; necesidad de reskilling.  
- **Comunicación**: plataformas con algoritmos de recomendación → riesgos de sesgos y burbujas.  
- **Ética**: privacidad, seguridad, transparencia algorítmica y sostenibilidad energética como ejes críticos.

## 6. Conclusiones
- Las nuevas tecnologías transforman procesos y estructuras sociales; la alfabetización digital y la gobernanza ética son esenciales.  
- La visualización y la proyección aportan evidencia para la toma de decisiones.

## 7. Trabajo Futuro
- Incorporar datos reales abiertos (OECD, UNESCO, bancos de indicadores).  
- Añadir modelos de series temporales (ARIMA, Prophet) y dashboards interactivos.  
- Extender a un servidor web (FastAPI/Streamlit) para uso educativo.

## 8. Guía de Ejecución
```bash
python -m src.main --make-charts --forecast --years-ahead 3
```
Las imágenes se generarán en `assets/charts/` y la salida de proyecciones en consola.

---

**Repositorio listo para entrega en GitHub.**
