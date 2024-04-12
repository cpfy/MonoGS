import matplotlib.pyplot as plt
import numpy as np
from icecream import ic


def test1_tracking_time():
    tracking_itr_num = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    tracking_iter_time = [1.1631321690510958, 1.065244141034782, 1.0187780971173197, 1.0486418900545686, 1.0026543620042503, 1.391871620900929, 1.3108217609114945, 1.4237884080503136, 1.440784557024017, 1.4759916090406477]
    tracking_iter_time_per_itr = [0.02326264338102192, 0.021304882820695637, 0.020375561942346396, 0.02097283780109137, 0.020053087240085005, 0.02783743241801858, 0.02621643521822989, 0.028475768161006273, 0.02881569114048034, 0.029519832180812954]
    fps = [1/i for i in tracking_iter_time_per_itr]

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(tracking_iter_time)
    plt.title('Tracking Time (50 iterations full time)')
    plt.xlabel('Sample')
    plt.ylabel('Time (s)')

    mean_time = sum(tracking_iter_time) / len(tracking_iter_time)
    plt.axhline(y=mean_time, color='r', linestyle='--', label='Mean')

    plt.subplot(1, 2, 2)
    plt.plot(fps)
    plt.title('FPS per Sample')
    plt.xlabel('Sample')
    plt.ylabel('frames/s')


    mean_fps = sum(fps) / len(fps)
    plt.axhline(y=mean_fps, color='r', linestyle='--', label='Mean FPS')

    plt.tight_layout()
    plt.show()



def test2_tracking_time_stepdetail():
    """
    各个语句时间统计

    废弃了。++新任务。。。。
    """
    times = [
        ("render", 0.005286599043756723),
        ("analyze render_pkg", 0.0004446629900485277),
        ("pose_optimizer.zero_grad()", 0.000460407929494977),
        ("get_loss_tracking", 0.0005814761389046907),
        ("loss_tracking.backward()", 0.0008716129232198),
        ("update_pose", 0.01734240003861487),
        ("single iteration fulltime", 0.026828902075067163),
    ]


    # 计算 "single iteration fulltime"
    fulltime = sum(time for _, time in times[:-1])
    ic(fulltime, times[-1])

    # 计算每个时间间隔的平均值
    avg_times = [(label, value) for label, value in times]
    avg_times.append(("single iteration fulltime", fulltime))

    # 绘制堆叠柱状图
    fig, ax = plt.subplots(figsize=(12, 6))

    labels, values = zip(*avg_times)
    x = np.arange(len(labels))
    bar_width = 0.8

    # 定义颜色
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

    # 绘制堆叠柱状图
    bottom = np.zeros(len(x))
    for i, value in enumerate(values):
        ax.bar(x, [value], bottom=bottom, width=bar_width, color=colors[i], label=labels[i])
        bottom += [value]

    ax.set_xlabel("Time Interval")
    ax.set_ylabel("Time (seconds)")
    ax.set_title("Time Breakdown")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=90)
    ax.legend()

    plt.tight_layout()
    plt.show()




def meantime():
    data= [0.08333194605074823, 0.13522223802283406, 0.08803613507188857, 0.07910172711126506, 0.07490808493457735, 0.07503540301695466, 0.07776211807504296, 0.07647342700511217, 0.07556876703165472, 0.07540156692266464, 0.0756140819285065, 0.0754945061635226, 0.07515601301565766, 0.10749649000354111, 0.16156439203768969, 0.11406828090548515, 0.11226686090230942, 0.10167270805686712, 0.076524977106601, 0.08090247400105, 0.1329280328936875, 0.1259789930190891, 0.145313270855695, 0.08246664307080209, 0.08566420804709196, 0.11256026895716786, 0.10116071300581098, 0.11378220305778086, 0.08518234291113913, 0.08347221580334008, 0.08784409612417221, 0.08482651994563639, 0.09116391302086413, 0.10058267810381949, 0.11527287494391203, 0.0926085680257529, 0.1396172980312258, 0.0856991158798337]


    plt.figure(figsize=(12, 4))

    plt.plot(data)
    plt.title('Ply save time')
    plt.xlabel('Num')
    plt.ylabel('Time (s)')

    mean_time = sum(data) / len(data)
    plt.axhline(y=mean_time, color='r', linestyle='--', label='Mean')

    plt.tight_layout()
    plt.show()


meantime()
