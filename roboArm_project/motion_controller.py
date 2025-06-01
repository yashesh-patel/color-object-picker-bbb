# motion_controller.py

def get_servo_angles_for_color(color_name):
    """
    Returns predefined servo angles for the robotic arm based on object color.
    color_name: 'red', 'green', 'yellow', or 'blue'
    Returns: list of 5 angles [base, shoulder, elbow, wrist, gripper]
    """
    positions = {
        "red":    [0, 45, 30, 60, 90],
        "green":  [45, 60, 60, 90, 45],
        "yellow": [90, 100, 135, 112, 90],
        "blue":   [135, 145, 180, 153, 135]
    }
    return positions.get(color_name.lower())

def move_robot_arm(angles):
    """
    Simulates servo movement by printing the movement commands.
    Replace this with actual servo control when using hardware.
    """
    if angles is None:
        print("Invalid color. No movement executed.")
        return

    labels = ["Base", "Shoulder", "Elbow", "Wrist", "Gripper"]
    for label, angle in zip(labels, angles):
        print(f"Moving {label} to {angle}°")
