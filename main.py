from fastapi import FastAPI, Query
from typing import Any, List, Dict, Optional
import datetime

app = FastAPI(title="Google Store Product API")

# MOCK: This data simulates fetching products from a database or API.
STORE_PRODUCTS_DATA = [
    {"id": "p9pxl", "category": "phones", "name": "Pixel 9 Pro XL", "description": "The most powerful Pixel yet, with a pro-level camera and Gemini AI.", "price": 1099.00, "currency": "USD", "specs": ["6.8-inch Super Actua display", "Triple rear camera system", "Tensor G4 chip"]},
    {"id": "p9p", "category": "phones", "name": "Pixel 9 Pro", "description": "Pro cameras and Gemini AI in a compact size.", "price": 999.00, "currency": "USD", "specs": ["6.3-inch Super Actua display", "Triple rear camera system", "Tensor G4 chip"]},
    {"id": "p9", "category": "phones", "name": "Pixel 9", "description": "The everyday premium phone with AI-powered helpfulness.", "price": 799.00, "currency": "USD", "specs": ["6.3-inch Actua display", "Advanced dual rear camera", "Tensor G4 chip"]},
    {"id": "p8a", "category": "phones", "name": "Pixel 8a", "description": "The AI-powered Pixel at an amazing value.", "price": 499.00, "currency": "USD", "specs": ["6.1-inch Actua display", "Tensor G3 chip", "All-day battery"]},
    {"id": "pbp2", "category": "earbuds", "name": "Pixel Buds Pro 2", "description": "The only earbuds engineered for Gemini.", "price": 229.00, "currency": "USD", "features": ["Large 11mm drivers", "Active Noise Cancellation with Silent Seal 2.0", "Built-in Gemini"]},
    {"id": "pba", "category": "earbuds", "name": "Pixel Buds A-Series", "description": "Rich sound, for less.", "price": 99.00, "currency": "USD", "features": ["Custom-designed 12mm drivers", "Adaptive Sound", "Up to 5 hours of listening time"]},
    {"id": "pw3", "category": "watches", "name": "Pixel Watch 3", "description": "The first watch with Loss of Pulse Detection.", "price": 349.00, "currency": "USD", "features": ["Advanced health and fitness by Fitbit", "Daily Readiness Score", "Comprehensive heart health tracking"]},
    {"id": "fc6", "category": "activity trackers", "name": "Fitbit Charge 6", "description": "Give your routine a routine.", "price": 159.00, "currency": "USD", "features": ["Built-in GPS", "Heart rate tracking", "Stress management tools"]},
    {"id": "fi3", "category": "activity trackers", "name": "Fitbit Inspire 3", "description": "Do what you love and feel your best.", "price": 99.00, "currency": "USD", "features": ["Up to 10 days of battery", "Active Zone Minutes", "Always-on heart rate"]},
    {"id": "nth4", "category": "smarthome", "name": "Nest Learning Thermostat (4th gen)", "description": "The thermostat that learns from you.", "price": 279.00, "currency": "USD", "features": ["Smart Schedule", "Energy History", "Home/Away Assist"]},
    {"id": "ndc", "category": "smarthome", "name": "Nest Doorbell (wired, 2nd gen)", "description": "The wired doorbell that knows who’s there.", "price": 179.00, "currency": "USD", "features": ["24/7 continuous video recording", "Intelligent alerts", "Talk and Listen"]},
    {"id": "pt", "category": "tablets", "name": "Pixel Tablet", "description": "The tablet that's also the heart of your home.", "price": 399.00, "currency": "USD", "features": ["11-inch screen", "Charging Speaker Dock included", "Chromecast built-in"]},
    {"id": "p9pc", "category": "accessories", "name": "Pixel 9 Pro Case", "description": "Designed to protect and look great.", "price": 34.99, "currency": "USD", "colors": ["Obsidian", "Porcelain", "Hazel", "Rose Quartz"]}
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Google Store Product API", "docs": "/docs"}

@app.get("/products")
def get_products(
    category: Optional[str] = Query(None, description="The category of products to filter by (e.g., 'phones', 'earbuds', 'smarthome')"),
    search_query: Optional[str] = Query(None, alias="q", description="A keyword or phrase to search for within product names or descriptions")
) -> Dict[str, Any]:
    """
    Retrieves a list of products from the Google Store, optionally filtered by category or a search query.
    """
    filtered_products = []
    for product in STORE_PRODUCTS_DATA:
        match = True
        if category and product["category"].lower() != category.lower():
            match = False
        if search_query:
            query_lower = search_query.lower()
            if query_lower not in product["name"].lower() and query_lower not in product["description"].lower():
                match = False
        if match:
            filtered_products.append(product)

    if not filtered_products:
        return {"products": [], "message": "No products found matching your criteria."}
    return {"products": filtered_products}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
