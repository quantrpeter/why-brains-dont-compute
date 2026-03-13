# Lesson 7: Learning Empirically

Game-playing provides a striking vindication of empirical learning. From Rubik's Cube (algorithmic) to chess and Go (empirical), the contrast reveals when trial-and-error succeeds—with implications for neuroscience.

## Key Concepts

### Game Tree Complexity
Rubik's Cube has ~10¹⁹ states and can be solved by a simple algorithm in about 20 moves. Tic-tac-toe (~10⁴), checkers (~10²⁰), chess (~10¹²⁰), and Go (~10³²⁰) grow exponentially. Beyond a threshold, exhaustive or rule-based search becomes impossible. Games that cannot be "solved" algorithmically must be mastered empirically.

### Deep Blue vs AlphaZero
Deep Blue beat Kasparov using brute-force search combined with expert-crafted evaluation functions. AlphaGo and AlphaZero, by contrast, learned entirely through self-play reinforcement learning—no human move databases, no hand-crafted heuristics. AlphaZero surpassed AlphaGo by learning from scratch in hours. The lesson: in sufficiently complex domains, empirical learning outperforms algorithmic design.

### Implications for Neuroscience
Real-life search spaces—perception, motor control, language, social behavior—dwarf even Go. Brains cannot compute optimal solutions; they must operate empirically. The success of AlphaZero and similar systems suggests that biological intelligence, too, relies on trial-and-error refinement rather than logical computation.

## Discussion Questions

1. What distinguishes games that can be solved algorithmically from those that require empirical learning?
2. Why did AlphaZero succeed without any human game knowledge, while Deep Blue relied on expert input?
3. How might the lessons from game-playing AI inform our understanding of how brains learn and perceive?

## Further Readings

- Silver D et al (2017) Mastering the game of Go without human knowledge. *Nature*
- Purves D (2019) What does AI's success playing complex board games tell brain scientists? *PNAS*
- Saxe A et al (2021) If deep learning is the answer, what is the question? *Neuroscience*

## What's Next

[Lesson 8: What We Perceive](../../lesson%208/code/) — Challenging the assumption that perception constructs representations of physical reality.
