import pytest
import requests
from pydantic import BaseModel, ValidationError


# We define the expected schema with Pydantic
class CompanySchema(BaseModel):
    id: int
    name: str
    address: str
    zip: str
    country: str
    employeeCount: int
    industry: str
    marketCap: int
    domain: str
    logo: str
    ceoName: str


# Test category with pytest
@pytest.mark.api
def test_get_companies():
    url = "https://fake-json-api.mock.beeceptor.com/companies"
    response = requests.get(url)

    # Check status code 200
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Validate that the response is JSON
    try:
        companies = response.json()
    except ValueError:
        pytest.fail("Response is not a valid JSON")

    # Validate that each company conforms to the expected schedule
    for company in companies:
        try:
            CompanySchema(**company)
        except ValidationError as e:
            pytest.fail(f"Response JSON does not match expected schema: {e}")
