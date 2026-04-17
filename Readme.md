Multi-Tier Flask & Docker Architecture Demo
This repository demonstrates the evolution of a web application from a Two-Tier architecture to a Three-Tier architecture. It is designed to showcase core DevOps principles, including containerization, microservices communication, and persistent storage.

📂 Project Structure
Plaintext
teck_nebula_demo/
├── two-tier-architect/       # Basic Backend-Frontend interaction
│   ├── app.py                # Flask API (hardcoded data)
│   ├── index.html            # Client-side UI
│   ├── Dockerfile            # Container definition
│   └── requirements.txt      # Python dependencies
├── three-tier-architecture/  # Scalable Backend-Frontend-DB interaction
│   ├── backend_3tier.py      # Flask API (Database logic)
│   ├── frontend_3tier.html   # Client-side UI
│   ├── database.db           # SQLite persistent storage
│   ├── Dockerfile            # Container definition
│   └── requirements.txt      # Python dependencies
└── .gitignore                # Prevents tracking of __pycache__ and local DBs
🏗️ Architecture Breakdown
1. Two-Tier Architecture
In this setup, the Presentation Layer (Frontend) communicates directly with the Application Layer (Backend). The data is stored in-memory within the Python script.

Technology: Python Flask, HTML/JS.

Best for: Simple prototypes and lightweight internal tools.

2. Three-Tier Architecture
This setup introduces a Data Layer (SQLite). The Backend acts as a bridge, ensuring the Frontend never has direct access to the database file.

Technology: Python Flask, SQLite, HTML/JS.

DevOps Focus: Persistent volumes, database connectivity, and separation of concerns.

🐳 Containerization (Docker)
Both tiers are fully containerized using optimized python:3.9-slim images to reduce the attack surface and image size.

Build the Images
Bash
# From the root directory
docker build -t devops-2tier ./two-tier-architect
docker build -t devops-3tier ./three-tier-architecture
Run the Containers
Two-Tier:

Bash
docker run -d --name 2tier-app -p 5000:5000 devops-2tier
Three-Tier (with Volume for Persistence):

Bash
docker run -d --name 3tier-app -p 5001:5001 -v $(pwd)/three-tier-architecture:/app devops-3tier
🚀 How to Use
Access the API:

2-Tier: http://localhost:5000/api/data

3-Tier: http://localhost:5001/api/inventory

Access the Frontend:
Open the index.html (2-tier) or frontend_3tier.html (3-tier) in any modern web browser.

Verify via CLI:

Bash
curl http://localhost:5001/api/inventory
🛠️ DevOps Skills Demonstrated
Microservices: Decoupling frontend and backend logic.

Docker Layer Caching: Efficiently utilizing requirements.txt to speed up builds.

Persistent Storage: Implementing Docker volumes to ensure database data survives container restarts.

Network Mapping: Exposing container ports to the host Linux environment.

Author: [M.Abubakr]
Role: DevOps & AIOps Engineer
