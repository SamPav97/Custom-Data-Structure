from unittest import TestCase, main
from customlist.custom_list import CustomIntList, NoElementsInListError, NoSuchValueError


class TestCustomList(TestCase):
    def test_append_adds_element_at_end_of_list(self):
        custom_l = CustomIntList()
        self.assertEqual([], custom_l._CustomIntList__values)
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)

    def test_append_non_integer_raises(self):
        custom_l = CustomIntList()
        with self.assertRaises(ValueError) as ex:
            custom_l.append("sss")
        self.assertEqual("Only ints are accepted", str(ex.exception))

    def test_remove_el_invalid_index_raises(self):
        custom_l = CustomIntList()
        self.assertEqual([], custom_l._CustomIntList__values)
        with self.assertRaises(IndexError) as ex:
            custom_l.remove(0)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_pass_invalid_integer_index_raises(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)
        with self.assertRaises(ValueError) as ex:
            custom_l.remove("0")
        self.assertEqual("Index is not a valid integer. Please pass an integer number", str(ex.exception))

    def test_remove_element_removes_and_returns(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)
        returned_el = custom_l.remove(0)
        self.assertEqual([], custom_l._CustomIntList__values)
        self.assertEqual(5, returned_el)

    def test_get_returns_element(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)

        element = custom_l.get(0)
        self.assertEqual(5, element)
        self.assertEqual([5], custom_l._CustomIntList__values)

    def test_get_invalid_index_raises(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)

        with self.assertRaises(IndexError) as ex:
            custom_l.get(-2)
        self.assertEqual("Invalid index", str(ex.exception))

        # Right border
        with self.assertRaises(IndexError) as ex:
            custom_l.get(1)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_extend_appends_new_values(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)

        custom_l.extend([2, 3, 4])
        self.assertEqual([5, 2, 3, 4], custom_l._CustomIntList__values)

    def test_extend_non_int_raises(self):
        custom_l = CustomIntList()
        with self.assertRaises(ValueError) as ex:
            custom_l.extend([5, "10", 5])
        self.assertEqual("Only ints are accepted", str(ex.exception))

    def test_extend_with_non_iterable_raises(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)

        with self. assertRaises(ValueError) as ex:
            custom_l.extend(5)
        self.assertEqual("Extend method works only with iterable objects", str(ex.exception))

    def test_extend_returns_new_list(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)
        result_lst = custom_l.extend([2, 3, 4])
        self.assertEqual([5, 2, 3, 4], custom_l._CustomIntList__values)
        self.assertEqual([5, 2, 3 ,4], result_lst)
        self.assertNotEqual(id(result_lst), id(custom_l._CustomIntList__values))

    def test_insert_invalid_index_raises(self):
        custom_l = CustomIntList()
        self.assertEqual([], custom_l._CustomIntList__values)
        with self.assertRaises(IndexError) as ex:
            custom_l.insert(0, 5)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_invalid_index_dataa_type_insert_raises(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)
        with self.assertRaises(ValueError) as ex:
            custom_l.insert("0", 5)
        self.assertEqual("Index is not a valid integer. Please pass an integer number", str(ex.exception))

    def test_insert_returns_the_list_with_inserted_element(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(10)
        custom_l.append(15)
        self.assertEqual([5, 10, 15], custom_l._CustomIntList__values)

        my_lst = custom_l.insert(1, -3)
        self.assertEqual([5, -3, 10, 15], custom_l._CustomIntList__values)
        self.assertEqual(id(my_lst), id(custom_l._CustomIntList__values))

    def test_pop_with_no_elements_raises(self):
        custom_l = CustomIntList()
        self.assertEqual([], custom_l._CustomIntList__values)
        with self.assertRaises(NoElementsInListError) as ex:
            custom_l.pop()
        self.assertEqual("No Elements in list", str(ex.exception))

    def test_pop_removes_and_returns_el(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)

        el = custom_l.pop()
        self.assertEqual(5, el)
        self.assertEqual([], custom_l._CustomIntList__values)

    def test_clear_no_elements_returns_empty_list(self):
        custom_l = CustomIntList()
        custom_l.clear()
        self.assertEqual([], custom_l._CustomIntList__values)

    def test_clear(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(15)
        self.assertEqual([5, 15], custom_l._CustomIntList__values)
        custom_l.clear()
        self.assertEqual([], custom_l._CustomIntList__values)

    def test_index_left_returns_left_most_index_of_the_element(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(15)
        custom_l.append(5)

        index = custom_l.index_left(5)
        self.assertEqual(0, index)

    def test_index_right_returns_right_most_index_of_the_element(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(15)
        custom_l.append(5)

        index = custom_l.index_right(5)
        self.assertEqual(2, index)

    def test_index_left_invalid_value_raises(self):
        custom_l = CustomIntList()
        self.assertEqual([], custom_l._CustomIntList__values)
        with self.assertRaises(NoSuchValueError) as ex:
            custom_l.index_left(5)
        self.assertEqual("No such value in the list", str(ex.exception))

    def test_index_right_invalid_value_raises(self):
        custom_l = CustomIntList()
        self.assertEqual([], custom_l._CustomIntList__values)
        with self.assertRaises(NoSuchValueError) as ex:
            custom_l.index_right(5)
        self.assertEqual("No such value in the list", str(ex.exception))

    def test_count_no_such_value(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        self.assertEqual([5], custom_l._CustomIntList__values)

        count = custom_l.count(10)
        self.assertEqual(0, count)

    def test_count(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(10)
        custom_l.append(10)
        self.assertEqual([5, 10, 10], custom_l._CustomIntList__values)

        count = custom_l.count(5)
        self.assertEqual(1, count)
        count = custom_l.count(10)
        self.assertEqual(2, count)

    def test_reverse_empty_list_returns_list(self):
        custom_l = CustomIntList()
        self.assertEqual([], custom_l._CustomIntList__values)
        reversed_list = custom_l.reverse()
        self.assertEqual([], reversed_list)

    def test_reverse_reverses_values_in_list(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(10)
        custom_l.append(10)
        self.assertEqual([5, 10, 10], custom_l._CustomIntList__values)
        reversed_list = custom_l.reverse()
        # Old list remains the same, new reversed list is returned.
        self.assertEqual([5, 10, 10], custom_l._CustomIntList__values)
        self.assertEqual([10, 10, 5], reversed_list)

    def test_copy_returns_same_element_diff_list(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(10)
        custom_l.append(10)
        self.assertEqual([5, 10, 10], custom_l._CustomIntList__values)
        res = custom_l.copy()
        self.assertEqual([5, 10, 10], res)
        self.assertNotEqual(id(res), id(custom_l._CustomIntList__values))

    def test_size_returns_el_count(self):
        custom_l = CustomIntList()
        self.assertEqual([], custom_l._CustomIntList__values)
        size = custom_l.size()
        self.assertEqual(0, size)
        custom_l.append(5)
        custom_l.append(10)
        self.assertEqual([5, 10], custom_l._CustomIntList__values)
        size = custom_l.size()
        self.assertEqual(2, size)

    def test_add_first_no_el_append(self):
        custom_l = CustomIntList()
        self.assertEqual([], custom_l._CustomIntList__values)
        custom_l.add_first(5)
        self.assertEqual([5], custom_l._CustomIntList__values)

    def test_add_first_adds_el_in_front(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(10)
        self.assertEqual([5, 10], custom_l._CustomIntList__values)
        custom_l.add_first(-3)
        self.assertEqual([-3, 5, 10], custom_l._CustomIntList__values)

    def test_add_first_non_int_raises(self):
        custom_l = CustomIntList()
        with self.assertRaises(ValueError) as ex:
            custom_l.add_first("5")
        self.assertEqual("Only ints are accepted", str(ex.exception))

    def test_dictionize_odd_count(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(10)
        custom_l.append(15)

        # Odd values are
        result = custom_l.dictionize()
        expected_res = {5: 10, 15: " "}
        self.assertEqual(expected_res, result)

    def test_dictionize_even_count(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(10)
        # Even values are

        result = custom_l.dictionize()
        expected_res = {5: 10}
        self.assertEqual(expected_res, result)

    def test_move_moves_n_values_at_end(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(10)
        custom_l.append(15)
        custom_l.append(20)
        self.assertEqual([5, 10, 15, 20], custom_l._CustomIntList__values)

        res = custom_l.move(2)
        self.assertEqual([15, 20, 5, 10], custom_l._CustomIntList__values)
        self.assertEqual([15, 20, 5, 10], res)

    def test_sum(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(10)
        custom_l.append(15)
        custom_l.append(20)
        self.assertEqual([5, 10, 15, 20], custom_l._CustomIntList__values)

        res = custom_l.sum()
        self.assertEqual(50, res)

    def test_overbound(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(20)
        custom_l.append(15)
        custom_l.append(10)
        self.assertEqual([5, 20, 15, 10], custom_l._CustomIntList__values)

        maximum = custom_l.overbound()
        self.assertEqual(20, maximum)

    def test_underbound(self):
        custom_l = CustomIntList()
        custom_l.append(5)
        custom_l.append(20)
        custom_l.append(15)
        custom_l.append(10)
        self.assertEqual([5, 20, 15, 10], custom_l._CustomIntList__values)

        maximum = custom_l.underbound()
        self.assertEqual(5, maximum)


if __name__ == "__main__":
    main()