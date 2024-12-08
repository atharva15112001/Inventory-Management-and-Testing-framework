# Inventory Management and Testing Framework

## Overview
A Python-based inventory management system that allows handling of products, categories, pricing, and ratings with CSV file integration. The project includes a robust testing suite using `pytest` to ensure functionality and reliability.

## Features
- **Product Management**:
  - Manage product attributes like name, category, price, ratings, and more.
  - Dynamic updates to pricing and ratings.
- **Inventory Operations**:
  - Add, filter, and manage products in the inventory.
  - Perform bulk stock updates.
- **CSV Integration**:
  - Load and manage products from CSV files with error handling.
- **Testing Framework**:
  - Automated tests using `pytest` for validation of operations and methods.

## Usage
1. **Initialize the Inventory**:
   ```python
   from START_asn_1 import myInventory
   inventory = myInventory("Inventory Name", "file.csv")
