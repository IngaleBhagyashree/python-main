
# Matplotlib is a plotting library used to create data visualizations like graphs and charts. It's helpful for understanding patterns in your data visually.
# ✅ Key Uses:
# Plotting line, bar, scatter, pie chart
# Customizing colors, labels, titles
# Making data easier to interpret visually

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
