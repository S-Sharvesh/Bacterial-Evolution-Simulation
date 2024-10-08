import pygame
import random
import math
import colorsys
import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt

def get_user_inputs():
    root = tk.Tk()
    root.withdraw()
    pressure_constraint = simpledialog.askinteger("Input", "Please enter desired pressure constraint (1-100): ")
    heat_constraint = simpledialog.askinteger("Input", "Please enter your desired temperature constraint: ")
    bacteria_initial_population = simpledialog.askinteger("Input", "Please enter your desired initial bacterial population: ")
    initial_pressure_resistance = simpledialog.askinteger("Input", "Please enter your desired initial pressure resistance: ")
    initial_temperature_resistance = simpledialog.askinteger("Input", "Please enter your desired initial temperature resistance: ")
    maximum_food_spawn = simpledialog.askinteger("Input", "Please enter maximum food spawn rate (1-100): ")
    root.destroy()
    return (pressure_constraint, heat_constraint, bacteria_initial_population, 
            initial_pressure_resistance, initial_temperature_resistance, maximum_food_spawn)

# Get user inputs
(pressure_constraint, heat_constraint, bacteria_initial_population, 
 initial_pressure_resistance, initial_temperature_resistance, maximum_food_spawn) = get_user_inputs()

# Initialize pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define the size of the screen
SCREEN_WIDTH = pygame.display.Info().current_w - 30
SCREEN_HEIGHT = pygame.display.Info().current_h - 50

# Define the size of the bacteria and food
BACTERIA_SIZE = 7
FOOD_SIZE = 5

# Create a screen object with a border
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the title of the screen
pygame.display.set_caption("Bacteria and Food Simulation")

# Create a clock object to track time
clock = pygame.time.Clock()

# Create a list to store bacteria objects
bacteria_list = []

# Create a list to store food objects
food_list = []

# Food spawning parameters
FOOD_SPAWN_RATE = 2  # Food spawns every 2 seconds

# Bacteria reproduction parameters
REPRODUCTION_THRESHOLD = 5  # Bacteria need to eat this many food items to reproduce

class Bacteria:
    def __init__(self, x, y, generation, heat_resistance, pressure_resistance):
        self.x = x
        self.y = y
        self.generation = generation
        self.heat_resistance = heat_resistance
        self.pressure_resistance = pressure_resistance
        self.health = 100
        self.food_eaten = 0
        self.velocity = 5
        self.screen = screen
        self.radius = BACTERIA_SIZE
        self.color = self.get_color()

    def get_color(self):
        num_generations = 100
        hue = self.generation / num_generations
        saturation = 1.0
        lightness = 0.5
        rgb_color = colorsys.hls_to_rgb(hue, lightness, saturation)
        rgb_color = [int(val * 255) for val in rgb_color]
        return rgb_color

    def move_towards_nearest_food(self):
        if not self.is_dead() and food_list and self.health < 85:
            nearest_food = min(food_list, key=lambda f: math.sqrt((self.x - f.x) ** 2 + (self.y - f.y) ** 2), default=None)
            if nearest_food:
                angle = math.atan2(nearest_food.y - self.y, nearest_food.x - self.x)
                self.x += self.velocity * math.cos(angle)
                self.y += self.velocity * math.sin(angle)

                distance_to_food = math.sqrt((self.x - nearest_food.x) ** 2 + (self.y - nearest_food.y) ** 2)
                if distance_to_food <= self.radius:
                    self.eat_food(nearest_food)

    def reproduce(self):
        if self.health > 75 and self.food_eaten >= REPRODUCTION_THRESHOLD:
            child1 = Bacteria(self.x + random.randint(-1, 1), self.y, self.generation + 1,
                              self.heat_resistance + random.uniform(0, 1),
                              self.pressure_resistance + random.uniform(0, 1))
            child2 = Bacteria(self.x, self.y + random.randint(-1, 1), self.generation + 1,
                              self.heat_resistance + random.uniform(0, 1),
                              self.pressure_resistance + random.uniform(0, 1))
            bacteria_list.append(child1)
            bacteria_list.append(child2)
            self.die()
            return child1, child2
        return None

    def depleteHealth(self, heat_constraint, pressure_constraint):
        self.health -= 0.5
        heat_depletion = (self.heat_resistance - heat_constraint) / 10
        pressure_depletion = (self.pressure_resistance - pressure_constraint) / 10
        self.health += min(0, heat_depletion + pressure_depletion)

    def update(self):
        self.depleteHealth(heat_constraint, pressure_constraint)
        self.move_towards_nearest_food()
        self.draw(self.x, self.y)
        if self.is_dead():
            self.die()
        if self.reproduce():
            print("Reproduced")

    def eat_food(self, food):
        self.health = min(100, self.health + 20)
        self.food_eaten += 1
        food_list.remove(food)

    def die(self):
        if self.is_dead():
            food_produced = self.food_eaten // 4
            bacteria_list.remove(self)
            for _ in range(food_produced):
                _food_ = Food(self.x + random.randint(-2, 2), self.y + random.randint(-2, 2), color=self.color)
                _food_.draw()
                food_list.append(_food_)

    def is_dead(self):
        return self.health <= 0

    def draw(self, x, y):
        pygame.draw.circle(self.screen, self.color, (int(x), int(y)), self.radius)

class Food:
    def __init__(self, x=None, y=None, color=None):
        self.x = x if x is not None else random.randint(FOOD_SIZE // 2, SCREEN_WIDTH - FOOD_SIZE // 2)
        self.y = y if y is not None else random.randint(FOOD_SIZE // 2, SCREEN_HEIGHT - FOOD_SIZE // 2)
        self.color = color if color is not None else GREEN

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), FOOD_SIZE // 2)

def spawn_food():
    for _ in range(random.randint(1, maximum_food_spawn)):
        food = Food()
        food_list.append(food)

# Create the initial population of bacteria
for _ in range(bacteria_initial_population):
    bacteria = Bacteria(random.randint(BACTERIA_SIZE // 2, SCREEN_WIDTH - BACTERIA_SIZE // 2),
                        random.randint(BACTERIA_SIZE // 2, SCREEN_HEIGHT - BACTERIA_SIZE // 2),
                        1, initial_temperature_resistance, initial_pressure_resistance)
    bacteria_list.append(bacteria)

running = True
food_spawn_timer = 0

time_data = []
population_data = []
heat_resistance_data = []
pressure_resistance_data = []

# Create a variable to track the simulation state
simulation_running = True

while simulation_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulation_running = False

    # Update and draw bacteria
    screen.fill((169, 169, 169))
    for bacteria in bacteria_list:
        bacteria.update()

    # Update and draw food
    for food in food_list:
        food.draw()

    pygame.display.flip()
    clock.tick(24)

    # Spawn food at random intervals
    food_spawn_timer += clock.get_time() / 1000
    if food_spawn_timer >= random.uniform(0.1, 1):  # Randomize food spawn time
        spawn_food()
        food_spawn_timer = 0

    # Collect data during the simulation
    current_time = pygame.time.get_ticks() / 1000
    current_population = len(bacteria_list)
    heat_resistances = [bacteria.heat_resistance for bacteria in bacteria_list]
    pressure_resistances = [bacteria.pressure_resistance for bacteria in bacteria_list]

    time_data.append(current_time)
    population_data.append(current_population)
    heat_resistance_data.append(sum(heat_resistances) / max(len(heat_resistances), 1))
    pressure_resistance_data.append(sum(pressure_resistances) / max(len(pressure_resistances), 1))

# Quit pygame
pygame.quit()

# Now generate Matplotlib plots after the Pygame simulation
plt.figure(figsize=(12, 6))

# Plot population growth over time
plt.subplot(2, 1, 1)
plt.plot(time_data, population_data, label="Population")
plt.xlabel("Time (seconds)")
plt.ylabel("Population")
plt.title("Population Growth Over Time")
plt.grid(True)
plt.legend()

# Plot average heat and pressure resistance over time
plt.subplot(2, 1, 2)
plt.plot(time_data, heat_resistance_data, label="Heat Resistance", color="red")
plt.plot(time_data, pressure_resistance_data, label="Pressure Resistance", color="blue")
plt.xlabel("Time (seconds)")
plt.ylabel("Resistance")
plt.title("Average Heat and Pressure Resistance Over Time")
plt.grid(True)
plt.legend()

plt.tight_layout()

# Display the Matplotlib plots
plt.show()
