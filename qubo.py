import pyqubo
from dimod import ExactSolver

def qubo(Q):
    q = {}
    for i in range(len(Q)):
        for j in range(len(Q)):
            q[(i,j)] = Q[i][j]

    x = pyqubo.Array.create('x', shape=(len(Q)), vartype='BINARY')
    H = sum(q[i,j]*x[i]*x[j] for i in range(len(Q)) for j in range(len(Q)))

    model = H.compile()
    qubo, _ = model.to_qubo()

    solver = ExactSolver()
    sampleset = solver.sample_qubo(qubo)
    sample = sampleset.first.sample

    return list(sample.values())

Q = [
    [-15,6,8,4,12],
    [0,-39,24,12,36],
    [0,0,-48,16,48],
    [0,0,0,-28,24],
    [0,0,0,0,-60]
]

print(qubo(Q))
