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
  diagrama_sistema.md      → diseño conceptual del sistema (Fase 2 del proyecto)
  decisiones_gerenciales.md → las tres decisiones de alta dirección (Fase 3)
  index.html                → landing page de las herramientas interactivas
  simulador-margenes.html          → simulador de sensibilidad de márgenes
  detector-anomalias-tickets.html  → detector de anomalías en volumen de tickets
  umbral-sla.html                  → umbral de alerta de riesgo de SLA
```

## Herramientas interactivas

Publicadas vía GitHub Pages en **https://fghnic.github.io/nodo-consultoria-ti/**
(o localmente: abre cualquiera de los `.html` de `docs/` directo en el navegador,
no requieren instalación). Cada una pone a prueba, con los datos reales del
dataset, una de las tres decisiones gerenciales del informe:

- **Simulador de márgenes** — ajusta los supuestos de costo (minutos por
  interacción, tarifa interna) y observa si la conclusión sobre el cliente
  menos rentable se sostiene.
- **Detector de anomalías en tickets** — media móvil y z-score sobre el
  volumen diario de tickets de 2023, para detectar picos inusuales por
  cliente antes de que afecten el margen.
- **Umbral de alerta de SLA** — calibra en qué punto del tiempo prometido
  el sistema debería avisar, contra los 1,912 tickets resueltos reales.

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
