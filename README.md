## AI Car Assistant

An AI-powered application that helps drivers diagnose car problems and estimate repair costs.

### Features
- Ask AI about car problems
- Personalized responses using car profile
- Knowledge base retrieval (RAG architecture)
- Maintenance tracking

### Add Car Profile Feature

Users should input:

- Car make
- Model
- Year
- Mileage

Then the AI response becomes personalized.

### Tech Stack

#### 1. Frontend
- React
- TypeScript
- Axios
- JWT auth

#### 2. Backend
- Python Flask
- FastAPI

#### 3. AI integration
- OpenAI API

#### 4. Vector Database
- ChromaDB

#### 5. Database
- SQLite
- PostgreSQL

#### 6. Caching
- radis

#### 7. DevOps
- Docker
- Docker Compose


### Project Architecture

The project looks like this:

```text
ai-car-assistant
|
backend
|-- app
|    |-- main.py
|    |-- database.py
|    |-- models.py
|    |-- schemas.py
|    |-- auth.py
|    |-- routers
|          |-- cars.py
|          |-- maintenance.py
|          |-- ai.py
|
|-- requirements.txt
|-- Dockerfile
|
frontend
|-- src
|    |
|    api
|    |-- api.ts
|    |
|    components
|    |-- CarForm.tsx
|    |-- AskAI.tsx
|    |-- AnswerBox.tsx
|    |
|    types
|    |-- car.ts
|    |
|    App.tsx
|    main.tsx
|    App.css
|-- Dockerfile
|
docker-compose.yml
|
README.md
```

### ⚙️ Installation (Run the System)

#### 0. Clone the Repository

```bash
git clone https://github.com/sanjoy-kumar/ai-car-assistant.git
cd ai-car-assistant
```

#### 1. Backend:

```bash
cd backend
```

Create .env file:

```bash
backend/.env
```

Insert the following lines in the .env file:

```text
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY = "supersecret"
ALGORITHM = "HS256"
REDIS_PORT=6379

## --- For Docker Testing (docker-compose up): ----
#DATABASE_URL=postgresql://postgres:password@db:5432/cars
#REDIS_HOST=host.docker.internal

## ---- For Local Testing (Outside Docker): -----
DATABASE_URL=postgresql://postgres:password@localhost:5432/cars
REDIS_HOST=localhost
```

```bash
pip install -r requirements.txt
python knowledge.py
python main.py
```

#### 2. Frontend:

```bash
cd frontend
```

Create .env file:

```bash
frontend/.env
```
Insert the following lines in the .env file:

```text
## For Local machine or development
VITE_API_URL=http://localhost:8000
## For docker's container
#VITE_API_URL=http://backend:8000
## For Production Server or VM
#VITE_API_URL=https://api.yourdomain.com
```

```bash
npm install
npm install axios react-markdown
npm start
```

Open:

http://localhost:3000


### Run Everything for Docker

From root project:

```bash
docker-compose up --build
```

Now we have:

1. Backend

http://localhost:8000

2. API docs

http://localhost:8000/docs

3. Frontend (React)

http://localhost:3000


The system runs as:

| Service | URL |
| :--- | :--- |
| **Frontend** | http://localhost:3000 |
| **Backend** | http://localhost:8000 |
| **API Docs** | http://localhost:8000/docs |
| **Database** | localhost:5432 |


### 🖥️ Example Interaction



### 🤝 Contributing

Contributions are welcome!

#### Steps

1. Fork the repository
2. Create a branch

```bash
git checkout -b feature/new-feature
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature/new-feature
```
5. Open a Pull Request

### 🛡️ License

This project is licensed under the MIT License.

### 👨‍💻 Author

Developed by Sanjoy Kumar

GitHub:
https://github.com/sanjoy-kumar

