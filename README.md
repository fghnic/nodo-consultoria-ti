# Nodo Consultoría TI — Sistema de información para toma de decisiones

Proyecto Integrador de la materia **Dirección de Empresas** (IMESP,
Licenciatura en Informática Administrativa). Diseño conceptual de un sistema
de información para una PyME ficticia de consultoría de TI, con datos de
soporte técnico reales adaptados al caso.

## Contenido del repositorio

```
data/
  original/   → dataset original, sin modificar
  derived/    → dataset enriquecido con columnas de cliente, contrato y costos
scripts/
  enrich_dataset.py → script que reproduce el dataset derivado
docs/
  diagrama_sistema.md → diseño conceptual del sistema (Fase 2 del proyecto)
```

## Fuente de datos y atribución

Este proyecto usa como base el **Technical Support Dataset**:

> Suvradeep. (2024). *Technical Support Dataset* [Conjunto de datos]. Kaggle.
> https://www.kaggle.com/datasets/suvroo/technical-support-dataset

Publicado bajo **licencia MIT**. El archivo original se conserva sin
modificar en `data/original/`.

## Qué es real, qué es derivado y qué es ficticio

| Dato | Origen |
|---|---|
| Tickets, prioridades, canales, tiempos, SLA, agentes, país | **Real** — dataset original |
| `Horas_Efectivas_Estimadas`, `Costo_Interno_Soporte_EUR`, `Horas_Transcurridas` | **Derivado** — calculado a partir de columnas reales, con supuestos declarados en `scripts/enrich_dataset.py` |
| `Cliente`, `Contrato_Anual_EUR` | **Ficticio** — construido para este ejercicio académico (el dataset original no incluye información de clientes ni contratos) |

Este repositorio es una **obra derivada** bajo los términos de la licencia
MIT del dataset original: se conserva la atribución al autor y se declaran
explícitamente las modificaciones y los datos agregados.

## Licencia

Este repositorio se distribuye bajo licencia MIT (ver `LICENSE`). El dataset
original conserva su propia atribución según se indica arriba.
