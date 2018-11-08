

import unittest
from tdd import check_order_status


class TestOrder(unittest.TestCase):
    """test for status of delivery"""
    def test_order_status(self):
        order_id = 2
        self.assertEqual(check_order_status(order_id),True)

    def test_order_status_mising(self): # this is false because this order_id doesn't exist in the list
        order_id = 0
        self.assertEqual(check_order_status(order_id),False)
    
    def test_order_status_is_int(self):
        order_id = "str"
        self.assertFalse(check_order_status(order_id),False)
    
    def test_order_exists(self):
        order_id = 1
        self.assertEqual(check_order_status(order_id),True)

    def test_for_adding_new_order(self):
        # order_id = 2
        # self.assertIn
        pass

    def test_for_marking_order_delivered(self):
        pass

    def test_order_added_to_list(self):
        pass

    def test_input_is_integer(self):
        pass

    def test_order_id_doesnot_exist_in_both_lists(self):
        pass