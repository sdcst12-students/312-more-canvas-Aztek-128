import tkinter as tk
"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""
'''
0000000000
0661111223
0661111233
1111122333
1111223334
5551223344
5511122223
5551111222
1155111222
1111122222
1111122266
'''


w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
water = tk.PhotoImage(file="assets/map.water.png")
plains = tk.PhotoImage(file="assets/map.plains.png")
forest = tk.PhotoImage(file="assets/map.forest.png")
hills = tk.PhotoImage(file="assets/map.hills.png")
mountains = tk.PhotoImage(file="assets/map.mountain.png")
swamp = tk.PhotoImage(file="assets/map.swamp.png")
city = tk.PhotoImage(file="assets/map.city.png")
c.create_rectangle(20,20,30,30,fill='green')
x = 0
y = 0
textures = []
f = open('map2.txt')
data = f.read()
data = list(data)
#textures.append(c.create_image(20,20,image = water))
for i in data:
    x+=1
    print(i,end="")
    if i  == "0":
        print(i) 
        c.create_image(20*x,20*y,image = water)
    if i == "1":
        c.create_image(20*x,20*y, image = plains)
    

w.mainloop()