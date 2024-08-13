# Bacterial-Evolution-Simulation
Bacterial Evolution Simulation models the behavior and evolution of bacteria under pressure and temperature constraints. Users define initial conditions, and bacteria consume food, reproduce, and adapt over generations. The simulation visualizes population growth and evolving resistances using Pygame, with results plotted using Matplotlib.

# Key Features:
User-Defined Parameters:

The simulation begins with user inputs for critical parameters such as pressure and temperature constraints, initial bacterial population size, initial resistance to pressure and temperature, and the maximum food spawn rate. These inputs are gathered using a simple Tkinter interface.
Bacterial Behavior:

Each bacterium is represented as a circle on the screen and is initialized with attributes such as health, food consumption, heat resistance, and pressure resistance.
Bacteria move towards the nearest food source, and upon reaching it, they consume the food to regain health. If a bacterium's health drops below a threshold or it consumes a sufficient amount of food, it will either die or reproduce, respectively.
Reproduction is modeled to introduce slight variations in the offspring's resistance to heat and pressure, simulating natural selection and mutation.
Environment Simulation:

The simulation includes food spawning at random intervals and locations within the screen, ensuring that the bacteria must constantly search for food to survive and reproduce.
The environment also exerts pressure on the bacteria in the form of heat and pressure constraints, which slowly deplete their health if their resistances are inadequate.
Real-Time Visualization:

The simulation runs in real-time using Pygame, allowing users to watch as bacteria move, consume food, reproduce, and die. The bacteria's color changes according to their generation, representing evolutionary progress.
Data Collection and Visualization:

Throughout the simulation, data is collected on the population size, average heat resistance, and average pressure resistance over time.
After the simulation ends, Matplotlib is used to generate plots showing the population growth and the evolution of heat and pressure resistance, providing insights into how the bacteria adapted to their environment.

# Bacterial Evolution Image:
<img width="1412" alt="image" src="https://github.com/user-attachments/assets/19ca5f34-1802-42e1-b8a5-88fdb18a75fa">

# Learning Outcomes:
This project demonstrates key concepts in evolutionary biology, such as natural selection, mutation, and survival of the fittest, in a controlled digital environment. It also provides practical experience with Python programming, including the use of libraries like Pygame, Tkinter, and Matplotlib, and concepts such as object-oriented programming, simulation modeling, and data visualization.

The Bacterial Evolution Simulation is not only an educational tool but also a fascinating project for exploring how simple rules and environmental pressures can lead to complex behaviors and evolutionary patterns over time.
