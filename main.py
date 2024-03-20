import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to resize the figure
def set_size(w, h, ax=None):
    # w, h: width, height in inches
    if not ax:
        ax = plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w) / (r - l)
    figh = float(h) / (t - b)
    ax.figure.set_size_inches(figw, figh)


xls = pd.ExcelFile("ListSurah.xlsx")

df = pd.read_excel(xls)
data_frame = df.sort_index(axis=1, ascending=True)

# Reversing the list of surah so that the first surah
# will start on the right of the plot
data_frame = data_frame.iloc[::-1]

x = data_frame.iloc[:, 0]
Y = data_frame.iloc[:, 3]

fig, ax = plt.subplots()
# Plot histogram
ax.scatter(x, Y)

plt.xticks(rotation=90)
plt.xlabel('Surah')
plt.ylabel('Number of Ayat')
plt.grid(True)
plt.subplots_adjust(left=None, bottom=0.16, right=None, top=None, wspace=None, hspace=None)

set_size(15, 10)

# Plotting "Alif"
array_alif1 = [112, 107, 108, 109, 113]
array_alif2 = [113, 108, 109, 110, 114]

temp1 = data_frame.iloc[113:114, 0]
temp2 = data_frame.iloc[113:114, 3]

for z in range(len(array_alif1)):
    fig, ax = plt.subplots()
    ax.scatter(x, Y)
    plt.xticks(rotation=90)
    plt.xlabel('Surah')
    plt.ylabel('Number of Ayat')
    plt.grid(True)
    plt.subplots_adjust(left=None, bottom=0.16, right=None, top=None, wspace=None, hspace=None)

    set_size(15, 10)

    alif_X = data_frame.iloc[array_alif1[z]:array_alif2[z], 0]
    alif_Y = data_frame.iloc[array_alif1[z]:array_alif2[z], 3]
    temp1 = pd.concat([temp1, alif_X])
    temp2 = pd.concat([temp2, alif_Y])

plt.plot(temp1, temp2, linewidth=2.0, color='blue')  # Set color for "Alif"

# Fill area under the curve for "Alif"
ax.fill_between(temp1, temp2, np.max(temp2), color='orange', alpha=0.8)

# Plotting "Lam Lam Ha"
array_lam1 = [105, 106, 101, 82, 73, 65, 54, 52, 48, 41, 17, 11, 6, 4, 0, 18, 58, 59, 71, 77, 86, 87, 91, 94, 88]
array_lam2 = [106, 107, 102, 83, 74, 66, 55, 53, 49, 42, 18, 12, 7, 5, 3, 19, 59, 60, 72, 78, 87, 88, 92, 95, 89]

temp3 = data_frame.iloc[88:89, 0]
temp4 = data_frame.iloc[88:89, 3]

for p in range(len(array_lam1)):
    lam_X = data_frame.iloc[array_lam1[p]:array_lam2[p], 0]
    lam_Y = data_frame.iloc[array_lam1[p]:array_lam2[p], 3]
    temp3 = pd.concat([temp3, lam_X])
    temp4 = pd.concat([temp4, lam_Y])

plt.plot(temp3, temp4, linewidth=2.0, color='red')  # Set color for "Lam Lam Ha"

# Fill area under the curve for "Lam Lam Ha"
ax.fill_between(temp3, temp4, np.max(temp4), color='green', alpha=0.8)

alif_df = pd.DataFrame({'Surah': temp1, 'No of Ayat': temp2})
print(alif_df)

lam_df = pd.DataFrame({'Surah': temp3, 'No of Ayat': temp4})
print(lam_df)

plt.show()
