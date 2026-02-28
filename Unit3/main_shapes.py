import shapes

print("choose a shapes:")
print("1.Circle")
print("2.Rectangle")
print("3.Triangle")

choice = int(input("Enter a choice(1-3)"))

if choice==1:
    r = float(input("Enter radius:"))
    area = shapes.circle_area(r)
    print("Area of circle =",area)

elif choice==2:
    l = float(input("Enter length:"))
    w = float(input("Enter width:"))
    area = Shapes.triangle_area(b,h)
    print("Area of Rectangle =", area)

elif choice==3:
    b = float(input("Enter base:"))
    h = float(input("Enter height:"))
    print("Area of Triangle =",area)            

else:
    print("Invalid Choice")