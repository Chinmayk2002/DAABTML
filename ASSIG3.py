# # Write a program to solve a fractional Knapsack problem using a greedy method

def fractional_knapsack(items, capacity):
    for item in items:
        item["ratio"] = item["profit"] / item["weight"]

    items.sort(key=lambda x: x["ratio"], reverse=True)

    total_value = 0.0
    knapsack = []

    for item in items:
        if item["weight"] <= capacity:
            knapsack.append(item)
            total_value += item["profit"]
            capacity -= item["weight"]
        else:
            fraction = capacity / item["weight"]
            knapsack.append({"item": item["item"], "weight": capacity, "profit": item["profit"] * fraction, "ratio": item["ratio"]})
            total_value += item["profit"] * fraction
            break

    return knapsack, total_value

def take_user_input():
    items = []
    num_items = int(input("Enter the number of items: "))

    for i in range(num_items):
        item = {}
        item["item"] = i + 1
        item["profit"] = int(input(f"Enter the profit for item {i + 1}: "))
        item["weight"] = int(input(f"Enter the weight for item {i + 1}: "))
        items.append(item)

    capacity = int(input("Enter the maximum weight capacity of the knapsack: "))

    return items, capacity

if __name__ == "__main__":
    items, capacity = take_user_input()

    selected_items, total_value = fractional_knapsack(items, capacity)
    
    print("\nSelected Items:")
    for item in selected_items:
        print(f"Item: {item['item']}, Weight: {item['weight']}, Profit: {item['profit']}")

    print(f"Total Profit in Knapsack: {total_value}")


'''
    items = [
        {"item": 1, "profit": 280, "weight": 40},
        {"item": 2, "profit": 100, "weight": 10},
        {"item": 3, "profit": 120, "weight": 20},
        {"item": 4, "profit": 120, "weight": 24}
    ]
'''
