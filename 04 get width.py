# Ask user for width and loop until they
# enter a number that is more than zero

error = "Please enter a number that is more than zero/n"
while True:

    try:
        width = float(input("Width: "))

        if width > 0:
            break
        else:
            print(error)

        expect ValueError:
          print(error)
    expect ValueError:
      print(error)        
