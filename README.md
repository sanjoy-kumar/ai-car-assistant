

Now your project shows real production skills:

#### Frontend

- React
- Axios
- JWT auth

### Backend

- FastAPI
- PostgreSQL
- AI integration

### DevOps

- Docker
- Docker Compose


Frontend now uses:

✅ Vite (fast dev server)
✅ TypeScript type safety
✅ Component architecture
✅ API service layer
✅ Clean folder structure


When a user asks a question:

User → Backend → AI model → Response

Without caching, the AI model runs every time (slow + expensive).

With Redis:

User → Backend
        │
        ├─ Redis cache hit → return instantly
        │
        └─ Redis miss → call AI → save result → return
