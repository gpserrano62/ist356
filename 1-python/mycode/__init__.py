print("Hello from mycode!")

person = "mike"

def say_hi(name:str) -> None:
    print(f"Hi {name}!")

#if say_hi("Tom")
"Hi, Tom!"

def add(number:list[float])-> float:
    return sum(number)

#test add
def test_add():
    #test 1
    numbers = [1, 2, 3, 4, 5]
    result = add(numbers)  
    assert result == 15, f"Expected 15, but got {result}"

    #test 2
    numbers = [0]
    result = add(numbers)
    assert result == 0

#run your tests
if __name__ == "__main__":
    test_add()