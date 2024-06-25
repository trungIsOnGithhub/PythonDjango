from datetime import datetime, timedelta
import unittest
from main.utils import convert_time
from rlimiter.main.models import TimeUnit

class TestConvertTime(unittest.TestCase):
    def setUp(self):
        self.current_time = datetime.timestamp(datetime(2024,1,1)) #1704067200
        self.current_time_exact = 1704067200.0 #read from outside when real use
    # def tearDown(self):
    #     del self.current_time

    def test_convert_to_second(self):
        """Test convert timestamp to Second Unit"""
        self.assertEqual(convert_time(self.current_time, TimeUnit.SEC), self.current_time_exact/1000.0)

    def test_negative_number(self):
        """Test convert timestamp to Minute Unit"""
        self.assertEqual(convert_time(self.current_time, TimeUnit.MIN), self.current_time_exact/(60 * 1000.0))

    def test_zero(self):
        """Test convert timestamp to Hour Unit"""
        self.assertEqual(convert_time(self.current_time, TimeUnit.HOUR), self.current_time_exact/)

if __name__ == "__main__":
    unittest.main(verbosity=2)