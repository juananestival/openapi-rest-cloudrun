# Google Store Product API

A REST API for querying Google Store products, implemented with FastAPI and uv.

## Local Development

1. Install [uv](https://github.com/astral-sh/uv)
2. Run the server:
   ```bash
   uv run python main.py
   ```
3. Access the API at http://localhost:8080 or explore the docs at http://localhost:8080/docs

## Cloud Run Deployment

### Option 1: Using gcloud CLI

```bash
gcloud run deploy google-store-api \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

### Option 2: Build and Push Docker Image

1. Build the image:
   ```bash
   docker build -t gcr.io/[PROJECT_ID]/google-store-api .
   ```
2. Push to Container Registry:
   ```bash
   docker push gcr.io/[PROJECT_ID]/google-store-api
   ```
3. Deploy to Cloud Run:
   ```bash
   gcloud run deploy google-store-api \
     --image gcr.io/[PROJECT_ID]/google-store-api \
     --region us-central1 \
     --allow-unauthenticated
```

## API Endpoints

- `GET /products`: List all products
- `GET /products?category=phones`: Filter by category
- `GET /products?q=Pixel`: Search by query
- `GET /docs`: Interactive API documentation
