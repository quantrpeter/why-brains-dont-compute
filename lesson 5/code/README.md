# Lesson 5: Neural Networks

Artificial neural networks originated with McCulloch & Pitts and Rosenblatt's perceptrons. Their key attribute—trial-and-error learning—also led to their initial failure and the dominance of algorithmic computing.

## Key Concepts

### McCulloch & Pitts and Trial-and-Error Learning
McCulloch and Pitts (1943) showed that networks of simple threshold units could solve logical problems when connection weights were modifiable. The key insight: learning could occur by trial-and-error, rewarded by success, without needing to know the answer in advance. This contrasted sharply with algorithmic approaches that require explicit rules.

### The Credit Assignment Problem
For a network to learn, it must know which connections to adjust when the output is wrong. The "credit assignment" problem: how to distribute feedback across many layers and connections. Without a solution, multi-layer networks could not learn from experience. This limitation stalled neural network research for decades.

### Perceptrons and the XOR Limitation
Rosenblatt's perceptron was a two-layer classifier that could learn linearly separable patterns. Minsky and Papert (1969) proved that perceptrons cannot solve XOR—a simple non-linear problem. Their critique, combined with the credit assignment challenge and the dominance of symbolic AI, led to the "first AI winter" for neural networks.

## Discussion Questions

1. Why is the credit assignment problem so central to understanding both artificial and biological neural networks?
2. How does the XOR limitation of perceptrons relate to the need for hidden layers?
3. What might the initial failure of neural networks tell us about the relationship between brains and computers?

## Further Readings

- McCulloch WS, Pitts W (1943) A logical calculus of the ideas immanent in nervous activity. *Bulletin of Mathematical Biophysics*
- Minsky M, Papert S (1972) *Perceptrons*. MIT Press
- Russell S, Norvig P (2003) *Artificial intelligence: a modern approach*. Pearson

## What's Next

[Lesson 6: Resurrection of Neural Networks](../../lesson%206/code/) — Backpropagation, gradient descent, and why empirical strategies dominate in huge search spaces.
