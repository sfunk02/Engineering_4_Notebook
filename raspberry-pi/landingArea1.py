# type: ignore

def triangle_area(x1, y1, x2, y2, x3, y3):
    total = (x1 * (y1 - y2) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    return abs(total)

print("Enter the first coord")
first = input()
first = first.split(",")
x1 = float(first[0])
y1 = float(first [1])
print("Enter the second coord")
second = input()
second = second.split(",")
x2 = float(second[0])
y2 = float(second [1])
print("Enter the third coord")
third = input()
third = third.split(",")
x3 = float(third[0])
y3 = float(third [1])

area = triangle_area(x1, y1, x2, y2, x3, y3)
print(f"The area of the triangle with vertices ({first[0]},{first[1]}), ({second[0]},{second[1]}), and ({third[0]},{third[1]}) is {area} square km.")