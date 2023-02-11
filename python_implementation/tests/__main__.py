import unittest
from utils.swap import swap
from utils.calculate_parent_index import calculate_parent_index
from utils.heapify_up import heapify_up
from utils.calculate_child_indices import calculate_child_indices
from utils.heapify_down import heapify_down
from utils.generate_longest_ancestry import generate_longest_ancestry
class TestUtils(unittest.TestCase):
  def test_swap_util(self):
    sampleArray = ['a', 'b', 'c', 'd', 'e']
    swappedArray = swap(sampleArray, 1, 3)
    self.assertTrue(swappedArray[1] == 'd' and swappedArray[3] == 'b')
  def test_parent_index_calculation(self):
    parent_index1 = calculate_parent_index(11, 2)
    parent_index2 = calculate_parent_index(14, 2)
    parent_index3 = calculate_parent_index(21, 2)
    parent_index4 = calculate_parent_index(25, 3)
    parent_index5 = calculate_parent_index(24, 3)
    parent_index6 = calculate_parent_index(21, 3)
    self.assertTrue(parent_index1 == 3 and parent_index2 == 4 and parent_index3 == 5 and parent_index4 == 3 and parent_index5 == 3 and parent_index6 == 3)
  def test_heapify_up(self):
    test_heapified_array = heapify_up([None, 1, 9, 2, 3], 4, 4, 1)
    self.assertTrue(test_heapified_array == [None, 3, 9, 2, 1])
  def test_child_indices_generation(self):
    child_indices_power2 = calculate_child_indices(3, 2, 13)
    child_indices_power3 = calculate_child_indices(2, 3, 18)
    self.assertTrue(child_indices_power2 == [10, 11, 12] and child_indices_power3 == [10, 11, 12, 13, 14, 15, 16, 17])
  def test_heapify_down(self):
    heapify_down_test_array = [None, 1000, 500, 800, 700, 900, 850, 650, 620, 630, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 610, 615, 612]
    down_heapified_array = heapify_down(heapify_down_test_array, 2, 2)
    self.assertTrue(down_heapified_array == [None, 1000, 850, 800, 700, 900, 615, 650, 620, 630, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 610, 500, 612])
  def longest_ancestry_test(self):
    squared_ancestry = generate_longest_ancestry(2, 18)
    unary_ancestry = generate_longest_ancestry(1,19)
    self.assertTrue(squared_ancestry==[4] and unary_ancestry==[2,4,9])
if __name__ == '__main__':
    unittest.main(verbosity=2)