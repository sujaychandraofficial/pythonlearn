names=["sujay","chandra","sri","sai"]
wiegts=[1,2,3,4]

for name,we in zip(names,wiegts):
    print("name = {} and weight = {}".format(name,we))

some_list=[("sujay",1),("chandra",2),("sri",3),("sai",4)]
newlist,weightlist=zip(*some_list)
print(newlist)
print(weightlist)


for i,name in enumerate(names):
    print(i,name)



x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for l,x,y,z in zip(labels,x_coord,y_coord,z_coord):
    points.append("{} : {} {} {}".format(l,x,y,z))


for point in points:
    print(point)


cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast = []
for i in zip(cast_names,cast_heights):
    cast.append(i)
print(cast)


cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names=[]
heights=[]
# define names and heights here
names,heights=zip(*cast)
print(names)
print(heights)


data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)


cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]


cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)

S_list=["sujay","chandr","super","practice"]
s1_list=[1,2,3,4]
s2_list=[]
for i in zip(S_list,s1_list):
    s2_list.append(i)

print(s2_list)


s3_list=[("skd",1),("dkkf",2),("hgjf",3),("dmfkld",4)]
nam,he=zip(*s3_list)
print(nam)
print(he)

for i,j in enumerate(S_list):
    print("{} {}".format(i,j))


