import matplotlib.pyplot as plt

def plot_multiple(*args):
    """Calls plot function in matplotlib for each input parameter.
        Each param musst be a matrix of shape N*2
    """
    for matrix in args:
        plt.plot(matrix[:, 0], matrix[:, 1])