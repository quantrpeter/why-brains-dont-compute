# Lesson 6: Resurrection of Neural Networks

Backpropagation revived neural networks by solving the credit assignment problem. Yet backprop is biologically implausible, and in huge search spaces, empirical strategies—including evolution as supervisor—dominate.

## Key Concepts

### Backpropagation and Gradient Descent
Werbos (1974) and Rumelhart & McClelland (1986) popularized backpropagation: propagating error signals backward through the network to adjust weights via gradient descent. This enabled multi-layer networks to learn from labeled data. The algorithm works by computing how each weight contributes to the output error and updating weights to reduce that error.

### Biological Implausibility of Backprop
Backpropagation requires known correct answers (supervision) and precise specification of recurrent weight paths for error propagation. Brains have neither: they learn from reward and experience without explicit labels, and synaptic connectivity does not support the symmetric backward pass that backprop assumes. Evolution and lifetime learning must use different mechanisms—unsupervised or reward-based credit assignment.

### Search Spaces and Empirical Strategies
Small search spaces (~10¹⁰ states) can be explored algorithmically. Huge spaces (~10¹⁰⁰ or more) overwhelm exhaustive or rule-based search. Game trees for chess and Go fall in this regime. Empirical approaches—trial-and-error, genetic algorithms, reinforcement learning—succeed where algorithms fail. Brains face search spaces that dwarf board games.

## Discussion Questions

1. Why is backpropagation considered biologically implausible, and what alternatives might brains use?
2. How does evolution serve as an "unsupervised" supervisor for credit assignment?
3. At what point does search space size make algorithmic approaches impractical?

## Further Readings

- Nielsen MA (2015) How the backpropagation algorithm works. *Neural Networks and Deep Learning*
- Rumelhart DE, McClelland JL (1986) *Parallel distributed processing*. MIT Press
- Werbos P (1974) *The roots of backpropagation*. PhD thesis, Harvard University

## What's Next

[Lesson 7: Learning Empirically](../../lesson%207/code/) — From Rubik's Cube to AlphaZero; how game-playing vindicates empirical learning.
