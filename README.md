# Car Management & Sorting System

This is a Python-based project for managing, searching, and sorting a list of cars based on different criteria. The project was developed as part of an academic assignment, implementing sorting and searching algorithms for vehicle data.

## Features 
- **Sorting algorithms**: Implements both O(n²) and O(n log n) sorting techniques.
- **Search algorithms**: Supports both sequential search and binary search.
- **Car entity management**: Each car has attributes like brand, model, token, purchase price, and sale price.
- **Command-based interface**: Users can interact with the program using commands.
- **Easter Egg 😺**: A hidden `easteregg.py` script for extra functionality.

## Sorting Options 📊
The program allows sorting cars by:
- Token
- Brand & Model
- Brand, Model & Token
- Profit (Sale Price - Purchase Price)


## Algorithm Execution Time Comparison


| Algorithm          | 50 Elements | 100 Elements | 200 Elements | 500 Elements | 1000 Elements | 2500 Elements | 5000 Elements | 10000 Elements | 100000 Elements | 1 Million Elements |
|-------------------|------------|-------------|-------------|-------------|--------------|--------------|--------------|---------------|----------------|-----------------|
| **Bubble Sort**   | 0.001s     | 0.006s      | 0.022s      | 0.133s      | 0.563s       | 3.611s       | 15.937s      | 62.348s       | Estimated      | Estimated       |
| **Merge Sort**    | 0.0005s    | 0.0013s     | 0.002s      | 0.0055s     | 0.0116s      | 0.0345s      | 0.0804s      | 0.1781s       | 27.918s        | 11142.86s       |
| **Sequential Search** | 0.001s  | 0.001s      | 0.0015s     | 0.001s      | 0.002s       | 0.0035s      | 0.0077s      | 0.0131s       | 0.2065s        | 2.167s          |
| **Binary Search** | 0.0000s    | 0.0000s     | 0.0000s     | 0.0000s     | 0.0000s      | 0.0000s      | 0.0000s      | 0.0000s       | 0.0s           | 0.0s            |


