from controller import Robot

# Create an instance of the robot
robot = Robot()

# Define constants
MAX_SPEED = 6.28

# Set up time step based on the current world configuration
time_step = int(robot.getBasicTimeStep())

# Sensors - initialize camera and enable recognition
camera = robot.getDevice("camera")
camera.enable(time_step)
camera.recognitionEnable(time_step)

camera_width = camera.getWidth()

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

while robot.step(time_step) != -1:
    detected_objects = camera.getRecognitionObjects()
    
    print(detected_objects[0])
    
    if len(detected_objects) == 0:
        left_speed = 0.1 * MAX_SPEED
        right_speed = -0.1 * MAX_SPEED
    else:
        target_object = detected_objects[0]
        obj_position_image = target_object.getPositionOnImage()
        obj_position_real = target_object.getPosition()
        
        if obj_position_image[0] != camera_width / 2:
            if obj_position_image[0] < camera_width / 2:
                left_speed = -0.2 * MAX_SPEED
                right_speed = 0.2 * MAX_SPEED
            elif obj_position_image[0] > camera_width / 2:
                left_speed = 0.2 * MAX_SPEED
                right_speed = -0.2 * MAX_SPEED
        else:
            if obj_position_real[0] > 0.1:
                left_speed = 0.5 * MAX_SPEED
                right_speed = 0.5 * MAX_SPEED
            else:
                left_speed = 0
                right_speed = 0

    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

