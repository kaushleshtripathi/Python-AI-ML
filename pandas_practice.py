import pandas as pd 

data = {
    "student_id": [1,2,3,4,5,6],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "age": [20, 21, 22, 23, 24, 25],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "score": [85, 90, 78, 92, 88, 95]
}


df = pd.DataFrame(data)

def section1():
    
    print(df.head(2))
    print(df.tail(2))
    print(df.shape)
    print(df.info())
    print(df.dtypes)

def section2():
    print(df["score"])
    print(df[["name","score"]])

    print(df.iloc[0])

def section3():
    selected_rows = df[df["score"] >= 80]
    print(selected_rows)

def section4():
    # update opeartion 
    df["result"] = df["score"].where(df["score"] >= 80, "Fail") 
    df["result"] = df["result"].where(df["result"] == "Fail", "Pass")
    print(df)   

def section5():
    print(df["score"].mean())
    print(df["score"].min())
    print(df["score"].max())

    print(df.sort_values(by="score", ascending=False))
    

if __name__ == "__main__":
    #section1()
    #section2()
    #section3()
    #section4()
    section5()