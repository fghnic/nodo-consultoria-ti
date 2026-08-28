"""
Enriquecimiento del Technical Support Dataset para el caso de estudio
"Nodo Consultoría TI" (Proyecto Integrador - Dirección de Empresas, IMESP).

Toma el dataset original (data/original/Technical_Support_Dataset.csv,
licencia MIT, autor: Suvradeep / Kaggle) y agrega columnas derivadas y
ficticias para adaptarlo al caso de una consultoría de TI hipotética.

Uso:
    python enrich_dataset.py
"""

import pandas as pd

INPUT_PATH = "../data/original/Technical_Support_Dataset.csv"
OUTPUT_PATH = "../data/derived/nodo_ti_dataset_enriquecido.csv"

# Nombres de clientes ficticios asignados por país (proxy de cuenta/cliente,
# ya que el dataset original no trae un campo explícito de cliente).
CLIENTES = {
    "Germany": "Rheinbrück Industries",
    "Italy": "Lombardia Software Group",
    "Poland": "Wisła Digital Solutions",
    "United Kingdom": "Thames Analytics Ltd",
    "Austria": "Alpen Tech Consulting",
    "Greece": "Aegean Systems SA",
    "France": "Seine Informatique",
    "Spain": "Ibérica Data Solutions",
    "Slovenia": "Triglav Software",
    "Czech Republic": "Vltava Tech s.r.o.",
    "Republic of Ireland": "Shannon Digital Services",
    "Bulgaria": "Sofia Cloud Systems",
}

# Contratos anuales ficticios (EUR) por cliente.
CONTRATOS_ANUALES_EUR = {
    "Germany": 150000, "Italy": 120000, "Poland": 90000, "United Kingdom": 140000,
    "Austria": 60000, "Greece": 50000, "France": 70000, "Spain": 55000,
    "Slovenia": 45000, "Czech Republic": 50000, "Republic of Ireland": 65000,
    "Bulgaria": 40000,
}

MINUTOS_POR_INTERACCION = 25   # supuesto: tiempo promedio real por interacción de agente
TARIFA_INTERNA_EUR_HORA = 45   # supuesto: costo interno de una hora de soporte


def enrich(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Created time"] = pd.to_datetime(df["Created time"])
    df["Resolution time"] = pd.to_datetime(df["Resolution time"])

    df["Cliente"] = df["Country"].map(CLIENTES)
    df["Contrato_Anual_EUR"] = df["Country"].map(CONTRATOS_ANUALES_EUR)

    # Esfuerzo real estimado (proxy de horas trabajadas, NO tiempo transcurrido)
    df["Horas_Efectivas_Estimadas"] = (
        df["Agent interactions"] * MINUTOS_POR_INTERACCION / 60
    ).round(2)
    df["Costo_Interno_Soporte_EUR"] = (
        df["Horas_Efectivas_Estimadas"] * TARIFA_INTERNA_EUR_HORA
    ).round(2)

    # Tiempo transcurrido entre creación y resolución (dato real de timestamps,
    # se conserva solo como referencia descriptiva, no como costo).
    df["Horas_Transcurridas"] = (
        (df["Resolution time"] - df["Created time"]).dt.total_seconds() / 3600
    ).round(2)

    return df


if __name__ == "__main__":
    original = pd.read_csv(INPUT_PATH)
    enriched = enrich(original)
    enriched.to_csv(OUTPUT_PATH, index=False)
    print(f"Dataset enriquecido guardado en {OUTPUT_PATH} ({len(enriched)} filas)")
