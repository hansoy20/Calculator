import concurrent.futures
import threading

# Given Employee Data 
employees = [
    ("Alice", 25000), ("Bob", 32000), ("Charlie", 28000),
    ("Diana", 40000), ("Edward", 35000)
]

# Shared Deduction Rates 
RATES = {
    "SSS": 0.045,
    "PhilHealth": 0.025,
    "Pag-IBIG": 0.02,
    "Tax": 0.10
}

if __name__ == "__main__":
    print("Payroll System Project Initialized.")
    