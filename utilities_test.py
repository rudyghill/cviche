import unittest
import utilities


class TestUtilites(unittest.TestCase):
    def test_expand_to_list(self):
        # Define a sample input table
        input_table = [
            {"id": "1", "key": " apple , banana,  orange "},
            {"id": "2", "key": "  apple,banana,orange  "},
            {"id": "3", "key": "apple, banana,orange"},
        ]

        desired_table = [
            {"id": "1", "key": ["apple", "banana", "orange"]},
            {"id": "2", "key": ["apple", "banana", "orange"]},
            {"id": "3", "key": ["apple", "banana", "orange"]},
        ]

        # Call the function with the sample input table and key
        reformatted_table = utilities.expand_to_list(input_table, "key")

        # Print the original and reformatted tables for comparison
        print("Original Table:")
        print(input_table)
        print("Reformatted Table:")
        print(reformatted_table)

        # Assert statements to validate the correctness of the reformatted table
        assert reformatted_table == desired_table, "Test failed!"


if __name__ == "__main__":
    unittest.main()