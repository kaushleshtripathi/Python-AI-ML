import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 

sns.set_theme(style="whitegrid")

def section1():
    x = np.arange(1,11)
    y = np.array([20,22,25,24,28,30,33,35,38,40])

    plt.figure(figsize=(10,6))
    sns.lineplot(x=x,y=y, marker="o")
    plt.title("Line Plot Example")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()

def section2():
    np.random.seed(42)
    hours = np.random.uniform(1,10,80)
    marks = 40 + hours * 6 + np.random.normal(0,5,80)

    plt.figure(figsize=(10,6))
    sns.scatterplot(x=hours, y=marks, color="teal", alpha=0.7)
    plt.title("Scatter Plot Example")
    plt.xlabel("Study Hours")
    plt.ylabel("Exam Marks")
    plt.show()

def section3():
    np.random.seed(42)
    scores = np.random.normal(70, 10, 300)

    plt.figure(figsize=(10,6))
    sns.histplot(x=scores, bins=20, kde=True, color="coral")    
    plt.title("Histogram Example")
    plt.xlabel("Scores")
    plt.ylabel("Frequency")
    plt.show()

def section4():
    # box plot 
    np.random.seed(42)
    group_a = np.random.normal(60, 8, 120)
    group_b = np.random.normal(70, 10, 120)

    plt.figure(figsize=(10,6))
    sns.boxplot(data=[group_a, group_b], palette=["lightblue", "lightcoral"])
    plt.title("Box Plot Example")
    plt.xlabel("Groups")
    plt.ylabel("Values")
    plt.show()

def section5():
    # bar plot 
    departments = ["HR", "Finance", "IT", "Marketing", "Sales"]
    employees = [15, 25, 40, 30, 20]

    plt.figure(figsize=(10,6))
    sns.barplot(x=departments, y=employees, palette="viridis")
    plt.title("Bar Plot Example")
    plt.xlabel("Departments")
    plt.ylabel("Number of Employees")
    plt.show()

if __name__ == "__main__":
    #section1() 
    #section2()
    #section3()
    #section4()
    section5()
