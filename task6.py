items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    total_cost = 0
    total_calories = 0
    selected = []

    for name, props in sorted_items:
        if total_cost + props["cost"] <= budget:
            selected.append(name)
            total_cost += props["cost"]
            total_calories += props["calories"]

    return {
        "selected_items": selected,
        "total_cost": total_cost,
        "total_calories": total_calories
    }


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    # dp[i][w] = max calories with first i elements and budget w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Restore selected items
    w = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = names[i - 1]
            selected.append(name)
            w -= items[name]["cost"]

    total_calories = dp[n][budget]
    total_cost = sum(items[name]["cost"] for name in selected)

    return {
        "selected_items": list(reversed(selected)),
        "total_cost": total_cost,
        "total_calories": total_calories
    }


budget = 80

greedy_result = greedy_algorithm(items, budget)
print("Greedy algorithm result:")
print(greedy_result)

dp_result = dynamic_programming(items, budget)
print("\nDynamic programming result:")
print(dp_result)
