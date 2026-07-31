# numpy-student-scores-analysis
# Student Exam Scores Analysis with NumPy

A simple data analysis project using **NumPy** to explore student exam performance across four subjects.

## 📊 Dataset

The dataset contains scores of **50 students** in the following subjects:

| Column Index | Subject  |
|--------------|----------|
| 0            | Math     |
| 1            | English  |
| 2            | Science  |
| 3            | History  |

## 🔍 What This Project Does

This script performs the following analysis:

1. **Descriptive Statistics**
   - Mean score per subject
   - Median score per subject
   - Standard deviation per subject

2. **Student Performance**
   - Total score of each student
   - Average score of each student

3. **Highest & Lowest Scores**
   - Maximum score in each subject
   - Minimum score in each subject

4. **Filtering**
   - Students who failed at least one subject (score < 50)
   - Students who scored above 80 in Math

## 🛠️ Requirements

- Python 3.x
- NumPy

Install NumPy if you don't have it:

```bash
pip install numpy
```

## ▶️ How to Run

```bash
python student_scores_analysis.py
```

## 📁 Project Structure

```
numpy-student-scores/
│
├── student_scores_analysis.py   # Main analysis script
└── README.md                    # Project documentation
```

## 📈 Sample Output

```
Shape of data: (50, 4)
----------------------------------------
Mean per subject (Math, English, Science, History): [...]
Median per subject: [...]
Standard Deviation per subject: [...]
...
```

## 🎯 Learning Goals

This project helps practice:

- Creating and working with NumPy arrays
- Using `axis` parameter in aggregation functions
- Filtering data with boolean indexing
- Basic statistical analysis

## 👤 Author

Enemuo Chidera Kingsley

---

Feel free to fork this repository and improve it!
