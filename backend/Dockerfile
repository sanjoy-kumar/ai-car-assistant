FROM python:3.11

WORKDIR /app

# 1. Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# 2. Upgrade pip to ensure faster/better metadata handling
RUN pip install --no-cache-dir --upgrade pip

# 3. Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# 4. Now copy the rest of your code
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
