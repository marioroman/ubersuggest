# 🧠 AI Workflow Automation Technical Assessment

**Role**: Sr. Software Engineer – Python and AI Workflow Automation

**Deliverable**: GitHub repo + README

---

## 🎯 Objective

Simulate a real-world automation task: a junior marketing assistant needs to create a client briefing document from public data using a mix of API integration and AI summarization.

Your task is to build a simple Python automation that fetches company information, organizes it, and produces a ready-to-share report using AI.

---

## 📌 Scenario

Imagine you’ve joined a team supporting marketing strategy for small businesses. Your colleague needs to create a client research brief quickly and wants a tool that can help automate it.

---

## 🧩 What You’ll Build

Build a simple Python CLI or web script that:

1. Accepts a **company name** or **domain** (e.g., `stripe.com`) as input
2. **Uses a free company info API** to get basic data:
  * Use Clearbit's free Logo & Autocomplete API or [Hunter.io](https://hunter.io/api)
  * Optional fallback: **DuckDuckGo**, **Wikipedia**
3. Fetches recent news or mentions:
  * Use the [NewsAPI.org](https://newsapi.org/) free tier or [Mediastack](https://mediastack.com/) for headlines
  * Filter for recent news related to the company/domain
4. Generates a research brief:
  * Use OpenAI (or any LLM) to write a summary like:
  > "Stripe is a fintech company focused on online payments. Based on recent news, they’ve recently expanded in the APAC region and launched a new fraud detection product."
  * Include a bullet list of the 3–5 most relevant articles with links
5. Exports the output:
  * As a markdown, plain text file, or Google Doc (optional)
  * Structure: Logo + Company Info + AI Summary + Recent Articles

---

## 🧰 Tools (Pick What You Like)

* Python
* OpenAI API
* `requests`, `pandas`, `jinja2`
* Docker

---

## 🗂 Expected Deliverables

1. A `README.md` with:
  * Setup instructions
  * Example input/output
  * Assumptions
2. Python scripts
3. Example output for 1 or 2 companies (e.g., stripe.com, notion.so)

---

## ✅ What We’ll Evaluate

| Area             | Criteria                                                |
| ---------------- | ------------------------------------------------------- |
| Automation logic | Can you stitch multiple services into one clear output? |
| Code quality     | Clear structure, modularity, error handling             |
| AI integration   | Is the prompt well thought out? Does the output feel usable?       |
| Simplicity       | Can a marketing user easily get value from the script?       |
| Communication    | Can you explain your approach clearly in the README?           |

---

## 🔒 What You Don’t Need

* No frontend polish needed
* No deployment or databases
* No production-level code — just clean, working scripts

---

## ✨ Bonus Points (Optional)

* Add a **Streamlit UI**
* Include a .pdf or nicely formatted markdown export
* Let the user pass a list of domains and output multiple briefs
* Use AI to build the code and explain how and what you use it for
