import pandas as pd

# CPCB-based + persona-adjusted thresholds [web:22][web:31]
RISK_THRESHOLDS = {
    "children": {
        "Safe": (0, 50),
        "Caution": (51, 100),
        "Dangerous": (101, 150),
        "Emergency": (151, 500)
    },
    "elderly": {
        "Safe": (0, 50),
        "Caution": (51, 100),
        "Dangerous": (101, 150),
        "Emergency": (151, 500)
    },
    "outdoor_workers": {  # ← YOU WERE MISSING THIS
        "Safe": (0, 50),
        "Caution": (51, 100),
        "Dangerous": (101, 200),
        "Emergency": (201, 500)
    }
}

UNSAFE_THRESHOLDS = {
    "children": 151,
    "elderly": 151,
    "outdoor_workers": 101
}

def get_risk_level(aqi: float, persona: str) -> str:
    """Returns risk level for given AQI and persona."""
    if persona not in RISK_THRESHOLDS:
        raise ValueError(f"Persona {persona} not supported")
    
    thresholds = RISK_THRESHOLDS[persona]
    for risk_level, (low, high) in thresholds.items():
        if low <= aqi <= high:
            return risk_level
    return "Emergency"  # AQI > 500

def is_unsafe_day(aqi: float, persona: str) -> bool:
    """True if day is unsafe for this persona."""
    threshold = UNSAFE_THRESHOLDS[persona]
    return aqi >= threshold
