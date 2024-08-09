FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY . /app

# RUN apt-get update && apt-get install -y \
#     libgl1-mesa-glx \
#     libglib2.0-0

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir fastapi python-multipart transformers torch

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
