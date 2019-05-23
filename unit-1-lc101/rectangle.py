class Rectangle:
    
    def __init__(self, length, width):
        self.length= length
        self.width = width
        
    def calc_area(self):
        area = int(self.length)* int(self.width)
        return area
    
    def calc_perimeter(self):
        perimeter = (int(self.length)*2)+(int(self.width)*2)
        return perimeter
    
    def compare(self,x):
        area1 = self.calc_area
        area2 = x.calc_area
        if area1 < area2:
            return ("I am smaller")
        
    def is_square(self):
        if self.length == self.width:
            return ("I am a square")
        
def main():
    bob = Rectangle(4,4)
    print(bob.is_square())

if __name__ == "__main__":
    main()