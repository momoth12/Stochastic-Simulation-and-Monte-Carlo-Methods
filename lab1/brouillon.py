import matplotlib.pyplot as plt
import numpy as np
import random

class PeebleExperiment:
    # ... (other methods and constructor remain unchanged)

    def plot_error(self, num_experiments=10):
        fig_err, ax = plt.subplots(figsize=(9, 5))

        for _ in range(num_experiments):
            self.data = []  # Reset data for each experiment
            self.C = []     # Reset throw positions for each experiment
            errors = []     # Store errors for each N

            for N in range(1, self.N + 1):
                self.add_peeble()
                estimated_pi = self.get_running_pi(N)
                error = abs(estimated_pi - math.pi)
                errors.append(error)

            color = random.choice(['k', 'b', 'y', 'r', 'chartreuse', 'magenta'])
            ax.plot(range(1, self.N + 1), errors, lw=1.5, c=color, alpha=1.0)

        ax.set_xlabel(r'$N$', fontsize=10)
        ax.set_ylabel('Error', fontsize=10)
        ax.set_title('Error vs. Number of Samples')
        plt.show()

# Example usage:
peeble_experiment = PeebleExperiment()
peeble_experiment.plot_error(num_experiments=10)
