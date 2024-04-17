import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
import csv


def rand_data():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # generate some random test data
    all_data = [np.random.normal(1, std, 200) for std in range(20, 0, -1)]
    return all_data


def ape_csv_data(num=30):

    data = []

    # if num == 30:
    #     file_path = "./results/tum_rgbd_dataset_freiburg1_desk/2024-04-15-16-38-49/plot/stats_0030.csv"
    # elif num == 100:
    #     file_path = "./results/tum_rgbd_dataset_freiburg1_desk/2024-04-15-16-16-23/plot/stats_0100.csv"
    # elif num == 50:
    #     file_path = "./results/tum_rgbd_dataset_freiburg1_desk/2024-04-15-18-02-18/plot/stats_0050.csv"
    # elif num == 15:
    #     file_path = "./results/tum_rgbd_dataset_freiburg1_desk/2024-04-15-17-03-02/plot/stats_0015.csv"
    # elif num == 10:
    #     file_path = "./results/tum_rgbd_dataset_freiburg1_desk/2024-04-15-17-11-47/plot/stats_0010.csv"
    # elif num == 20:
    #     file_path = "./results/tum_rgbd_dataset_freiburg1_desk/2024-04-15-18-15-22/plot/stats_0020.csv"

    file_path = "./apes/apes_iter120-2024-04-15-20-39-32.csv"
    # file_path = './apes/apes_iter30-2024-04-16-10-26-25.csv'
    # file_path = './apes/apes_iter20-2024-04-16-11-02-15.csv'

    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            iter = int(row[0])
            ape_errors = [float(x) for x in row[1:]]
            data.append(ape_errors)

    ic(data, type(data))
    return data


# 以下是draw部分
def draw_boxplot(data):
    fig, ax = plt.subplots(figsize=(12, 4))

    # plot box plot
    ax.boxplot(data, whis=10)
    ax.set_title("Box plot")

    # x刻度计算
    n = len(data)
    xtick_indices = np.linspace(0, n, 5, dtype=int)
    ic(xtick_indices)

    # 获取中位数值，绘制中位数连接线
    medians = [np.median(dat) for dat in data]
    n = len(medians)
    x = np.arange(1, n + 1)

    ax.yaxis.grid(True)
    ax.set_xticks(xtick_indices)
    ax.set_xticklabels(xtick_indices)
    ax.set_xlabel("Iteration Steps")
    ax.set_ylabel("Translation error")

    ax.plot(x, medians, color="black", linewidth=1.5, linestyle="-")

    plt.show()


def draw_separate_trend(data, samples=10, filter=0):
    fig, ax = plt.subplots(figsize=(12, 4))

    n = len(data[0])
    rand_index = np.random.randint(0, n - 1, samples)
    ic(n, rand_index)

    for i in rand_index:
        draw_data = []
        for dat in data:
            # ic(len(dat), i)
            draw_data.append(dat[i])

        if filter > 0 and np.average(draw_data) > filter:
            continue

        ax.plot(draw_data, label=f"frame={i}")

    # x刻度计算
    n = len(data)
    xtick_indices = np.linspace(0, n, 5, dtype=int)

    ax.yaxis.grid(True)
    ax.set_xticks(xtick_indices)
    ax.set_xticklabels(xtick_indices)
    ax.set_xlabel("Iteration Steps")
    ax.set_ylabel("Translation error")
    ax.legend()
    plt.show()


data = ape_csv_data(20)
# draw_boxplot(data)
draw_separate_trend(data, samples=20, filter=0.1)
