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

def compute_sss(salary): return salary * RATES["SSS"]
def compute_philhealth(salary): return salary * RATES["PhilHealth"]
def compute_pagibig(salary): return salary * RATES["Pag-IBIG"]
def compute_tax(salary): return salary * RATES["Tax"]

def run_task_parallelism(name, salary):
    print(f"\n>>> Part A: Task Parallelism for {name}")
    
    tasks = {
        "SSS": compute_sss,
        "PhilHealth": compute_philhealth,
        "Pag-IBIG": compute_pagibig,
        "Withholding Tax": compute_tax
    }
    
    total_deduction = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks concurrently and return Future objects
        futures = {executor.submit(func, salary): label for label, func in tasks.items()}
        
        for future in concurrent.futures.as_completed(futures):
            label = futures[future]
            amount = future.result()
            total_deduction += amount
            print(f" - {label}: {amount:.2f} | Thread: {threading.current_thread().name}")
            
    print(f"Total Deduction for {name}: {total_deduction:.2f}")

   # PART B - DATA PARALLELISM LOGIC
def compute_full_payroll(employee):
    name, salary = employee
    total_deduction = salary * 0.19 
    net_salary = salary - total_deduction
    return name, salary, total_deduction, net_salary

def run_data_parallelism(data_list):
    print("\n>>> Part B: Data Parallelism for All Employees")
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(compute_full_payroll, data_list))
        
        for name, gross, deduct, net in results:
            print(f"Employee: {name:8} | Gross: {gross:7} | Total Deductions: {deduct:8.2f} | Net Salary: {net:8.2f}")


# MAIN EXECUTION
if __name__ == "__main__":
    print("Payroll System Project Initialized.")
    
    # Run Part A for the first employee
    run_task_parallelism(employees[0][0], employees[0][1])
    
    # Run Part B for all employees
    run_data_parallelism(employees)