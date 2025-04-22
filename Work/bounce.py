# bounce.py
#
# Exercise 1.5
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground,
# it bounces back up to 3/5 the height it fell.
# Write a program bounce.py that prints a table showing the height of the first 10 bounces.

init_height = 60
bounce_number = 10

height = init_height
for i in range(1,bounce_number+1):
    height = height * 3 / 5
    print(i,round(height,2))
