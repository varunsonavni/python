

isTrue = False
#  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Hurdle 4!!
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def movement():
    turn_left()
    move()
    if wall_on_right():
        move()
    
while not at_goal():
    if front_is_clear() and not right_is_clear():
        move()
    elif wall_in_front() and not right_is_clear():
        movement()
    elif right_is_clear():
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()

        

    

 