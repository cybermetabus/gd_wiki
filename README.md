# 🧠 P-Reinforce: The Autonomous Knowledge Gardener

> **"Turning fragmented thoughts into a persistent, evolving brain through Reinforcement Learning."**

`P-Reinforce` is an AI-driven knowledge automation engine inspired by the LLM-Wiki architecture. It functions as an **Autonomous Gardener**—monitoring your raw inputs, classifying them with semantic precision, and interweaving them into a dense, navigable web of knowledge.

---

## 📂 System Architecture

The workspace is divided into three functional layers to maintain focus and clarity:

### 1️⃣ `00_Raw/` (The Soil)
- **Source of Truth**: All unprocessed, raw data from the user.
- **Daily Journaling**: Organizes original notes by date (`YYYY-MM-DD`).

### 2️⃣ `10_Wiki/` (The Garden)
- **🛠️ Projects**: Goal-oriented summaries and current active workflows.
- **💡 Topics**: Conceptual knowledge (Psychology, Coding, Philosophy, etc.).
- **⚖️ Decisions**: Log of critical pivots and logical deductions.
- **🚀 Skills**: Reusable patterns, prompt engineering, and refined workflows.

### 3️⃣ `20_Meta/` (The Brain)
- **`Graph.json`**: Data structure for knowledge connectivity visualization.
- **`Policy.md`**: RL weights and classification logic based on user feedback.
- **`Index.md`**: The master Table of Contents.

---

## 🧠 Core Engine: RL-Driven Logic

P-Reinforce optimizes its actions based on the **Reward Function ($R$):**
$$R = w_1(\text{Accuracy}) + w_2(\text{Connectivity}) + w_3(\text{Satisfaction})$$

- **Autonomous Classification**: New information is automatically routed to existing folders or prompts for category creation.
- **Bi-directional Linking**: Automatically creates `[[links]]` between related concepts to prevent "isolated" knowledge.
- **Git Protocol**: Every reinforcement stage is committed and pushed to GitHub, ensuring an immutable timeline of your intellectual growth.

---

## 🚀 How to Use

1. **Input**: Drop any text, markdown, or research file into `00_Raw/YYYY-MM-DD/`.
2. **Reinforce**: The P-Reinforce agent will detect the new input, synthesize it using the **Wiki Template**, and move it to the appropriate `10_Wiki/` subfolder.
3. **Feedback**: 
   - Move a file to a different folder -> Agent updates the `Policy.md` weights.
   - Praise or correction -> Agent refines its boundary definitions.

---

## 🛠️ Tech Stack

- **Engine**: Antigravity (LLM Agent)
- **Foundation**: Markdown + Obsidian-style Linking
- **Persistence**: Git + GitHub Sync
- **Logic**: Reinforcement Learning (Weight-based)

---

*“Knowledge is not a library, it’s a living tree. Let P-Reinforce be the roots.”*
