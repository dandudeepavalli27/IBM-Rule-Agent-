# SESSION 18 – Rule-Based Agent

# Step 1: Input values
obstacle = True   # obstacle detected
speed = 5         # current speed

# Step 2: Apply rule
if obstacle and speed > 0:
    print("Stop Action Executed")
else:
    print("Continue Moving")

print("\nProgram Executed Successfully")
