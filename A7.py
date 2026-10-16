import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df = df.dropna()
print(df.head())
print(df.info())

sns.barplot(x="day", y="total_bill", hue="sex", data=df, )
plt.title("Average Total Bill by Day ")
plt.xlabel("Day")
plt.ylabel("Average Total Bill ($)")
plt.show()

sns.boxplot(x="day", y="total_bill", hue="sex", data=df)
plt.title("Spread of Total Bill by Day ")
plt.xlabel("Day")
plt.ylabel("Count")
plt.show()

sns.boxplot(x="day", y="total_bill", hue="sex", data=df)
plt.title("Spread of Total Bill by Day ")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()

sns.swarmplot(x="day", y="total_bill", hue="sex", data=df)
plt.title("everyday bill amount per day ")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()

sns.stripplot(x="day", y="total_bill", hue="sex", data=df)
plt.title("everyday bill amount per day ")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()

sns.pairplot(df[["total_bill", "tip", "size"]])
plt.suptitle("Pairplot of Total Bill, Tip, and Size", y=1.02)
plt.show()

sns.pointplot(x="day", y="total_bill", hue="sex", data=df)
plt.title("everyday bill amount per gender ")
plt.xlabel("Day")
plt.ylabel("Average Bill ($)")
plt.show()

sns.implot(x="total_bill", y="tip", hue="sex", data=df)
plt.title("Total Bill vs. Tip trend line")
plt.show()

