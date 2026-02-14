import concurrent.futures
import threading


employees = [
    ("Alice", 25000), ("Bob", 32000), ("Charlie", 28000),
    ("Diana", 40000), ("Edward", 35000)
]

RATES = {
    "SSS": 0.045,
    "PhilHealth": 0.025,
    "Pag-IBIG": 0.02,
    "Tax": 0.10
}

