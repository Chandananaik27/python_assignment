def text_alignment():
    thickness = int(input("Enter the thickness of the logo (must be an odd number): "))
    if thickness % 2 == 0:
        print("The thickness must be an odd number.")
    else:
        c = 'H'
        # Top Cone
        for i in range(thickness):
            print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
        # Top Pillars
        for i in range(thickness + 1):
            print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        # Middle Belt
        for i in range((thickness + 1) // 2):
            print((c * thickness * 5).center(thickness * 6))
        # Bottom Pillars
        for i in range(thickness + 1):
            print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        # Bottom Cone
        for i in range(thickness):
            print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).center(thickness * 6))
