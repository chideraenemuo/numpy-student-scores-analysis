import numpy as np
# Student Exam Scores Dataset
# Columns: [Math, English, Science, History]
data = np.array([
    [78, 85, 90, 72],
    [65, 70, 68, 75],
    [92, 88, 95, 90],
    [55, 60, 58, 62],
    [80, 82, 78, 85],
    [70, 75, 72, 68],
    [88, 90, 85, 92],
    [60, 55, 65, 58],
    [95, 92, 98, 94],
    [72, 78, 70, 75],
    [85, 80, 88, 82],
    [50, 45, 55, 48],
    [77, 83, 79, 81],
    [68, 72, 65, 70],
    [90, 87, 93, 89],
    [58, 62, 60, 55],
    [82, 85, 80, 84],
    [73, 70, 75, 72],
    [96, 94, 97, 95],
    [66, 68, 64, 70],
    [79, 81, 77, 80],
    [54, 50, 58, 52],
    [87, 89, 86, 90],
    [71, 74, 69, 73],
    [93, 91, 94, 92],
    [61, 65, 59, 63],
    [84, 86, 83, 85],
    [69, 67, 71, 68],
    [91, 93, 90, 94],
    [57, 53, 60, 55],
    [76, 79, 74, 78],
    [63, 66, 62, 65],
    [89, 88, 91, 87],
    [52, 48, 55, 50],
    [81, 84, 80, 83],
    [74, 76, 72, 75],
    [97, 95, 98, 96],
    [67, 69, 65, 70],
    [83, 85, 82, 84],
    [59, 61, 57, 60],
    [86, 88, 85, 89],
    [70, 73, 68, 72],
    [94, 92, 96, 93],
    [56, 54, 59, 55],
    [78, 80, 77, 79],
    [64, 67, 63, 66],
    [90, 89, 92, 91],
    [53, 50, 56, 52],
    [85, 87, 84, 86],
    [72, 75, 70, 74]
])
#print("Shape of data:", data.shape)
#print(data)
##Find mean, median, standard deviation of each subject
mean_score = np.mean(data,axis = 0)
median_score = np.median(data,axis = 0)
std_score = np.std(data,axis = 0)
##Find total score of each student
Total_score = np.sum(data,axis = 1)
##Highest and lowest score in each subject
max_score = np.max(data,axis = 0)
min_score = np.min(data,axis = 0)
##Average score per student
avg_score = np.mean(data,axis = 1)
##Students who failed any subject (score < 50)
failed_student = data[data < 50]
##Students who scored above 80 in Math
math_above_80 = data[data[:, 0] > 80]
print(f"mean per subject: {mean_score}")
print(f"median per subject : {median_score}")
print(f"std per subject : {std_score}")
print(f"total per subject : {Total_score}")
print(f"max per subject : {max_score}")
print(f"min per subject : {min_score}")
print(f"average per subject : {avg_score}")
print(f" student who failed: {failed_student}")
print(math_above_80)
