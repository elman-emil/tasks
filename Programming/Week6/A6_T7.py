print("Travel starting.")


#Learning to create a file in context to the task

with open("output.txt", "w") as f:
    lines = ["Line one", "Line two", "Line three"]

    for line in lines:
        f.write(line + "\n")







        
