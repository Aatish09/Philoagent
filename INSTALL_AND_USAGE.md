<table style="border-collapse: collapse; border: none;">
  <tr style="border: none;">
    <td width="20%" style="border: none;">
      <a href="https://theneuralmaze.substack.com/" aria-label="The Neural Maze">
        <img src="https://avatars.githubusercontent.com/u/151655127?s=400&u=2fff53e8c195ac155e5c8ee65c6ba683a72e655f&v=4" alt="The Neural Maze Logo" width="150"/>
      </a>
    </td>
    <td width="80%" style="border: none;">
      <div>
        <h2>📬 Stay Updated</h2>
        <p><b><a href="https://theneuralmaze.substack.com/">Join The Neural Maze</a></b> and learn to build AI Systems that actually work, from principles to production. Every Wednesday, directly to your inbox. Don't miss out!
</p>
      </div>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://theneuralmaze.substack.com/">
    <img src="https://img.shields.io/static/v1?label&logo=substack&message=Subscribe Now&style=for-the-badge&color=black&scale=2" alt="Subscribe Now" height="40">
  </a>
</p>

<table style="border-collapse: collapse; border: none;">
  <tr style="border: none;">
    <td width="20%" style="border: none;">
      <a href="https://decodingml.substack.com/" aria-label="Decoding ML">
        <img src="https://github.com/user-attachments/assets/f2f2f9c0-54b7-4ae3-bf8d-23a359c86982" alt="Decoding ML Logo" width="150"/>
      </a>
    </td>
    <td width="80%" style="border: none;">
      <div>
        <h2>📬 Stay Updated</h2>
        <p><b><a href="https://decodingml.substack.com/">Join Decoding ML</a></b> for proven content on production-grade AI, GenAI, and information retrieval systems. Every week, straight to your inbox.</p>
      </div>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://decodingml.substack.com/">
    <img src="https://img.shields.io/static/v1?label&logo=substack&message=Subscribe Now&style=for-the-badge&color=black&scale=2" alt="Subscribe Now" height="40">
  </a>
</p>

------

# 🚀 Installation and Usage Guide

This guide will help you set up and run a ...

# 📑 Table of Contents

- [📋 Prerequisites](#-prerequisites)
- [🎯 Getting Started](#-getting-started)
- [📁 Project Structure](#-project-structure)
- [🏗️ Set Up Your Local Infrastructure](#-set-up-your-local-infrastructure)
- [⚡️ Running the Code for Each Module](#️-running-the-code-for-each-module)
- [🔧 Utlity Commands](#-utility-commands)

# 📋 Prerequisites

## Local Tools

For all the modules, you'll need the following tools installed locally:

| Tool | Version | Purpose | Installation Link |
|------|---------|---------|------------------|
| Python | 3.11 | Programming language runtime | [Download](https://www.python.org/downloads/) |
| uv | ≥ 0.4.30 | Python package installer and virtual environment manager | [Download](https://github.com/astral-sh/uv) |
| GNU Make | ≥ 3.81 | Build automation tool | [Download](https://www.gnu.org/software/make/) |
| Git | ≥2.44.0 | Version control | [Download](https://git-scm.com/downloads) |
| Docker | ≥27.4.0 | Containerization platform | [Download](https://www.docker.com/get-started/) |

## Cloud Services

Also, the course requires access to these cloud services. The authentication to these services is done by adding the corresponding environment variables to the `.env` file:

| Service | Purpose | Cost | Environment Variable | Setup Guide | Starting with Module |
|---------|---------|------|---------------------|-------------| ---------------------|
| [Groq](https://rebrand.ly/philoagents-groq) | LLM API that powers the agents | Free tier | `GROQ_API_KEY` | [Quick Start Guide](https://rebrand.ly/philoagents-groq-quickstart) | Module 1 |
| [Opik](https://rebrand.ly/philoagents-opik) | LLMOps | Free tier (Hosted on Comet - same API Key) | `COMET_API_KEY` | [Quick Start Guide](https://rebrand.ly/philoagents-opik-quickstart) | Module 5 |
| [OpenAI API](https://openai.com/index/openai-api/) | LLM API used for evaluation | Pay-per-use | `OPENAI_API_KEY` | [Quick Start Guide](https://platform.openai.com/docs/quickstart) | Module 5 |

When working locally, the infrastructure is set up using Docker. Thus, you can use the default values found in the [config.py](philoagents-api/src/philoagents/config.py) file for all the infrastructure-related environment variables.

But, in case you want to deploy the code, you'll need to setup the following services with their corresponding environment variables:

| Service | Purpose | Cost | Required Credentials | Setup Guide |
|---------|---------|------|---------------------|-------------| 
| [MongoDB](https://rebrand.ly/philoagents-mongodb) | Document database | Free tier | `MONGODB_URI` | 1. [Create a free MongoDB Atlas account](https://rebrand.ly/philoagents-mongodb-setup-1) <br> 2. [Create a Cluster](https://rebrand.ly/philoagents-mongodb-setup-2) </br> 3. [Add a Database User](https://rebrand.ly/philoagents-mongodb-setup-3) </br> 4. [Configure a Network Connection](https://rebrand.ly/philoagents-mongodb-setup-4) |

# 🎯 Getting Started

## 1. Clone the Repository

Start by cloning the repository and navigating to the project directory:
```
git clone https://github.com/neural-maze/philoagents-course.git
cd philoagents-course 
```

Next, we have to prepare your Python environment and its dependencies.

## 2. Installation

To install the dependencies and activate the virtual environment, run the following commands:

```bash
uv venv .venv
. ./.venv/bin/activate # or source ./.venv/bin/activate
uv pip install -e .
```

Test that you have Python 3.11.9 installed in your new `uv` environment:
```bash
uv run python --version
# Output: Python 3.11.9
```

This command will:
- Create a virtual environment with the Python version specified in `.python-version` using `uv`
- Activate the virtual environment
- Install all dependencies from `pyproject.toml`

## 3. Environment Configuration

Before running any command, you have to set up your environment:
1. Create your environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and configure the required credentials following the inline comments and the recommendations from the [Cloud Services](#-prerequisites) section.

# 📁 Project Structure

The project follows a clean architecture structure commonly used in production Python projects:

```bash
philoagents-api/
    ├── data/                  # Data files
    ├── notebooks/             # Notebooks
    ├── src/philoagents/       # Main package directory
    │   ├── application/       # Application layer
    │   ├── domain/            # Domain layer
    │   ├── infrastructure/    # Infrastructure layer
    │   └── config.py          # Configuration settings
    ├── tools/                 # Entrypoint scripts that use the Python package
    ├── .env.example           # Environment variables template
    ├── .python-version        # Python version specification
    ├── Dockerfile             # API Docker image definition
    ├── Makefile               # Project commands
    └── pyproject.toml         # Project dependencies
```

# 🏗️ Set Up Your Local Infrastructure

We use Docker to set up the local infrastructure (Game UI, Agent API, MongoDB).

> [!WARNING]
> Before running the command below, ensure you do not have any processes running on ports `27017` (MongoDB), `8000` (Agent API) and `8080` (Game UI).

To start it, run:
```bash
make infrastructure-up
```

To stop it, run:
```bash
make infrastructure-stop
```

To build the Docker images (without running them), run:
```bash
make infrastructure-build
```

# ⚡️ Running the Code for Each Lesson

After you have set up your environment (through the `.env` file) and local infrastructure (through Docker), you are ready to run the code.

## Modules 1 to 4

As the first 4 modules are coupled together, you can test them all at once.

First, populate the long term memory within your MongoDB instance (required for agentic RAG) with the following command:
```bash
make create-long-term-memory
```

> [!NOTE]
> To visualize the raw and RAG data from MongoDB, we recommend using [MongoDB Compass](https://rebrand.ly/philoagents-mongodb-compass) or Mongo's official IDE plugin (e.g., `MongoDB for VS Code`). To connect to the working MongoDB instance, use the `MONGODB_URI` value from the `.env` file or found inside the [config.py](philoagents-api/src/philoagents/config.py) file.

Next, you can access the game by typing in your browser:
```
http://localhost:8080
```
Which will open the game UI, similar to the screenshot below:

![Philosopher Town](static/game_starting_page.png)

To see the instructions for playing the game, you can click on the `Instructions` button. To start the game, you can click on the `Let's Play!` button.

Now you can start playing the game, wonder around the town and talk to our philosophers, as seen in the screenshot below:

![Philosopher Town](static/game_socrates_example.png)

You can also access the API documentation by typing in your browser:
```
http://localhost:8000/docs
```

To delete the long term memory from your MongoDB instance, you can run the following command:
```bash
make delete-long-term-memory
```

## Module 5

First, to visualize the prompt traces, as seen in the screenshot below, visit [Opik](https://rebrand.ly/philoagents-opik-dashboard).

![Opik](static/opik_monitoring_example.png)

To evaluate the agents, you can run the following command:
```bash
make evaluate-agent
```

To visualize the evaluation results, as seen in the screenshot below, you also have to visit [Opik](https://rebrand.ly/philoagents-opik-dashboard).

![Opik](static/opik_evaluation_example.png)

We already generated a dataset for you found at [data/evaluation_dataset.json](philoagents-api/data/evaluation_dataset.json), but in case you want to generate a new one (to override the existing one), you can run the following command:
```bash
make generate-evaluation-dataset
```
