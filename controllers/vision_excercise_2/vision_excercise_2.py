from controller import Robot

# Initialize robot and devices
robot = Robot()
MAX_SPEED = 6.28
time_interval = int(robot.getBasicTimeStep())
camera_sensor = robot.getDevice("camera")
camera_sensor.enable(time_interval)
camera_sensor.recognitionEnable(time_interval)
frame_width = camera_sensor.getWidth()
left_wheel = robot.getDevice('left wheel motor')
right_wheel = robot.getDevice('right wheel motor')
left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))
left_wheel.setVelocity(0.0)
right_wheel.setVelocity(0.0)

# hyper parameters
TARGET_COLOR = [0.8, 0.5, 0.5] # we may set this for any other color, but to make sure the threshold is correctly written and validated as well!
COLOR_THRESHOLD = 10  # pixels

while robot.step(time_interval) != -1:
    _ = camera_sensor.getImage()  # Triggering camera updates with real-time images...
    objects_in_view = camera_sensor.getRecognitionObjects()
    matched_object = None

    for entity in objects_in_view:
        r, g, b = entity.colors[:3]  # Fix: only unpack the first 3 color components
        print(f"Detected Color: R={r:.2f}, G={g:.2f}, B={b:.2f}")

        if r >= TARGET_COLOR[0] and g <= TARGET_COLOR[1] and b <= TARGET_COLOR[2]:
            matched_object = entity
            break  # First purple-like match found

    # Default movement: rotation in circle
    left_velocity = 0.5 * MAX_SPEED
    right_velocity = -0.5 * MAX_SPEED

    if not matched_object:
        print("No purple object detected — scanning...")
        left_wheel.setVelocity(left_velocity)
        right_wheel.setVelocity(right_velocity)
        continue

    print("Purple-toned object identified.")

    x_position = matched_object.getPositionOnImage()[0]
    z_distance = matched_object.getPosition()[2]
    image_center = frame_width / 2

    offset = x_position - image_center
    print(f"Relative X offset: {offset:.2f}")

    if abs(offset) > COLOR_THRESHOLD:
        turning_direction = "left" if offset < 0 else "right"
        print(f"Adjusting alignment — rotating {turning_direction}.")
        multiplier = -1 if offset < 0 else 1
        left_velocity = 0.2 * MAX_SPEED * multiplier
        right_velocity = -0.2 * MAX_SPEED * multiplier
    elif z_distance > 0.01:
        print("Target centered — approaching...")
        left_velocity = 0.5 * MAX_SPEED
        right_velocity = 0.5 * MAX_SPEED
    else:
        print("Target directly ahead — stopping.")
        left_velocity = 0
        right_velocity = 0

    left_wheel.setVelocity(left_velocity)
    right_wheel.setVelocity(right_velocity)
