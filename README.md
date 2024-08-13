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

In the Bacterial Evolution Simulation, the color of each bacterium changes over time to visually represent its generational progression. This change in color is directly tied to the generation number of the bacterium, with different colors indicating the evolution and adaptation of the bacteria through successive generations.

# How the Color Changes Work:
# Hue-Based Color Representation:

The color of a bacterium is determined using the HLS (Hue, Lightness, Saturation) color model, where the hue component is tied to the generation number. As bacteria reproduce and form new generations, their hue value changes incrementally.
Specifically, the hue is calculated as the ratio of the bacterium's generation number to a predefined maximum number of generations (e.g., 100). This hue value is then converted to an RGB color that is visually distinct from the colors of previous generations.
Visualizing Evolution:

Early generations might be represented by colors like red or orange, while later generations could shift towards green, blue, or purple, depending on the hue calculation.
As bacteria evolve and reproduce, the shift in color provides a visual cue to observers, making it easy to identify which bacteria are more evolved and have adapted better to the environment.
Significance of Color Change:

The changing colors serve as a visual representation of natural selection at work. As the simulation progresses, observers can see which bacteria survive and reproduce, leading to a population that visually evolves over time.
This color shift also highlights the genetic diversity within the bacterial population, showing how certain traits (like heat and pressure resistance) may become more prevalent as bacteria with advantageous traits reproduce more successfully.
In summary, the color change of the bacteria over time is a way to visually track the evolutionary progress of the population, allowing users to see the generational shift and adaptation to environmental challenges in real-time.

# Initial Bacterial Evolution:
<img width="1412" alt="image" src="https://github.com/user-attachments/assets/19ca5f34-1802-42e1-b8a5-88fdb18a75fa">

# Color Change in Bacteria i.e After a Few Evolutions:
<img width="1415" alt="image" src="https://github.com/user-attachments/assets/fa828eca-9aa6-4459-9190-9d575090c0ac">


# Learning Outcomes:
This project demonstrates key concepts in evolutionary biology, such as natural selection, mutation, and survival of the fittest, in a controlled digital environment. It also provides practical experience with Python programming, including the use of libraries like Pygame, Tkinter, and Matplotlib, and concepts such as object-oriented programming, simulation modeling, and data visualization.

The Bacterial Evolution Simulation is not only an educational tool but also a fascinating project for exploring how simple rules and environmental pressures can lead to complex behaviors and evolutionary patterns over time.
