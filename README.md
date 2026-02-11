# **Gaussian vs. Fat‑Tailed Distributions**  
### *Normal vs. Laplace vs. Student‑t — Understanding Tails, Extremes, and Real‑World Risk*

This repository provides a clear, visual, and intuitive comparison between **Gaussian (Normal)** and **fat‑tailed** distributions such as **Laplace** and **Student‑t**.  
It includes simulations, tail‑probability analysis, log‑scale comparisons, and explanations of why fat tails matter in real‑world systems like finance, physics, and communication.

---

## 📌 **Overview**

Many natural and human‑made systems exhibit **rare but extreme deviations** that the Gaussian distribution severely underestimates.  
This project demonstrates:

- How Gaussian and fat‑tailed distributions differ  
- Why fat tails produce more extreme events  
- How tail decay (exponential vs. power‑law) affects risk  
- Visual comparisons using PDFs, CCDFs, and random samples  

The goal is to build intuition for when Gaussian assumptions fail — and what alternatives model reality better.

---

## 📊 **Distributions Compared**

| Distribution | Tail Behavior | Notes |
|-------------|---------------|-------|
| **Normal (Gaussian)** | Exponential decay | Underestimates extremes; good for CLT‑dominated systems |
| **Laplace** | Heavier exponential decay | Sharp peak + heavier tails; good for impulsive noise |
| **Student‑t (ν degrees)** | Power‑law decay | ν controls tail heaviness; ν ≤ 4 → infinite kurtosis |

---

## 📈 **Included Visualizations**

- Probability density functions (PDFs)  
- Log‑scale tail comparisons  
- Complementary CDF (CCDF) plots  
- Random sample visualizations  
- Effect of Student‑t degrees of freedom on tail thickness  

All plots are generated using Python (NumPy, SciPy, Matplotlib, Seaborn).

---

## 🧠 **Key Concepts**

### **1. Gaussian Tails**

Gaussian tails decay approximately as:

```
P(|X| > x) ≈ exp( - x^2 / 2 )
```

Extreme events become *exponentially unlikely* as x grows.

---

### **2. Laplace Tails**

Laplace tails decay as:

```
P(|X| > x) ≈ exp( - |x| )
```

Heavier than Gaussian → more frequent large deviations.

---

### **3. Student‑t Tails**

Student‑t tails decay as:

```
P(|X| > x) ≈ x^-(ν + 1)
```

This is a **power‑law**, meaning extreme events are dramatically more likely, especially for small ν.

---

### **4. Why Fat Tails Matter**

Gaussian models fail when:

- Markets crash  
- Communication channels experience bursts  
- Physical systems have shocks  
- Noise is impulsive  
- Outliers dominate system behavior  

Fat‑tailed models capture these realities more accurately.

---

## 🧪 **How to Run the Code**

### Install dependencies
```bash
pip install -r requirements.txt
```

### Launch the notebook
```bash
jupyter notebook notebooks/gaussian_vs_fat_tailed.ipynb
```

---

## 📦 **Repository Structure**

```
gaussian-vs-fat-tailed-distributions/
│
├── README.md
├── notebooks/
│   └── gaussian_vs_fat_tailed.ipynb
├── src/
│   ├── distributions.py
│   ├── plots.py
│   └── simulation.py
├── images/
│   ├── pdf_comparison.png
│   ├── tail_zoom.png
│   └── random_samples.png
├── requirements.txt
└── LICENSE
```

---

## 🧩 **Example Code Snippets**

### Generate samples
```python
import numpy as np
from scipy.stats import norm, laplace, t

n = 100000
gaussian = norm.rvs(size=n)
lap = laplace.rvs(size=n)
student = t.rvs(df=3, size=n)
```

### Plot PDFs
```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(gaussian, label="Gaussian")
sns.kdeplot(lap, label="Laplace")
sns.kdeplot(student, label="Student-t (ν=3)")
plt.legend()
plt.show()
```

---

## 📜 **License**
MIT License
```
