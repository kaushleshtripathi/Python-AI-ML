import matplotlib.pyplot as plt 
import numpy as np 


def section1():
    # line chart
    x = [1,2,3,4,5]
    y = [2,4,6,8,10]
    
    plt.figure(figsize=(7,4))
    plt.plot(x,y)
    
    plt.title("First Line Plot")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.show() 

def section2():
    # styled line chart
    x = np.arange(0,6)
    y = x**2    

    plt.figure(figsize=(7,4))
    plt.plot(x,y, color="red", linestyle="--", marker="o", markersize=8, markerfacecolor="blue")
    
    plt.title("Styled Line Plot")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid(True)
    plt.show() 

def section3():
    # multiple line chart
    x = np.linspace(0,2 * np.pi , 200)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.figure(figsize=(8,4))
    plt.plot(x, y1, label="sin(x)")
    plt.plot(x, y2, label="cos(x)")
    plt.title("Sine and Cosine Waves")
    plt.xlabel("x")
    plt.ylabel("values")
    plt.legend() 
    plt.grid(True)
    plt.show()

def section4():
    # scatter plot
    np.random.seed(42)    
    x = np.random.normal(50, 10, 100)
    y = x * 2 + np.random.normal(0, 10, 100)

    plt.figure(figsize=(7,4))
    plt.scatter(x,y, color="green", alpha=0.8)
    plt.title("Scatter Plot")
    plt.xlabel("Feature X")
    plt.ylabel("Feature Y")
    plt.grid(True)
    plt.show()

def section5():
    # bar chart 
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [10, 15, 7, 12, 20]

    plt.figure(figsize=(7,4))
    plt.bar(categories, values)
    plt.title("Bar Chart")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.show()

def section6():
    # histogram 
    np.random.seed(42)
    data = np.random.normal(70, 12, 500) 

    plt.figure(figsize=(7,4))
    plt.hist(data, bins=30, color="purple", alpha=0.7)
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()




if __name__ == "__main__":
    #section1()    
    #section2()
    #section3()
    #section4()
    #section5()
    section6()