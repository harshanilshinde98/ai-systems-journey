# AI Systems Journey: B2B Shipping Data Validator

A production-grade data validation engine designed to eliminate manual data-entry errors in freight forwarding and customs clearance workflows.

## The Business Problem
In high-volume logistics corridors (such as Nhava Sheva / JNPT), shipping documents—such as Bills of Lading and Shipping Bills—are frequently retyped manually by back-office staff. A single typographical error in a container ID, weight, or destination can trigger customs holds, port delays, and thousands of rupees in demurrage penalties.

## The Solution
This engine implements strict data contracts using **Pydantic** to validate incoming logistics records before they enter customs filing systems or ERP databases:
- **Alphanumeric ID Validation:** Rejects corrupted or abbreviated container IDs.
- **Physical Weight Boundaries:** Enforces legal gross container payload constraints (`0 < weight <= 35,000 kg`).
- **Comprehensive Error Trapping:** Intercepts multiple validation failures simultaneously without crashing downstream systems.

## Quick Start (How to Run This Project)

```bash
# 1. Clone the repository
git clone [https://github.com/harshanilshinde98/ai-systems-journey.git](https://github.com/harshanilshinde98/ai-systems-journey.git)

# 2. Navigate to the project directory
cd ai-systems-journey

# 3. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1    # On Windows
# source venv/bin/activate     # On macOS/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the validation engine
python shipping_validator.py