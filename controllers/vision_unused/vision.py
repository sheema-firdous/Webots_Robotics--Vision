from controller import Robot

robot = Robot()
#pysical color appearence: Solid>children>Shape>appearence Appearance>material Material>diffusecolor
#to change the recognition color: Solid>recognitionColor>here we may select the color values that will be used for sensing this object by the robot...

# Define constants
MAX_SPEED = 6.28
PURPLE_OBJECT_ID = 61  # ID for the purple cylinder
GREEN_OBJECT_ID = 56   # ID for the green cylinder

time_step = int(robot.getBasicTimeStep())

camera = robot.getDevice("camera")
camera.enable(time_step)
camera.recognitionEnable(time_step)

# Retrieve camera width to help with object centering calculations
camera_width = camera.getWidth()

# Initialize motors and configure them for continuous rotation
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

while robot.step(time_step) != -1:
    # Retrieve all recognized objects in the camera's view
    detected_objects = camera.getRecognitionObjects()

    if len(detected_objects) == 0:
        # No objects detected, rotate to search
        left_speed = 0.1 * MAX_SPEED
        right_speed = -0.1 * MAX_SPEED
    else:
        # Initialize variable to track which object to target
        target_object = None
        
        for obj in detected_objects:
            print('Color:',obj.getColor())
            # Prioritize the purple object (ID: 54) if detected
            if obj.getId() == PURPLE_OBJECT_ID:
                target_object = obj
                break
            # If no purple object is found, target the green object (ID: 59)
            elif obj.getId() == GREEN_OBJECT_ID:
                target_object = obj
                print("")
        print("Detected Id:",obj.getId() )
        # If a target object is found (either purple or green based on priority)
        if target_object:
            obj_position_image = target_object.getPositionOnImage()
            obj_position_real = target_object.getPosition()

            # Adjust the robot's direction to center the object in view
            if obj_position_image[0] != camera_width / 2:
                if obj_position_image[0] < camera_width / 2:
                    left_speed = -0.2 * MAX_SPEED
                    right_speed = 0.2 * MAX_SPEED
                else:
                    left_speed = 0.2 * MAX_SPEED
                    right_speed = -0.2 * MAX_SPEED
            else:
                # Move forward if the object is centered but distant
                if obj_position_real[0] > 0.1:
                    left_speed = 0.5 * MAX_SPEED
                    right_speed = 0.5 * MAX_SPEED
                else:
                    # Stop if the object is close enough
                    left_speed = 0
                    right_speed = 0

    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
