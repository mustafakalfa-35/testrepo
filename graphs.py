import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_excel("table_data.xlsx", "Sheet1", header=0)
print(dataset.head())

# let's make all column labels of type string to make sure
dataset.columns = list(map(str, dataset.columns))

fig = plt.figure()
# plt.xlim(dataset.columns[0], dataset.columns[5])

ax1 = fig.add_subplot(2, 3, 1)
ax1.scatter(x=dataset["scenarios"], y=dataset["THD_RC_16°C"], color='r')
ax1.scatter(x=dataset["scenarios"], y=dataset["THD_RC_32°C"], color='b')
# ax1.set_xlim([dataset.columns[0], "case 5"])
plt.grid(True)
plt.ylabel('°C')
plt.title('THD_RC vs Scenarios')
plt.legend(["16°C", "32°C"], loc="upper left")

ax2 = fig.add_subplot(2, 3, 2)
ax2.scatter(x=dataset["scenarios"], y=dataset["THD_FC_16°C"], color='r')
ax2.scatter(x=dataset["scenarios"], y=dataset["THD_FC_32°C"], color='b')
plt.grid(True)
plt.ylabel('°C')
plt.title('THD_FC vs Scenarios')
plt.legend(["16°C", "32°C"], loc="upper left")

ax3 = fig.add_subplot(2, 3, 3)
ax3.scatter(x=dataset["scenarios"], y=dataset["EAN_16°C"], color='r')
ax3.scatter(x=dataset["scenarios"], y=dataset["EAN_32°C"], color='b')
plt.grid(True)
plt.ylabel('kWh/d')
plt.title('EAN vs Scenarios')
plt.legend(["16°C", "32°C"], loc="upper left")

ax4 = fig.add_subplot(2, 3, 4)
ax4.scatter(x=dataset["scenarios"], y=dataset["TND_RC_16°C"], color='r')
ax4.scatter(x=dataset["scenarios"], y=dataset["TND_RC_32°C"], color='b')
plt.grid(True)
plt.ylabel('°C')
plt.title('TND_RC vs Scenarios')
plt.legend(["16°C", "32°C"], loc="upper left")

ax5 = fig.add_subplot(2, 3, 5)
ax5.scatter(x=dataset["scenarios"], y=dataset["TND_FC_16°C"], color='r')
ax5.scatter(x=dataset["scenarios"], y=dataset["TND_FC_32°C"], color='b')
plt.grid(True)
plt.ylabel('°C')
plt.title('TND_FC vs Scenarios')
plt.legend(["16°C", "32°C"], loc="upper left")

ax6 = fig.add_subplot(2, 3, 6)
ax6.scatter(x=dataset["scenarios"], y=dataset["RED_16°C"], color='r')
ax6.scatter(x=dataset["scenarios"], y=dataset["RED_32°C"], color='b')
plt.grid(True)
plt.ylabel('RED')
plt.title('RED vs Scenarios')
plt.legend(["16°C", "32°C"], loc="upper left")

plt.show()