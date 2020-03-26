class Operations:
    def add(x,y):
        return x + y
    def subtract(x,y):
        return x - y
    def multiply(x,y):
        return x * y
    def divide(x,y, error_message):
        if y == 0:
            return error_message
        else:
            return x/y

