import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

file = "./log/frontend_stats_history.csv"
df = pd.read_csv(filepath_or_buffer=file,encoding="cp932")
df_time = df.iloc[:, 0]         #タイムスタンプ
df_init_time = df.iloc[0,0]     #開始時間
df_time -= df_init_time         #タイムスタンプの整理，x軸
df_req = df.iloc[:, 4]          #リクエスト/s，y軸1
df_res = df.iloc[:, 22]         #最大応答時間，y軸2

fig = plt.figure()

ax1 = fig.subplots()
ax2 = ax1.twinx()
ax1.plot(df_time, df_res, c="b", label="res")
ax2.plot(df_time, df_req, c="r", label="req")
ax1.set_xlabel("Time Stamp (s)", fontsize=10)
ax1.set_ylabel("Total Max Response Time (s)", fontsize=10)
ax2.set_ylabel("Requests per second", fontsize=10)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2)
ax1.set_xlim(0)
ax1.set_ylim(0)
plt.savefig('./graph/frontend_graph_data.png')
plt.show()
plt.close()