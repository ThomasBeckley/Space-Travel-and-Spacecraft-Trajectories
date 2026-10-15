
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --------------------------------------------------
# 1. DEFINE CONSTANTS
# --------------------------------------------------

# Earth constants
G = 6.67430e-11       # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24          # Mass of Earth (kg)
R = 6.371e6           # Radius of Earth (m)

# Rocket parameters (example values)
m = 2000             # Mass of rocket without fuel (kg)
k = 12000              # Initial fuel mass (kg)
r = 50                # Fuel consumption rate (kg/s)
F = 180000            # Constant thrust (N)

# Time taken to burn all fuel
t_burn = k / r


# --------------------------------------------------
# 2. DEFINE DIFFERENTIAL EQUATIONS
# --------------------------------------------------

def rocket_equations(t, y):

    # Current height and velocity
    h, v = y

    # Rocket mass decreases as fuel burns
    mass = m + k - r*t

    # Acceleration = thrust acceleration - gravity
    a = F/mass - G*M/(R+h)**2

    # Return derivatives of height and velocity
    return [v, a]


# --------------------------------------------------
# 3. SOLVE USING RUNGE-KUTTA (RK45)
# --------------------------------------------------

solution = solve_ivp(
    fun=rocket_equations,
    t_span=(0, t_burn),
    y0=[0, 0],
    method="RK45",
    rtol=1e-9,
    atol=1e-11,
    dense_output=True
)

if not solution.success:
    raise RuntimeError(solution.message)


# --------------------------------------------------
# 4. EXTRACT RESULTS
# --------------------------------------------------

# Evaluate solution at 1000 equally spaced times
time = np.linspace(0, t_burn, 1000)

height, velocity = solution.sol(time)

# Final height and velocity
final_height = height[-1]
final_velocity = velocity[-1]

print(f"Time until fuel runs out: {t_burn:.2f} s")
print(f"Height at burnout: {final_height:.2f} m")
print(f"Height at burnout: {final_height/1000:.2f} km")
print(f"Velocity at burnout: {final_velocity:.2f} m/s")


# --------------------------------------------------
# 5. PLOT HEIGHT AGAINST TIME
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(time, height/1000, label="Rocket height")

plt.xlabel("Time (seconds)")
plt.ylabel("Height above Earth's surface (km)")
plt.title("Rocket Height During Powered Flight")

plt.grid(True)
plt.legend()
plt.show()


# --------------------------------------------------
# 6. PLOT VELOCITY AGAINST TIME
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(time, velocity, label="Rocket velocity")

plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.title("Rocket Velocity During Powered Flight")

plt.grid(True)
plt.legend()
plt.show()
