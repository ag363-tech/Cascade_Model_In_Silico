import matplotlib
matplotlib.use("TkAgg")

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from model import three_node_system

params = {
    "k_prod_A": 1.0,
    "k_deg_A": 0.2,
    "k_deg_A_fast": 50.0,
    "t_switch": 25.0,
    "k1": 1.0,
    "k2": 1.0,
    "k_deg_B": 0.3,
    "k_deg_C": 0.1,
}

y0 = [0, 0, 0]
t_eval = np.linspace(0, 60, 1000)

params_baseline = params.copy()
params_baseline["k_deg_A_fast"] = params_baseline["k_deg_A"]

sol_baseline = solve_ivp(
    three_node_system, (0, 60), y0, t_eval=t_eval, args=(params_baseline,)
)

sol_switch = solve_ivp(
    three_node_system, (0, 60), y0, t_eval=t_eval, args=(params,)
)

plt.figure()
plt.plot(sol_baseline.t, sol_baseline.y[0], label="A")
plt.plot(sol_baseline.t, sol_baseline.y[1], label="B")
plt.plot(sol_baseline.t, sol_baseline.y[2], label="C")
plt.title("Three-node cascade")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.savefig("baseline.png", dpi=150)
plt.close()


plt.figure()
plt.plot(sol_switch.t, sol_switch.y[0], label="A")
plt.plot(sol_switch.t, sol_switch.y[1], label="B")
plt.plot(sol_switch.t, sol_switch.y[2], label="C")
plt.axvline(params["t_switch"], linestyle="--", label="A shutoff")
plt.title("Cascade with A degradation")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.savefig("switch.png", dpi=150)
plt.close()

import os

os.system("open baseline.png")
os.system("open switch.png")



