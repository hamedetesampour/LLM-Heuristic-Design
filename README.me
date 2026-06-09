# LLM-Enabled Automated Heuristic Design (TSP Case Study)

This repository demonstrates the application of Large Language Models (LLMs) to automatically generate and improve routing heuristics for combinatorial optimization problems. 

By framing an LLM as the mutation operator within an evolutionary algorithm loop, this project explores the intersection of generative AI and operations research, applying multimodal AI concepts to spatial task planning.

## 🧮 Mathematical Framework

The optimization environment relies on a $(\mu + \lambda)$ elitist evolutionary strategy. 
Let the system be defined by a complete graph $G = (V, E)$, where $V = \{v_1, v_2, \dots, v_n\}$ represents the set of $n$ spatial coordinates. The objective is to find a permutation $\pi$ of the vertices that minimizes the total Euclidean tour length $L(\pi)$:

$$
L(\pi) = \sum_{i=1}^{n-1} d(v_{\pi(i)}, v_{\pi(i+1)}) + d(v_{\pi(n)}, v_{\pi(1)})
$$

Instead of relying on rigid, hard-coded heuristics (like a standard 2-opt swap or nearest neighbor), the mutation operation $M_{LLM}$ is dynamically governed by the LLM. 
At generation $t$, the LLM evaluates the spatial array state and proposes a structural sequence mutation $\pi_{t}'$. 

Strict elitist selection is applied to maintain monotonic convergence:

$$
\pi_{t+1} = \begin{cases} 
\pi_{t}' & \text{if } L(\pi_{t}') < L(\pi_t) \\ 
\pi_t & \text{otherwise} 
\end{cases}
$$

## 🛠️ Implementation Pipeline

1. **Environment Initialization:** `numpy` generates a reproducible 2D spatial plane mimicking standard multidimensional agent navigation grids.
2. **LLM Agent Interaction:** The Google Gemini API (`gemini-3.5-flash`) parses the mathematical coordinate arrays and incumbent routes. Using deterministic temperature settings ($T=0.2$), it identifies crossing paths and outputs structural adjustments.
3. **Regex Sanitization:** Defensive parsing architectures strip Markdown artifacts and validate the permutation integrity before passing the sequence back to the evaluation engine.
4. **Iterative Evaluation:** The loop enforces strict fitness evaluation, simulating decision-making and task planning cycles found in robotic navigation modules.

## 📊 Outputs & Visualizations

The algorithm successfully untangles highly inefficient random initialization routes into optimized local minima. 

* **Initial State (`initial_state.png`):** The randomized starting sequence with heavy path overlapping.
* **Final Result (`final_result.png`):** The untangled, LLM-optimized routing sequence after $N$ generations.

## ⚙️ How to Run

1. Clone the repository and establish a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Provide a `.env` file with `GEMINI_API_KEY=your_key`.
4. Execute the main pipeline: `python evolutionary_loop.py`