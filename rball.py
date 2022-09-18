from simulation import Simulation

def main():
    probA=0.5
    probB=0.7
    numGames=1000
    sim1 = Simulation(probA,probB,numGames)
    sim1.run()



main()