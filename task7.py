import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls: int = 100000):
    counts = {sum_: 0 for sum_ in range(2, 13)}

    # Shooting simulation
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        counts[total] += 1

    # Calculating probabilities
    probabilities = {k: v / num_rolls for k, v in counts.items()}
    return probabilities, counts


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(sums, probs, color='skyblue', edgecolor='black')
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)")
    plt.xticks(sums)
    plt.ylim(0, max(probs) * 1.2)

    for bar, prob in zip(bars, probs):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 f"{prob * 100:.2f}%", ha="center", va="bottom")

    plt.show()


def main():
    num_rolls = 100000
    probabilities, counts = simulate_dice_rolls(num_rolls)

    print("Сума\tЙмовірність\tКількість")
    for sum_ in range(2, 13):
        prob = probabilities[sum_]
        count = counts[sum_]
        print(f"{sum_}\t{prob:.4f}\t\t{count}")

    plot_probabilities(probabilities)


if __name__ == "__main__":
    main()
