import math
import turtle

class Circle:
    def __init__(self, num):
        self.num = num
        print(f"Creating circle with value {num}")
        print("choose:")
        print("1. radius")
        print("2. diameter")
        
        # Input validation
        while True:
            try:
                self.ch = int(input("===> "))
                if self.ch in [1, 2]:
                    break
                else:
                    print("Please choose 1 or 2:")
            except ValueError:
                print("Please enter a valid number (1 or 2):")
        
    def area(self):
        if self.ch == 1:
            # num is radius
            A = math.pi * (self.num**2)
            return A
        else:
            # num is diameter
            B = math.pi * ((self.num/2)**2)
            return B
    
    def radius(self):
        if self.ch == 1:
            return self.num
        else:
            return self.num / 2
        
    def __repr__(self):
        return f"Circle(radius={self.radius():.2f}, area={self.area():.2f})"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            # Create a new circle with area equal to the sum of both circles
            total_area = self.area() + other.area()
            new_radius = math.sqrt(total_area / math.pi)
            new_circle = Circle(new_radius)
            new_circle.ch = 1  # Set as radius
            return new_circle
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.area() > other.area()
        return NotImplemented
        
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.area() == other.area()
        return NotImplemented

# Create circles
circles = [Circle(30), Circle(50), Circle(40), Circle(60)]

# Sort circles by area (smallest to largest)
sorted_circles = sorted(circles)

print("Sorted circles (smallest to largest):")
for circle in sorted_circles:
    print(circle)

# Setup turtle
screen = turtle.Screen()
screen.title("Circles Side by Side")
t = turtle.Turtle()
t.speed(3)

# Starting position
start_x = -200
current_x = start_x

# Draw circles side by side
for circle in sorted_circles:
    radius = circle.radius()
    
    # Move to starting position
    t.penup()
    t.goto(current_x, -radius)
    t.pendown()
    
    # Draw circle
    t.circle(radius)
    
    # Update position for next circle
    current_x += 2 * radius + 20  # diameter + spacing

# keep window open

turtle.done()