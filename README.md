# Tax Calculator Program

This project is a simple Python program that calculates income tax based on predefined tax slabs.  
The user enters their annual income, and the program computes the total tax payable using conditional logic.

---

## 📌 Features

- User-friendly input system  
- Calculates tax using multiple income slabs  
- Displays final tax amount  
- Beginner-friendly Python code  

---

## 🧮 Tax Slabs Used

| Income Range (₹) | Tax Rate |
|------------------|----------|
| Up to 4,00,000 | 0% |
| 4,00,001 – 8,00,000 | 5% |
| 8,00,001 – 12,00,000 | 10% |
| 12,00,001 – 16,00,000 | 15% |
| 16,00,001 – 20,00,000 | 20% and 25% (as written in the code) |
| 20,00,001 – 24,00,000 | 30% |
| Above 24,00,000 | 35% |

> **Note:** The tax slabs are represented exactly as implemented in the code (even if overlapping).

---

## 🏗️ How It Works

1. User inputs salary.
2. Salary is passed into the `Calculating_tax()` function.
3. The tax is calculated based on slab conditions.
4. The final tax amount is printed on the screen.

---

## ▶️ Usage

Run the script using:

```bash
python tax_calculator.py
