from fastapi.testclient import TestClient
from server import app
from utils.image import ImageData

client = TestClient(app)


# Minimum required fields need for an image.
def test_simple_upload():
    response = client.post(
        "/upload/",
        json=ImageData(url="http://example.com/simpleImage.png", dpi=300).dict(),
    )
    assert response.status_code == 200
    assert "_id" in response.json()

# Test a full upload request and also a new parameter


def test_full_upload():
    response = client.post(
        "/upload/",
        json=ImageData(
            url="http://example.com/image.jpg",
            camera_type="Canon",
            location="Waldkirch Factory",
            dpi=350,
            domain="Supply Chain Monitoring",
            newly_added_parameter="more_metadata_doesnthurt",
            label=["Package", "L", "Plastic"]).dict())
    assert response.status_code == 200
    assert "_id" in response.json()

# Upload and image to db and retrieve it via id


def test_get_images():
    # upload and test image to db
    response = client.post(
        "/upload/",
        json=ImageData(url="http://test.com/testImage.png", dpi=300).dict(),
    )
    test_id = response.json()["_id"]
    response = client.get(f"/images/{test_id}")
    assert response.status_code == 200
    assert "url" in response.json()[0]

# Try to upload a low quality image (as per app config), make
# sure that validation error is thrown.


def test_dpi_limit():
    response = client.post(
        "/upload/",
        json={"url": "http://test.com/lowQualityImage.png", "dpi": 2},
    )
    assert response.status_code == 422  # validation error

# Make sure mutually exclusive labels are not passed to training data.


def test_mutually_exclusive_labels():
    # According to app config we cannot have plastic envelopes.
    labels = ["Envelope", "Plastic"]
    response = client.post(
        "/upload/",
        json={"url": "http://test.com/testImage.png",
              "dpi": 300, "label": labels},
    )

    # Validation error
    assert response.status_code == 422


def test_invalid_location():
    # Try to upload an image with an invalid location
    response = client.post(
        "/upload/",
        json={"url": "http://test.com/invalidLocationImage.png",
              "dpi": 300,
              "location": "Emmendingen"},
    )

    # Validation error
    assert response.status_code == 422
