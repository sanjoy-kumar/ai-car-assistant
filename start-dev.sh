#!/bin/bash

echo "Starting backend..."
cd backend
uvicorn app.main:app --reload &

echo "Starting frontend..."
cd ../frontend
npm run dev

