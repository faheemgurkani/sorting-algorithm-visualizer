import matplotlib
matplotlib.use('TkAgg')  # Using 'TkAgg' backend to open a separate window
import matplotlib.animation as animation
from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import random
from matplotlib.patches import Patch

# # Although all the of the respective custom implementations are provided in this file; however the seperate modules are provided from where the custom models can be imported
# from sorting_algorithms import SortingAlgorithms
# from sorting_algorithm_visualizer_modes import SortingVisualizerDarkMode, SortingVisualizerLightMode



class SortingAlgorithms:
    """Class encapsulating various sorting algorithms for visualization."""
    
    def bubble_sort(self, arr):
        """Bubble Sort Algorithm with visualization yields."""
        n = len(arr)
        
        for i in range(n):
        
            for j in range(0, n - i - 1):
        
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swapping
        
                yield arr.copy(), j, j + 1  # Yield the current state of the array

    def selection_sort(self, arr):
        """Selection Sort Algorithm with visualization yields."""
        n = len(arr)
        
        for i in range(n):
            min_index = i
        
            for j in range(i + 1, n):
        
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Swapping
        
            yield arr.copy(), i, min_index  # Yield the current state of the array

    def insertion_sort(self, arr):
        """Insertion Sort Algorithm with visualization yields."""
        
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
        
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        
            yield arr.copy(), i, j + 1  # Yield the current state of the array

    def merge_sort(self, arr):
        """Merge Sort Algorithm with visualization yields."""
        
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            yield from self.merge_sort(left_half)
            yield from self.merge_sort(right_half)

            i = j = k = 0
        
            while i < len(left_half) and j < len(right_half):
        
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
        
                yield arr.copy(), k, -1  # Yield the current state of the array

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
        
                yield arr.copy(), k, -1  # Yield the current state of the array

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        
                yield arr.copy(), k, -1  # Yield the current state of the array

    def quick_sort(self, arr):
        """Quick Sort Algorithm with visualization yields."""
        
        if len(arr) <= 1:
            yield arr.copy(), -1, -1  # Base case yields
        
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        yield from self.quick_sort(left)
        yield middle, -1, -1  # Yield current pivot position
        yield from self.quick_sort(right)

    def heap_sort(self, arr):
        """Heap Sort Algorithm with visualization yields."""
        
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # Swapping
        
                yield from heapify(arr, n, largest)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            yield from heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swapping
        
            yield from heapify(arr, i, 0)

    def counting_sort(self, arr):
        """Counting Sort Algorithm with visualization yields."""
        max_val = max(arr)
        count = [0] * (max_val + 1)

        for num in arr:
            count[num] += 1

        sorted_index = 0
        
        for i, c in enumerate(count):
        
            for _ in range(c):
                arr[sorted_index] = i
                sorted_index += 1
        
                yield arr.copy(), sorted_index - 1, -1  # Yield the current state of the array

    def radix_sort(self, arr):
        """Radix Sort Algorithm with visualization yields."""
        
        def counting_sort_for_radix(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(n - 1, -1, -1):
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1

            for i in range(n):
                arr[i] = output[i]
        
                yield arr.copy(), i, -1  # Yield the current state of the array

        max_num = max(arr)
        exp = 1

        while max_num // exp > 0:
            yield from counting_sort_for_radix(arr, exp)
        
            exp *= 10

    def bucket_sort(self, arr):
        """Bucket Sort Algorithm with visualization yields."""
        
        if len(arr) == 0:
            return arr

        # Creating buckets
        max_value = max(arr)
        bucket_count = len(arr) // 5
        buckets = [[] for _ in range(bucket_count)]

        # Distributing input array values into buckets
        for num in arr:
            index = min(num * bucket_count // (max_value + 1), bucket_count - 1)
            buckets[index].append(num)

        # Sorting each bucket and concatenate
        sorted_arr = []

        for bucket in buckets:
            sorted_arr.extend(sorted(bucket))

        yield sorted_arr, -1, -1  

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



if __name__ == "__main__":
    pass
