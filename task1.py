import tkinter as tk
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
w.title("please kill me")
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()



wallCoords = []
f = open('map1.txt')
data = f.read()
data = list(data)

x = 0
y = 0
lines = 0

for i in data:
    print(i)
    if i == "*":
        wallCoords.append( c.create_rectangle(0 +(25 * x),0 +(25* y),25 +(25 * x),25 +(25 * y),fill = "black") )
    x += 1
    
    if x == 30:
        y += 1
        x = 0
        



w.mainloop()