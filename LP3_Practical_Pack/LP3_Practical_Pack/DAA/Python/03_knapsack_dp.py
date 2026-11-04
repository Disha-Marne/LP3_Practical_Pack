"""Practical 3: 0/1 Knapsack using dynamic programming."""


def knapsack(weights, values, capacity):
    """Return the maximum value achievable without exceeding capacity."""
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")
    if any(weight < 0 for weight in weights):
        raise ValueError("weights must be non-negative")

    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]
        for current_capacity in range(capacity + 1):
            dp[i][current_capacity] = dp[i - 1][current_capacity]
            if weight <= current_capacity:
                dp[i][current_capacity] = max(
                    dp[i][current_capacity],
                    value + dp[i - 1][current_capacity - weight],
                )

    return dp[n][capacity]


def main():
    try:
        n = int(input("Number of items: "))
        if n < 0:
            print("Number of items must be non-negative.")
            return

        weights = list(map(int, input("Enter weights separated by spaces: ").split()))
        values = list(map(int, input("Enter values separated by spaces: ").split()))
        capacity = int(input("Enter capacity: "))

        if len(weights) != n or len(values) != n:
            print("Invalid input. Enter exactly n weights and n values.")
            return
        if capacity < 0:
            print("Capacity must be non-negative.")
            return
        if any(weight < 0 for weight in weights):
            print("Weights must be non-negative.")
            return
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    print("Maximum value:", knapsack(weights, values, capacity))
    print(f"Time: O(nW); space: O(nW), where n is item count and W is capacity.")


if __name__ == "__main__":
    main()

