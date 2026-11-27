import unittest
from unittest.mock import patch

from src.env_info_impl import EnvironmentInfoUnmarshaller


class EnvironmentInfoUnmarshallerTest(unittest.TestCase):

    def test_nan_payload_is_online_with_unavailable_values(self):
        payload = '{"temperature":{"value":nan,"unit":"°C"},"humidity":{"value":nan,"unit":"%"}}'
        now = "2026-11-27T10:00:00"

        with patch("src.env_info_impl.DatetimeStringBuilder") as datetime_builder:
            datetime_builder.return_value.now.return_value = now
            env_info = EnvironmentInfoUnmarshaller(payload.encode("utf-8")).unmarshall()

        self.assertEqual(env_info.temperature.value, "n/a")
        self.assertEqual(env_info.humidity.value, "n/a")
        self.assertEqual(env_info.get_status(), "online")
        self.assertEqual(env_info.get_timestamp(), now)

    def test_missing_sensor_section_is_online_with_unavailable_values(self):
        payloads = [
            '{"humidity":{"value":40,"unit":"%"}}',
            '{"temperature":{"value":21.5,"unit":"°C"}}',
        ]
        now = "2026-11-27T10:00:00"

        with patch("src.env_info_impl.DatetimeStringBuilder") as datetime_builder:
            datetime_builder.return_value.now.return_value = now
            for payload in payloads:
                with self.subTest(payload=payload):
                    env_info = EnvironmentInfoUnmarshaller(payload.encode("utf-8")).unmarshall()

                    self.assertEqual(env_info.temperature.value, "n/a")
                    self.assertEqual(env_info.humidity.value, "n/a")
                    self.assertEqual(env_info.get_status(), "online")
                    self.assertEqual(env_info.get_timestamp(), now)
