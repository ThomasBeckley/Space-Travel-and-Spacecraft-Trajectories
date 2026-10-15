import matplotlib.pyplot as plt
import pandas as pd

# 1. Physical constants
G = 6.67430e-11       # Gravitational constant
M = 5.972e24          # Mass of Earth (kg)
R = 6.371e6           # Radius of Earth (m)

# 2. Rocket parameters (example values)
m = 1000              # Rocket dry mass (kg)
k = 500               # Initial fuel mass (kg)
r = 5                 # Fuel burn rate (kg/s)
F = 20000             # Constant thrust (N)

# 3. Initial conditions
h = 0
v = 0
t = 0

# 4. Time settings
burnout_time = k / r
dt = 5
N = round(burnout_time / dt)
dt = burnout_time / N

# 5. Lists to store results
times = [t]
heights = [h]
velocities = [v]
accelerations = []

# 6. Euler iteration
for n in range(N):

    # Calculate current acceleration
    a = F / (m + k - r*t) - G*M / (R + h)**2

    # Store current acceleration
    accelerations.append(a)

    # Update height FIRST, then velocity
    h = h + v*dt
    v = v + a*dt
    t = (n + 1)*dt

    # Store updated values
    times.append(t)
    heights.append(h)
    velocities.append(v)

# Calculate acceleration at burnout
a = F/m - G*M/(R + h)**2
accelerations.append(a)

# 7. Create table using pandas
table = pd.DataFrame({
    "Time (s)": times,
    "Height (m)": heights,
    "Velocity (m/s)": velocities,
    "Acceleration (m/s²)": accelerations
})

# 8. Display results
print(table.to_string(index=False, float_format="%.2f"))

print("\nFuel runs out after:", burnout_time, "seconds")
print("Height at burnout:", round(h, 2), "metres")
print("Velocity at burnout:", round(v, 2), "m/s")
# Plot height against time
plt.plot(times, heights)

# Label the axes
plt.xlabel("Time (seconds)")
plt.ylabel("Height (metres)")

# Give the graph a title
plt.title("Rocket Height During Fuel Burn")

# Add grid lines
plt.grid(True)

# Display the graph
plt.show()
