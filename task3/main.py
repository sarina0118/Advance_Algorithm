from coin_change import coin_change_limited
from mice_to_holes import assign_mice_to_holes
from hamiltonian import hamiltonian_cycle

print("-" * 30)
print("COIN CHANGE WITH LIMITED SUPPLY")
print("-" * 30)

coins = [1, 2, 5]
limits = [3, 2, 1]
target = 8

print("Coins:", coins)
print("Limits:", limits)
print("Target:", target)

result = coin_change_limited(coins, limits, target)

if result == -1:
    print("\nIt is impossible to make the target amount.")
else:
    print("\nMinimum coins required:", result)

print("-" * 30)
print("ASSIGN MICE TO HOLES")
print("-" * 30)

mice = [4, -4, 2]
holes = [4, 0, 5]

print("Mice:", mice)
print("Holes:", holes)

result = assign_mice_to_holes(mice, holes)

print("\nMinimum time required:", result)

print("\n" + "-" * 30)
print("HAMILTONIAN CYCLE")
print("-" * 30)

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

result = hamiltonian_cycle(graph)

if result is None:
    print("No Hamiltonian Cycle exists.")
else:
    print("Hamiltonian Cycle:")
    print(result)