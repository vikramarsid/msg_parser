#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tests for data_models module - Python 3 compatibility."""

import struct
import unittest
from datetime import datetime, timedelta

from msg_parser.data_models import DataModel, get_time, get_floating_time, get_multi_value_offsets


class TestDataModelsPython3Compatibility(unittest.TestCase):
    """Test suite for Python 3 compatibility of data_models module."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.data_model = DataModel()
    
    def test_ptyp_integer16(self):
        """Test PtypInteger16 method with Python 3 int.from_bytes."""
        # Test positive number
        test_value = struct.pack('<h', 1234)  # Little-endian signed short
        result = self.data_model.PtypInteger16(test_value)
        self.assertEqual(result, 1234)
        
        # Test negative number
        test_value = struct.pack('<h', -5678)
        result = self.data_model.PtypInteger16(test_value)
        self.assertEqual(result, -5678)
        
        # Test zero
        test_value = struct.pack('<h', 0)
        result = self.data_model.PtypInteger16(test_value)
        self.assertEqual(result, 0)
        
        # Test max value for 16-bit signed integer
        test_value = struct.pack('<h', 32767)
        result = self.data_model.PtypInteger16(test_value)
        self.assertEqual(result, 32767)
        
        # Test min value for 16-bit signed integer
        test_value = struct.pack('<h', -32768)
        result = self.data_model.PtypInteger16(test_value)
        self.assertEqual(result, -32768)
    
    def test_ptyp_integer32(self):
        """Test PtypInteger32 method with Python 3 int.from_bytes."""
        # Test positive number
        test_value = struct.pack('<i', 123456789)  # Little-endian signed int
        result = self.data_model.PtypInteger32(test_value)
        self.assertEqual(result, 123456789)
        
        # Test negative number
        test_value = struct.pack('<i', -987654321)
        result = self.data_model.PtypInteger32(test_value)
        self.assertEqual(result, -987654321)
        
        # Test zero
        test_value = struct.pack('<i', 0)
        result = self.data_model.PtypInteger32(test_value)
        self.assertEqual(result, 0)
        
        # Test max value for 32-bit signed integer
        test_value = struct.pack('<i', 2147483647)
        result = self.data_model.PtypInteger32(test_value)
        self.assertEqual(result, 2147483647)
        
        # Test min value for 32-bit signed integer
        test_value = struct.pack('<i', -2147483648)
        result = self.data_model.PtypInteger32(test_value)
        self.assertEqual(result, -2147483648)
    
    def test_ptyp_multiple_integer16(self):
        """Test PtypMultipleInteger16 method - ensures no 'bytes' variable shadowing."""
        # Pack multiple 16-bit integers
        values = [100, -200, 300, -400, 0]
        test_value = b''.join(struct.pack('<h', v) for v in values)
        
        result = self.data_model.PtypMultipleInteger16(test_value)
        self.assertEqual(result, values)
        
        # Test empty data
        test_value = b''
        result = self.data_model.PtypMultipleInteger16(test_value)
        self.assertEqual(result, [])
        
        # Test single value
        test_value = struct.pack('<h', 42)
        result = self.data_model.PtypMultipleInteger16(test_value)
        self.assertEqual(result, [42])
    
    def test_ptyp_multiple_integer32(self):
        """Test PtypMultipleInteger32 method - ensures no 'bytes' variable shadowing."""
        # Pack multiple 32-bit integers
        values = [1000000, -2000000, 3000000, -4000000, 0]
        test_value = b''.join(struct.pack('<i', v) for v in values)
        
        result = self.data_model.PtypMultipleInteger32(test_value)
        self.assertEqual(result, values)
        
        # Test empty data
        test_value = b''
        result = self.data_model.PtypMultipleInteger32(test_value)
        self.assertEqual(result, [])
        
        # Test single value
        test_value = struct.pack('<i', 42424242)
        result = self.data_model.PtypMultipleInteger32(test_value)
        self.assertEqual(result, [42424242])
    
    def test_ptyp_multiple_floating32(self):
        """Test PtypMultipleFloating32 method - ensures no 'bytes' variable shadowing."""
        # Pack multiple 32-bit floats
        values = [1.5, -2.75, 3.14159, -0.001, 0.0]
        test_value = b''.join(struct.pack('<f', v) for v in values)
        
        result = self.data_model.PtypMultipleFloating32(test_value)
        # Use approximate equality for floating point
        for expected, actual in zip(values, result):
            self.assertAlmostEqual(actual, expected, places=5)
    
    def test_ptyp_multiple_floating64(self):
        """Test PtypMultipleFloating64 method - ensures no 'bytes' variable shadowing."""
        # Pack multiple 64-bit floats
        values = [1.5e10, -2.75e-10, 3.141592653589793, -0.0000001, 0.0]
        test_value = b''.join(struct.pack('<d', v) for v in values)
        
        result = self.data_model.PtypMultipleFloating64(test_value)
        # Use approximate equality for floating point
        for expected, actual in zip(values, result):
            self.assertAlmostEqual(actual, expected, places=10)
    
    def test_ptyp_multiple_integer64(self):
        """Test PtypMultipleInteger64 method - ensures no 'bytes' variable shadowing."""
        # Pack multiple 64-bit integers
        values = [9223372036854775807, -9223372036854775808, 0, 123456789012345]
        test_value = b''.join(struct.pack('<q', v) for v in values)
        
        result = self.data_model.PtypMultipleInteger64(test_value)
        self.assertEqual(result, values)
    
    def test_ptyp_multiple_time(self):
        """Test PtypMultipleTime method - ensures no 'bytes' variable shadowing."""
        # Create test timestamps (microseconds since 1601-01-01)
        base_time = datetime(1601, 1, 1)
        test_dates = [
            datetime(2023, 1, 1, 12, 0, 0),
            datetime(2024, 6, 15, 18, 30, 45),
            datetime(2025, 12, 31, 23, 59, 59)
        ]
        
        # Convert to microseconds since 1601
        values = []
        for dt in test_dates:
            delta = dt - base_time
            microseconds = int(delta.total_seconds() * 1e6) * 10  # Windows FILETIME units
            values.append(microseconds)
        
        test_value = b''.join(struct.pack('<q', v) for v in values)
        
        result = self.data_model.PtypMultipleTime(test_value)
        self.assertEqual(len(result), len(test_dates))
        
        # Verify the dates are close to expected (allowing for precision loss)
        for expected, actual in zip(test_dates, result):
            diff = abs((expected - actual).total_seconds())
            self.assertLess(diff, 1.0)  # Within 1 second tolerance
    
    def test_ptyp_multiple_floating_time(self):
        """Test PtypMultipleFloatingTime method - ensures no 'bytes' variable shadowing."""
        # Floating time is days since December 30, 1899
        base_date = datetime(1899, 12, 30)
        test_dates = [
            datetime(2023, 1, 1),
            datetime(2024, 6, 15),
            datetime(2025, 12, 31)
        ]
        
        # Convert to days since base date
        values = []
        for dt in test_dates:
            delta = dt - base_date
            days = delta.total_seconds() / 86400.0
            values.append(days)
        
        test_value = b''.join(struct.pack('<d', v) for v in values)
        
        result = self.data_model.PtypMultipleFloatingTime(test_value)
        self.assertEqual(len(result), len(test_dates))
        
        # Verify the dates are correct (allowing for time component)
        for expected, actual in zip(test_dates, result):
            self.assertEqual(expected.date(), actual.date())
    
    def test_ptyp_multiple_guid(self):
        """Test PtypMultipleGuid method - ensures no 'bytes' variable shadowing."""
        # Create test GUIDs (16 bytes each)
        guids = [
            b'\x01' * 16,
            b'\x02' * 16,
            b'\x03' * 16,
            b'\xFF' * 16
        ]
        test_value = b''.join(guids)
        
        result = self.data_model.PtypMultipleGuid(test_value)
        self.assertEqual(result, guids)
        
        # Test empty data
        test_value = b''
        result = self.data_model.PtypMultipleGuid(test_value)
        self.assertEqual(result, [])
    
    def test_get_multi_value_offsets(self):
        """Test get_multi_value_offsets function - ensures no 'bytes' variable shadowing."""
        # Test with single value (count = 1)
        test_value = struct.pack('<I', 1) + b'\x00' * 20  # count=1 plus padding
        count, offsets = get_multi_value_offsets(test_value)
        self.assertEqual(count, 1)
        self.assertEqual(offsets, [8, 24])  # Fixed offset for single value
        
        # Test with multiple values
        count_val = 3
        offset_values = [16, 32, 48]
        test_value = struct.pack('<I', count_val)  # Count
        for offset in offset_values:
            test_value += struct.pack('<Q', offset)  # Offsets
        test_value += b'\x00' * 20  # Some data
        
        count, offsets = get_multi_value_offsets(test_value)
        self.assertEqual(count, count_val)
        self.assertEqual(offsets[:-1], offset_values)  # Last offset is length of data
        self.assertEqual(offsets[-1], len(test_value))
    
    def test_ptyp_binary_preserves_null_bytes(self):
        """PtypBinary must return binary data unchanged, including embedded
        null bytes.

        Null bytes are significant content in binary properties (0x0102), not
        string padding. The PR_RTF_COMPRESSED body stream in particular carries
        legitimate 0x00 bytes in its LZFu header and compressed payload;
        stripping them shifts the header and makes compressed_rtf raise
        "Unknown type of RTF compression!". Upstream still strips here, so this
        guards against the bug being reintroduced on a re-sync.
        """
        # Shape mirrors a real LZFu compressed-RTF header (length, 'LZFu' magic
        # at offset 8, CRC) -- full of meaningful null bytes.
        value = b"\x85\x00\x00\x00\x09\x01\x00\x00LZFu\x21\x00\x21\xb4\x00\x00"
        result = self.data_model.PtypBinary(value)
        self.assertEqual(result, value)
        self.assertEqual(result.count(b"\x00"), value.count(b"\x00"))

    def test_get_value_with_data_type_name(self):
        """Test get_value method using data_type_name parameter."""
        # Test with PtypInteger32
        test_value = struct.pack('<i', 42)
        result = self.data_model.get_value(test_value, data_type_name='PtypInteger32')
        self.assertEqual(result, 42)
        
        # Test with PtypString (UTF-16LE)
        test_string = "Hello, World!"
        test_value = test_string.encode('utf-16-le')
        result = self.data_model.get_value(test_value, data_type_name='PtypString')
        self.assertEqual(result, test_string)
        
        # Test with PtypBoolean
        test_value = struct.pack('B', 1)
        result = self.data_model.get_value(test_value, data_type_name='PtypBoolean')
        self.assertTrue(result)
        
        test_value = struct.pack('B', 0)
        result = self.data_model.get_value(test_value, data_type_name='PtypBoolean')
        self.assertFalse(result)
    
    def test_helper_functions(self):
        """Test standalone helper functions."""
        # Test get_time
        microseconds = 13288896000000000 * 10  # Some date in Windows FILETIME
        test_value = struct.pack('<q', microseconds)
        result = get_time(test_value)
        self.assertIsInstance(result, datetime)
        self.assertGreater(result, datetime(1601, 1, 1))
        
        # Test get_floating_time
        days = 45000.5  # Days since 1899-12-30
        test_value = struct.pack('<d', days)
        result = get_floating_time(test_value)
        self.assertIsInstance(result, datetime)
        self.assertGreater(result, datetime(1899, 12, 30))


if __name__ == '__main__':
    unittest.main()
