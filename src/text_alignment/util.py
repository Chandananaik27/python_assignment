import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def text_alignment():
    thickness = int(input("Enter the thickness of the logo (must be an odd number): "))
    if thickness % 2 == 0:
        logging.debug("The thickness must be an odd number.")
    else:
        c = 'H'
        # Top Cone
        for i in range(thickness):
            logging.debug((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
        # Top Pillars
        for i in range(thickness + 1):
            logging.debug((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        # Middle Belt
        for i in range((thickness + 1) // 2):
            logging.debug((c * thickness * 5).center(thickness * 6))
        # Bottom Pillars
        for i in range(thickness + 1):
            logging.debug((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        # Bottom Cone
        for i in range(thickness):
            logging.debug(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).center(thickness * 6))
        Top_cone =(c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)
        Top_pillars= (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
        Middle_belt = (c * thickness * 5).center(thickness * 6)
        Bottom_pillar=(c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
        Bottom_cone=((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).center(thickness * 6)
        return Top_cone, Top_pillars,Middle_belt,Bottom_pillar,Bottom_cone