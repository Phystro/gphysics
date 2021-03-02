### Infinite Square Well

import numpy as np
import matplotlib.pyplot as plt

PI = np.pi
QPNc = 3        # Quantum Principle Number counter

class InfiniteSquareWell:
    def __init__(self):
        """Solution graphs to the One Dimensional infinite square well""" 
        bins = 1000 # the number of evaulation points
        self.l = 2 * PI
        self.nrows = QPNc
        self.ncols = QPNc
        self.space = np.linspace(0, self.l, bins)
        self.normalization = np.sqrt(2/self.l)
        rn = 0      # row counter

        # Draws probability amplitude graph
        for i in range(QPNc):
            cn = 0
            qpn = i + 1     # quantum principle number
            lbl = "$\Psi_{(n=%d)}(x)$"%qpn
            data = [ self.prob_amp(qpn, x) for x in self.space ]
            self.plot_graph(data, rn, cn, lbl)
            rn+=1

        # Draws probability distribution graph
        for i in range(QPNc):
            cn = 1
            qpn = i + 1 # quantum principle number
            lbl = "$|\Psi_{(n=%d)}(x)|^2$"%qpn
            data = [ self.prob_dist(qpn, x) for x in self.space ]
            self.plot_graph(data, i, cn, lbl)
                
        plt.show()

    def prob_amp(self, n, x):
        return self.normalization * np.sin(n * PI * x/self.l)

    def prob_dist(self, n, x):
        return (self.normalization**2) * (np.sin(n * PI * x/self.l)**2)


    def plot_graph(self, data, rn, cn, ylbl):
        gr = plt.subplot2grid( (self.nrows, self.ncols), (rn, cn), rowspan=1, colspan=1 )
        gr.plot(self.space, data, linewidth=0.5, label=ylbl)
        gr.legend()
        plt.title(ylbl)
        plt.xlabel("x values")
        plt.ylabel(ylbl)
        plt.grid()

InfiniteSquareWell()

