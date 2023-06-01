import tkinter as tk
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
label = tk.Label(text = "penis")



wallCoords = []
f = open('map1.txt')
data = f.read()
data = list(data)
for i in data:
    ix = 0 * i[0]
    ix2 = 0 * i[1]
    x = 0
    y = 0
    xi = x + 25
    yi = y + 25    
    print(i)
    if i == "*":
        wallCoords.append( c.create_rectangle(x,y,xi,yi,fill = "black") )




label.pack()





w.mainloop()