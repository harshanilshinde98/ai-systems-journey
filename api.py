from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# 1. Initialize your Web API application
app = FastAPI(title="Nhava Sheva Customs Validation API", version="1.0")

# 2. Your exact Shipping Container Data Contract
class ShippingContainer(BaseModel):
    container_number: str = Field(min_length=5, description="Container alphanumeric ID")
    weight_kg: float = Field(gt=0, le=35000, description="Gross container weight in kilograms")
    cargo_items: str = Field(min_length=2, description="Description of goods inside")
    destination_port: str = Field(min_length=2, description="Destination port code or name")

# 3. Create a Health-Check Endpoint (GET /)
@app.get("/")
def home():
    return {"status": "online", "system": "Nhava Sheva Customs Gateway v1"}

# 4. Create the Validation Endpoint (POST /validate-container)
@app.post("/validate-container")
def validate_container(container: ShippingContainer):
    # If the incoming data reaches this line, Pydantic ALREADY validated it!
    return {
        "status": "APPROVED",
        "message": "Container data meets all customs regulatory standards.",
        "verified_container": container.container_number,
        "recorded_weight_kg": container.weight_kg,
        "destination": container.destination_port
    }   