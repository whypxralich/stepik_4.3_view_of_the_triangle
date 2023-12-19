#stepik_4.3_view_of_the_triangle
a = int(input())
b = int(input())
c = int(input())

if a == b ==c:
    print ("Равносторонний")
elif (a == b or a == c or b == c) and (a != c or a != b or b != c):
    print ("Равнобедренный")
elif a != b != c != a:
    print ("Разносторонний")