## AI Car Assistant


<div align="left">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi" alt="FastAPI" />
  <img src="https://img.shields.io/badge/React-18-blue?style=for-the-badge&logo=react" alt="React" />
  <img src="https://img.shields.io/badge/PostgreSQL-18-blue?style=for-the-badge&logo=postgresql" alt="Postgres" />
  <img src="https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge&logo=docker" alt="Docker" />
  <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg?style=for-the-badge" alt="License" />
</div>


An AI-powered application that helps drivers diagnose car problems and estimate repair costs.

## 🚀 Features
- **Intelligent Diagnostics**: Natural language processing to diagnose car symptoms.
- **Personalized Insights**: Tailored responses based on your car's make, model, year, and mileage.
- **RAG Architecture**: Knowledge retrieval for accurate, context-aware advice.
- **High-Performance Caching**: Redis integration to reduce latency and optimize AI API costs.
- **Maintenance Tracking**: Keep a history of your vehicle's service records.


## 🏗️ Project Architecture
The system follows a microservices approach, utilizing Docker to manage containerized components.

```text
ai-car-assistant/
├── backend/          # FastAPI application & business logic
├── frontend/         # React + TypeScript SPA
└── images/           # Documentation assets
└── scripts/ 
├── docker-compose.yml # Orchestration of containers
└── README.md
```


## 🛠️ Tech Stack
- **Frontend**: React, TypeScript, Axios, JWT Authentication
- **Backend**: Python, FastAPI
- **AI Engine**: OpenAI API with RAG (Retrieval-Augmented Generation)
- **Database**: PostgreSQL, SQLite
- **Caching**: Redis
- **DevOps**: Docker, Docker Compose

## 🚀 Getting Started

#### Prerequisites
- Docker Desktop installed
- Node.js (v20+) and Python (v3.11+)

#### Installation

1. Clone the repository:

```bash
git clone https://github.com/sanjoy-kumar/ai-car-assistant.git
cd ai-car-assistant
```

2. Configure Environment Variables:

    Create a **.env** file in both **/backend** and **/frontend** directories using the provided templates in the source code.

3. Launch the System:
To run the entire stack using Docker Compose:

```bash
docker-compose up --build
```
## 🌐 Service Access

| Service | URL |
| :--- | :--- |
| Frontend | http://localhost:3000 |
| Backend | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |
| Database | localhost:5432 |


## 📸 System Overview

![Optional Alt Text](images/1.png)

![Optional Alt Text](images/2.png)

![Optional Alt Text](images/3.png)


## 🤝 Contributing

Contributions are welcome!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## 🛡️ License

Distributed under the MIT License. See LICENSE for more information.

## 👨‍💻 Author

Sanjoy Kumar Das |  [GitHub](https://github.com/sanjoy-kumar)



