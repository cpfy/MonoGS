import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
import csv


def rand_data(mu, sigma, size):

    np.random.seed(19680801)
    data = np.random.normal(mu, sigma, size)
    return data


def ape_csv_data(file_path):

    data = []

    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            iter = int(row[0])
            ape_errors = [float(x) for x in row[1:]]
            data = data + ape_errors

    # ic(data, type(data))
    data = np.array(data)
    return data


def ape_csv_onearrow_data(file_path):

    data = []

    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            pass

        last_row = row
        ape_errors = [float(x) for x in last_row[1:]]
        data = data + ape_errors

    data = np.array(data)
    return data




file_path = "./apes/apes_iter120-2024-04-15-20-39-32.csv"
# file_path = './apes/apes_iter30-2024-04-16-10-26-25.csv'
# file_path = './apes/apes_iter20-2024-04-16-11-02-15.csv'



mu = 200
sigma = 25
n_bins = 25
# data = rand_data(mu, sigma, size=100)

data = ape_csv_data(file_path)
data = ape_csv_onearrow_data(file_path)

fig, ax = plt.subplots(figsize=(9, 6), layout="constrained")

ic(data, type(data), data.shape)

# Cumulative distributions.
ax.ecdf(data, label="CDF")
n, bins, patches = ax.hist(
    data,
    n_bins,
    density=True,
    histtype="step",
    cumulative=True,
    label="Cumulative histogram",
)

# x = np.linspace(data.min(), data.max())
# y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
#     np.exp(-0.5 * (1 / sigma * (x - mu))**2))
# y = y.cumsum()
# y /= y[-1]
# ax.plot(x, y, "k--", linewidth=1.5, label="Theory")


# Label the figure.
fig.suptitle("Cumulative distributions")

ax.grid(True)
ax.legend()
ax.set_xlabel("Translation Error (m)")
ax.set_ylabel("Probability of occurrence")
ax.label_outer()

plt.show()
