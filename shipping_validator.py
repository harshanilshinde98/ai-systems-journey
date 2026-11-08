from pydantic import BaseModel, Field, ValidationError

class ShippingContainer(BaseModel):
    container_number: str = Field(min_length=5, description="Container alphanumeric ID")
    weight_kg: float = Field(gt=0, le=35000, description="Gross container weight in kilograms")
    cargo_items: str = Field(min_length=2, description="Description of goods inside")
    destination_port: str = Field(min_length=2, description="Destination port code or name")

print("=== 1. Testing Valid Shipping Container ===")
clean_data = {
    "container_number": "MSKU9823410",
    "weight_kg": 21450.50,
    "cargo_items": "Industrial Centrifugal Pumps",
    "destination_port": "Jebel Ali, UAE"
}

container = ShippingContainer(**clean_data)
print(f"Container Validated: {container.container_number}")
print(f"Destination: {container.destination_port}")
print(f"Gross Weight: {container.weight_kg:,} kg\n")

print("=== 2. Testing Corrupted Shipping Data ===")
corrupted_data = {
    "container_number": "X",
    "weight_kg": -1200.0,
    "cargo_items": "A",
    "destination_port": ""
}

try:
    bad_container = ShippingContainer(**corrupted_data)
except ValidationError as e:
    print(f"Blocked {e.error_count()} errors from corrupting the customs filing:")
    for error in e.errors():
        field = error['loc'][0]
        message = error['msg']
        print(f"  [REJECTED] Field '{field}': {message}")