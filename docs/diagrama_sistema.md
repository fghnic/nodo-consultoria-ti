# Prototipo conceptual del sistema — Nodo Consultoría TI

Caso de estudio del Proyecto Integrador de Dirección de Empresas (IMESP,
Licenciatura en Informática Administrativa).

## La PyME

**Nodo Consultoría TI** — consultoría ficticia de servicios de TI, 8 personas:
1 director general, 2 consultores/desarrolladores de proyectos, 3 técnicos de
soporte, 1 administrativo/facturación, 1 comercial. Ofrece proyectos de
implementación de sistemas y contratos de soporte técnico post-implementación.

## Problemas identificados

1. No miden si cumplen los tiempos de respuesta/resolución prometidos a cada
   cliente (no hay SLA formal medido).
2. No identifican qué clientes consumen más horas de soporte en proporción a
   lo que pagan.
3. No tienen visibilidad clara de la carga de trabajo por técnico.
4. No tienen datos consolidados para decidir entre invertir en soporte o en
   proyectos nuevos.

## Funcionalidades del sistema

| Módulo | Resuelve |
|---|---|
| Tickets y SLA | Registro y alertas de cumplimiento de tiempos prometidos |
| Carga técnica | Distribución de trabajo entre técnicos, segmentada por nivel de soporte |
| Rentabilidad | Horas de soporte consumidas vs. contrato pagado, por cliente |
| Dashboard directivo | Consolidado de KPIs para la dirección |

## Reglas de decisión automatizables

- Alerta de SLA en riesgo (ticket al 80% del tiempo prometido sin resolver).
- Semáforo de rentabilidad de cliente (horas consumidas vs. contrato).
- Alerta de sobrecarga por técnico.

## Datos clave y KPIs

| Funcionalidad | Datos clave | KPI |
|---|---|---|
| Tickets y SLA | Hora de apertura/resolución, prioridad, SLA prometido | % de tickets resueltos dentro de SLA |
| Carga técnica | Técnico, tickets abiertos, nivel de soporte | Tickets/interacciones promedio por técnico, segmentado por nivel |
| Rentabilidad | Horas efectivas por cliente, monto del contrato | Margen (contrato − costo interno de soporte) |
| Dashboard directivo | Consolidado de los anteriores | Tendencia mensual de cumplimiento y rentabilidad |

## Paquete tecnológico propuesto

Dado el tamaño de la empresa (8 personas), se descarta un ERP completo por
sobredimensionado. Se propone:

- Sistema de tickets/helpdesk ligero (ej. osTicket, o desarrollo a medida).
- Dashboard de reportes (ej. Power BI o Google Data Studio) conectado a la
  base de tickets.

## Prototipos funcionales

Como prueba de concepto del "Dashboard directivo", se construyeron tres
prototipos interactivos que implementan las reglas de decisión de esta
sección con datos reales del dataset derivado. Ver `docs/index.html` y
`README.md` (sección "Herramientas interactivas") para el detalle.

