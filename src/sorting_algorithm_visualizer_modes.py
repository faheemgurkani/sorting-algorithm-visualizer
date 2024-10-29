import matplotlib
matplotlib.use('TkAgg')  # Using 'TkAgg' backend to open a separate window
import matplotlib.animation as animation
from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import random
from matplotlib.patches import Patch

from sorting_algorithms import SortingAlgorithms



class SortingVisualizerLightMode:

    def __init__(self, array_size=15, value_range=(1, 100), algorithm='selection_sort'):
        """Initialize the sorting visualizer with a given array size and value range."""
        self.array_size = array_size
        self.value_range = value_range
        self.algorithm = algorithm
        self.unordered_list = self.generate_random_list()
        # self.arr_states = list(self.selection_sort(self.unordered_list.copy()))
        self.algorithms = SortingAlgorithms()  # Create an instance of SortingAlgorithms
        self.arr_states = list(self.execute_sorting_algorithm(self.unordered_list.copy()))
        self.fig, self.ax, self.bars = self.initial_plot(self.unordered_list)
        self.ani = None
        self.create_animation()

    def generate_random_list(self):
        """Generate a random list of integers."""

        return [random.randint(self.value_range[0], self.value_range[1]) for _ in range(self.array_size)]

    def execute_sorting_algorithm(self, arr):
        """Execute the sorting algorithm specified and yield states for visualization."""
        # Using getattr to dynamically get the sorting method by name
        sorting_method = getattr(self.algorithms, self.algorithm, None)

        if sorting_method:
            return sorting_method(arr)  # Return generator for the selected sorting algorithm
        else:
            raise ValueError(f"Sorting algorithm '{self.algorithm}' is not defined.")

    # def selection_sort(self, arr):
    #     """Selection Sort Algorithm with animation yields."""
    #     n = len(arr)

    #     for i in range(n):
    #         min_index = i
        
    #         for j in range(i + 1, n):
        
    #             if arr[j] < arr[min_index]:
    #                 min_index = j
        
    #         # Swapping the elements
    #         arr[i], arr[min_index] = arr[min_index], arr[i]
        
    #         yield arr.copy(), i, min_index

    def initial_plot(self, arr):
        """Initialize the plot with dark mode settings."""
        fig, ax = plt.subplots()
        
        ax.set_title(f"Sorting Visualization for: {self.algorithm}", loc='left')
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        ax.set_xlim(-0.5, len(arr) - 0.5)  # Centering the bars
        ax.set_ylim(0, max(arr) + 10)

        # Creating bars with initial array values
        bar_positions = range(len(arr))
        bars = ax.bar(bar_positions, arr, color="cyan") 
        ax.tick_params()

        # Creating custom legend handles
        legend_handles = [
            Patch(color="yellow", label="Current Index"),
            Patch(color="green", label="Minimum Index")
        ]
        ax.legend(handles=legend_handles, loc="upper left", facecolor="white", framealpha=0.8)

        return fig, ax, bars

    def update_plot(self, frame):
        """Update the plot with the current state."""
        arr_data, current_index, min_index = self.arr_states[frame]

        for i, (bar, val) in enumerate(zip(self.bars, arr_data)):
            # Set bar colors based on current index and min index
            bar.set_color("yellow" if i == current_index else "green" if i == min_index else "cyan")
            bar.set_height(val)
        
        return self.bars

    def create_animation(self):
        """Create the animation for the sorting process."""
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update_plot,
            frames=len(self.arr_states),
            interval=500,
            repeat=False
        )

        # Creating a "Reset" button
        ax_button = plt.axes([0.8, 0.9, 0.1, 0.05])  # Position [left, bottom, width, height]
        button = Button(ax_button, 'Reset', color='white', hovercolor='lightgray')
        button.label.set_color('black')  # Text color
        button.on_clicked(self.restart_animation)

        plt.show()

    def restart_animation(self, event):
        """Restart the animation when the button is clicked."""
        self.unordered_list = self.generate_random_list()
        self.arr_states = list(self.selection_sort(self.unordered_list.copy()))

        # Restarting the animation with the new list
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update_plot,
            frames=len(self.arr_states),
            interval=500,
            repeat=False
        )

        plt.draw()  # Update the figure

class SortingVisualizerDarkMode:

    def __init__(self, array_size=15, value_range=(1, 100), algorithm='selection_sort'):
        """Initialize the sorting visualizer with a given array size and value range."""
        self.array_size = array_size
        self.value_range = value_range
        self.algorithm = algorithm
        self.unordered_list = self.generate_random_list()
        # self.arr_states = list(self.selection_sort(self.unordered_list.copy()))
        self.algorithms = SortingAlgorithms()  # Create an instance of SortingAlgorithms
        self.arr_states = list(self.execute_sorting_algorithm(self.unordered_list.copy()))
        self.fig, self.ax, self.bars = self.initial_plot(self.unordered_list)
        self.ani = None
        self.create_animation()

    def generate_random_list(self):
        """Generate a random list of integers."""

        return [random.randint(self.value_range[0], self.value_range[1]) for _ in range(self.array_size)]

    def execute_sorting_algorithm(self, arr):
        """Execute the sorting algorithm specified and yield states for visualization."""
        # Using getattr to dynamically get the sorting method by name
        sorting_method = getattr(self.algorithms, self.algorithm, None)

        if sorting_method:
            return sorting_method(arr)  # Return generator for the selected sorting algorithm
        else:
            raise ValueError(f"Sorting algorithm '{self.algorithm}' is not defined.")
        
    # def selection_sort(self, arr):
    #     """Selection Sort Algorithm with animation yields."""
    #     n = len(arr)

    #     for i in range(n):
    #         min_index = i
        
    #         for j in range(i + 1, n):
        
    #             if arr[j] < arr[min_index]:
    #                 min_index = j
        
    #         # Swapping the elements
    #         arr[i], arr[min_index] = arr[min_index], arr[i]
        
    #         yield arr.copy(), i, min_index

    def initial_plot(self, arr):
        """Initialize the plot with dark mode settings."""
        plt.style.use("dark_background")  # Enabling dark mode

        fig, ax = plt.subplots()
        
        ax.set_title(f"Sorting Visualization for: {self.algorithm}", color="white", loc='left')
        ax.set_xlabel("Index", color="white")
        ax.set_ylabel("Value", color="white")
        ax.set_xlim(-0.5, len(arr) - 0.5)  # Centering the bars
        ax.set_ylim(0, max(arr) + 10)

        # Creating bars with initial array values
        bar_positions = range(len(arr))
        bars = ax.bar(bar_positions, arr, color="cyan") 
        ax.tick_params(colors="white")

        # Creating custom legend handles
        legend_handles = [
            Patch(color="white", label="Current Index"),
            Patch(color="green", label="Minimum Index")
        ]
        ax.legend(handles=legend_handles, loc="upper left", facecolor="gray", framealpha=0.8)

        return fig, ax, bars

    def update_plot(self, frame):
        """Update the plot with the current state."""
        arr_data, current_index, min_index = self.arr_states[frame]

        for i, (bar, val) in enumerate(zip(self.bars, arr_data)):
            # Set bar colors based on current index and min index
            bar.set_color("white" if i == current_index else "green" if i == min_index else "cyan")
            bar.set_height(val)
        
        return self.bars

    def create_animation(self):
        """Create the animation for the sorting process."""
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update_plot,
            frames=len(self.arr_states),
            interval=500,
            repeat=False
        )

        # Creating a "Reset" button
        ax_button = plt.axes([0.8, 0.9, 0.1, 0.05])  # Position [left, bottom, width, height]
        button = Button(ax_button, 'Reset', color='gray', hovercolor='lightgray')
        button.label.set_color('white')  # Text color
        button.on_clicked(self.restart_animation)

        plt.show()

    def restart_animation(self, event):
        """Restart the animation when the button is clicked."""
        self.unordered_list = self.generate_random_list()
        self.arr_states = list(self.selection_sort(self.unordered_list.copy()))

        # Restarting the animation with the new list
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update_plot,
            frames=len(self.arr_states),
            interval=500,
            repeat=False
        )

        plt.draw()  # Update the figure
    
