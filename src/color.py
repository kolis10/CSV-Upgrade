colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]

for i, color in enumerate(colors):
    ratio = ratios[i]
    print("{}% {}".format(ratio * 100, color))

lst = ['A','B','C','D']
print({k: v for v, k in enumerate(lst)})

dictionary = dict(zip(colors, ratios))
print(dictionary)

for i in colors:
    p = i
    print(dict(i = ratios[p]))
