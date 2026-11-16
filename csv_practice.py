import csv
import os

# ==========================================
# EXERCISE 2: Read and Print Raw Rows
# ==========================================
print("--- Exercise 2: Raw Rows ---")
with open("data/sales.csv", mode="r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ==========================================
# EXERCISE 3: Clean & Convert Types
# ==========================================
print("\n--- Exercise 3: Clean & Convert Types ---")
cleaned_data = []
with open("data/sales.csv", mode="r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        cleaned_data.append((product, price, quantity))
        print((product, price, quantity))

# ==========================================
# EXERCISE 4: Calculate Revenue Per Row
# ==========================================
print("\n--- Exercise 4: Revenue per Row ---")
for product, price, quantity in cleaned_data:
    revenue = round(price * quantity, 2)
    print(f"{product} revenue: ${revenue:.2f}")

# ==========================================
# EXERCISE 5: Summary Statistics
# ==========================================
print("\n--- Exercise 5: Summary Statistics ---")
total_revenue = 0.0
total_quantity = 0
top_product = ""
top_revenue = -1.0

for product, price, quantity in cleaned_data:
    revenue = price * quantity
    total_revenue += revenue
    total_quantity += quantity
    if revenue > top_revenue:
        top_revenue = revenue
        top_product = product

avg_quantity = total_quantity / len(cleaned_data) if cleaned_data else 0

print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Order Quantity: {avg_quantity:.2f}")
print(f"Top Revenue Product: {top_product} (${top_revenue:.2f})")

# ==========================================
# EXERCISE 6: Write Cleaned Report
# ==========================================
print("\n--- Exercise 6: Write Cleaned Report ---")
os.makedirs("data", exist_ok=True)
with open("data/cleaned.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "price", "quantity", "revenue"])
    for product, price, quantity in cleaned_data:
        revenue = round(price * quantity, 2)
        writer.writerow([product, price, f"{revenue:.2f}"])
print("data/cleaned.csv created successfully.")

# ==========================================
# EXERCISE 7: Filter Top Sales
# ==========================================
print("\n--- Exercise 7: Filter Top Sales ---")
top_sales_count = 0
with open("data/top_sales.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "price", "quantity", "revenue"])
    for product, price, quantity in cleaned_data:
        revenue = round(price * quantity, 2)
        if revenue > 500:
            writer.writerow([product, price, f"{revenue:.2f}"])
            top_sales_count += 1
print(f"Wrote {top_sales_count} rows to data/top_sales.csv.")

# ==========================================
# EXERCISE 8: DictReader / DictWriter Refactor
# ==========================================
print("\n--- Exercise 8: DictReader / DictWriter Refactor ---")
with open("data/sales.csv", mode="r", newline="") as infile, open("data/dict_cleaned.csv", mode="w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ["product", "price", "quantity", "revenue"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        revenue = round(price * quantity, 2)
        print(f"{product} (DictReader) revenue: ${revenue:.2f}")
        writer.writerow({
            "product": product,
            "price": price,
            "quantity": quantity,
            "revenue": f"{revenue:.2f}"
        })

# ==========================================
# REFLECTION QUESTIONS
# ==========================================
# 1. Why is type conversion (str -> float/int) necessary after reading a CSV?
# Answer: CSV files store all data as plain text strings. When Python's csv module reads a CSV file,
# it imports every field as a string data type. Mathematical operations like multiplication,
# addition, or numeric comparisons cannot be directly performed on strings (or would result in
# string concatenation instead of numeric arithmetic). Therefore, converting strings to appropriate
# numeric types (float or int) is necessary to perform calculation and aggregation.

# 2. What are the advantages of csv.DictReader over csv.reader?
# Answer: csv.DictReader maps the information in each row to a Python dictionary where keys are derived
# from the header row (column names). This makes code significantly more readable, self-documenting,
# and robust to changes in CSV column ordering. Developers can access fields by column name
# (e.g., row['price']) rather than relying on positional hardcoded integer indices (e.g., row[1]),
# reducing errors if columns are added, removed, or reordered in the source CSV.
