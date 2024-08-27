import matplotlib.pyplot as plt
import itertools as it
import pomegranate as pom
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

# Define variable names
F = 'Fraud'
T = 'Travel'
OD = 'OwnsDevice'
FP = 'ForeignPurchase'
OP = 'OnlinePurchase'

# Define probability distributions
travel_distribution = pom.DiscreteDistribution({False: 0.05, True: 0.95})
foreign_purchase_distribution = pom.ConditionalProbabilityTable(
    [
        [False, False, 0.99],
        [False, True, 0.01],
        [True, False, 0.12],
        [True, True, 0.88]
    ],
    [travel_distribution])
owns_device_distribution = pom.DiscreteDistribution({False: 0.3, True: 0.7})
online_purchase_distribution = pom.ConditionalProbabilityTable(
    [
        [False, False, 0.95],
        [False, True, 0.05],
        [True, False, 0.60],
        [True, True, 0.40]
    ],
    [owns_device_distribution])
fraud_distribution = pom.ConditionalProbabilityTable(
    [
        [False, False, False, 0.25],
        [False, True, False, 0.15],
        [True, False, False, 0.20],
        [True, True, False, 0.005],
        [False, False, True, 0.75],
        [False, True, True, 0.85],
        [True, False, True, 0.80],
        [True, True, True, 0.995]
    ],
    [online_purchase_distribution, foreign_purchase_distribution])

# Create nodes for Bayesian network
foreign_purchase = pom.Node(foreign_purchase_distribution, name=FP)
online_purchase = pom.Node(online_purchase_distribution, name=OP)
fraud = pom.Node(fraud_distribution, name=F)
owns_device = pom.Node(owns_device_distribution, name=OD)
travel = pom.Node(travel_distribution, name=T)

# Build the Bayesian network
model = pom.BayesianNetwork("Fraud Detection")
model.add_states(fraud, owns_device, travel, foreign_purchase, online_purchase)
model.add_edge(travel, foreign_purchase)
model.add_edge(owns_device, online_purchase)
model.add_edge(foreign_purchase, fraud)
model.add_edge(online_purchase, fraud)
model.bake()

# Function to plot the Bayesian network and save it as an image
def plot_and_save(model, filename):
    G = nx.DiGraph()
    for state in model.states:
        G.add_node(state.name)
    for parent, child in model.edges:
        G.add_edge(parent.name, child.name)
    
    plt.figure(figsize=(10, 7))
    pos = graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=True, arrows=True, font_weight='bold', node_size=2000, node_color='skyblue', edge_color='gray', linewidths=2)
    plt.savefig(filename)  # Save the plot as an image
    plt.show()

# Part 1: Model plot and conditional probability tables
plot_and_save(model, "output.png")

# Part 2: Gibbs Sampling
N = 10000

# No evidence
predictions = model._gibbs(n=N, evidences=[{}])
prob_no_owns_device = len(list(filter(lambda x: x[0], predictions))) / N

# Evidence: OwnsDevice = True
predictions = model._gibbs(n=N, evidences=[{OD: True}])
prob_owns_device = len(list(filter(lambda x: x[0], predictions))) / N

# Evidence: OwnsDevice = True, Travel = True
predictions = model._gibbs(n=N, evidences=[{OD: True, T: True}])
prob_owns_device_and_travel = len(list(filter(lambda x: x[0], predictions))) / N

print("Inference through Gibbs sampling:\n")
print("Probability of Fraud with no evidence:", prob_no_owns_device)
print("Probability of Fraud with evidence that the person owns a device:", prob_owns_device)
print("Probability of Fraud with evidence that the person owns a device and travels:", prob_owns_device_and_travel)

# Part 3: Variable Elimination to find probabilities under different evidences

# No evidence
no_evidence = model.predict_proba({})
prob_fraud_no_evidence = no_evidence[model.states.index(fraud)].parameters[0][True]

# Evidence: OwnsDevice = True
evidence_owns_device = {OD: True}
prob_fraud_owns_device = model.predict_proba(evidence_owns_device)[model.states.index(fraud)].parameters[0][True]

# Evidence: OwnsDevice = True, Travel = True
evidence_owns_device_and_travels = {OD: True, T: True}
prob_fraud_owns_device_and_travels = model.predict_proba(evidence_owns_device_and_travels)[model.states.index(fraud)].parameters[0][True]

print("\nInference through Variable Elimination method:")
print("\nProbability of Fraud with no evidence:", prob_fraud_no_evidence)
print("Probability of Fraud with evidence that the person owns a device:", prob_fraud_owns_device)
print("Probability of Fraud with evidence that the person owns a device and travels:", prob_fraud_owns_device_and_travels)
