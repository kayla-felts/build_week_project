from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_input():
    """Return 200 Success when input is valid."""
    response = client.post(
        '/predict',
        json={
            property_type: 'Apartment'
            room_type: 'Entire home/apt'
            bed_type: 'Real Bed'
            cancellation_policy: 'Strict'
            city: 'NYC'
            host_identity_verified: 'True'
            instant_bookable: 'False'
            neighbourhood:'Brooklyn Heights'
            zipcode: 11201
            amenities: 8
            accommodates: 3
            bathrooms: 1
            bedrooms: 1
            beds: 1
            host_since_days: 3341
        }
    )
    body = response.json()
    assert response.status_code == 200
    assert body['prediction'] in [True, False]
    assert 0.50 <= body['probability'] < 1


def test_invalid_input():
    """Return 422 Validation Error when amenities is negative."""
    response = client.post(
        '/predict',
        json={
            property_type: 'Apartment'
            room_type: 'Entire home/apt'
            bed_type: 'Real Bed'
            cancellation_policy: 'Strict'
            city: 'NYC'
            host_identity_verified: 'True'
            instant_bookable: 'False'
            neighbourhood:'Brooklyn Heights'
            zipcode: 11201
            amenities: 8
            accommodates: 3
            bathrooms: 1
            bedrooms: 1
            beds: 1
            host_since_days: 3341
        }
    )
    body = response.json()
    assert response.status_code == 422
    assert 'amenities' in body['detail'][0]['loc']