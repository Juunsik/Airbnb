from rest_framework.test import APITestCase
from rooms import models


class TestAmenity(APITestCase):
    NAME = "Test Amenity"
    DESC = "Test Dsc"
    UPDATE_NAME = "Update Amenity"
    UPDATE_DESC = "Update Dsc"

    def setUp(self):
        models.Amenity.objects.create(
            pk=1,
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2")

        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/1")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESC,
        )

    def test_put_amenity(self):
        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={"name": self.UPDATE_NAME, "description": self.UPDATE_DESC},
        )

        data = response.json()
        self.assertEqual(data["name"], self.UPDATE_NAME)
        self.assertEqual(data["description"], self.UPDATE_DESC)
        self.assertEqual(response.status_code, 200)

        new_name = "1" * 151
        max_length_response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={"name": new_name},
        )
        data = max_length_response.json()
        self.assertIn("name", data)
        self.assertNotIn("decs", data)
        self.assertEqual(max_length_response.status_code, 400)

    def test_delete_amenity(self):
        response = self.client.delete("/api/v1/rooms/amenities/1")

        self.assertEqual(response.status_code, 204)
