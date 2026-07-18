import os
import pandas as pd
import matplotlib.pyplot as plt


os.makedirs("graphs", exist_ok=True)


data = pd.read_csv("outputs/performance_results.csv")


pivot = data.pivot(
    index="Dataset",
    columns="Data Structure",
    values="Insert Time"
)

pivot.plot(marker="o")

plt.title("Insert Time Comparison")
plt.xlabel("Dataset")
plt.ylabel("Time (seconds)")
plt.grid(True)

plt.savefig("graphs/insert_time.png")

plt.close()


search_data = data[data["Search Time"] != "N/A"].copy()
search_data["Search Time"] = search_data["Search Time"].astype(float)

pivot = search_data.pivot(
    index="Dataset",
    columns="Data Structure",
    values="Search Time"
)

pivot.plot(marker="o")

plt.title("Search Time Comparison")
plt.xlabel("Dataset")
plt.ylabel("Time (seconds)")
plt.grid(True)

plt.savefig("graphs/search_time.png")

plt.close()


delete_data = data.copy()

delete_data["Delete/Remove Time"] = pd.to_numeric(
    delete_data["Delete/Remove Time"]
)

pivot = delete_data.pivot(
    index="Dataset",
    columns="Data Structure",
    values="Delete/Remove Time"
)

pivot.plot(marker="o")

plt.title("Delete / Remove Time Comparison")
plt.xlabel("Dataset")
plt.ylabel("Time (seconds)")
plt.grid(True)

plt.savefig("graphs/delete_time.png")

plt.close()

print("Graphs created successfully!")