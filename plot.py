from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def plot(results):
    labels = {}
    for nonce in results:
        nonce_base_10 = int(nonce, 2)
        labels[str(nonce_base_10)] = results[nonce]

    plot_histogram(labels, (20,20))
    plt.show()