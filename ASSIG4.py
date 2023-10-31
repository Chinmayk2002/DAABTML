# Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy

def knapsack_01(profits, weights, capacity):
    n = len(profits)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items

if __name__ == "__main__":
    profits = list(map(int, input("Enter profits separated by spaces: ").split()))
    weights = list(map(int, input("Enter weights separated by spaces: ").split()))
    capacity = int(input("Enter the knapsack capacity: "))

    max_profit, selected_items = knapsack_01(profits, weights, capacity)

    print("Maximum Profit:", max_profit)
    print("Selected Items:")
    for i in selected_items:
        print(f"Item {i}: Profit {profits[i]}, Weight {weights[i]}")

'''
    profits = [2, 3, 4, 1]
    weights = [3, 4, 5, 6]
    capacity = 8
'''