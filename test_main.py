from typing import List
from unittest import main, mock, TestCase

from tkinter import ACTIVE, END

from main import add_item, delete_item, load_tasks


class MainTest(TestCase):
    task_filename: str = 'tasks.txt'

    def setUp(self):
        super(MainTest, self).setUp()
        self.delete_called = False

    def tearDown(self):
        super(MainTest, self).tearDown()

    def _setup_tasks(self, items: List[str]):
        """Set up our tasks.txt file with the given list of tasks"""
        with open(self.task_filename, 'w') as f:
            for item in items:
                f.write(item + '\n')

    # def _read_tasks(self) -> List[str]:
    #     """Read our tasks from tasks.txt and return a list of strings"""
    #     with open(self.task_filename, 'r') as f:
    #         # for line in f.readlines():
    #         #   if len(line.rstrip)) > 0:
    #         #     lines.append(line.rstrip())                
    #         # return lines
    #         return [
    #             line.rstrip()
    #             for line in f.readlines()
    #             if len(line.rstrip()) > 0
    #         ]
    def assertTasks(self, tasks:List[str]):
        expected_string = "".join((f'{task}\n' for task in tasks))
        with open(self.task_filename, 'r') as f:
            actual_string = f.read()
        self.assertEqual(actual_string, expected_string)



    def test_add_item(self):
        self._setup_tasks(['one', 'two', 'three'])

        entry = mock.Mock()
        entry.get = mock.Mock(return_value='four')
        listbox = mock.Mock()

        add_item(entry, listbox)

        # self.assertEqual(self._read_tasks(), ['one', 'two', 'three', 'four'])
        self.assertTasks(['one', 'two', 'three', 'four'])
        listbox.insert.assert_called_with(END, 'four')

    # def test_delete_item_whitespace(self):
    #     self._setup_tasks(['one', 'two', 'three'])

    #     listbox = mock.Mock()
        
    #     def call_back(index):
    #         if index == ACTIVE and not self.delete_called:
    #             return 'two\n'
    #         return None

    #     def del_call(index):
    #         if index == ACTIVE:
    #             self.delete_called = True

    #     listbox.delete = mock.Mock(side_effect = del_call)
    #     listbox.get = mock.Mock(side_effect=call_back)

    #     delete_item(listbox)

    #     # self.assertEqual(self._read_tasks(), ['one', 'three'])
    #     self.assertTasks(['one', 'three'])

    def test_delete_item(self):
        self._setup_tasks(['one', 'two', 'three'])

        listbox = mock.Mock()
        def call_back(index):
            if index == ACTIVE and not self.delete_called:
                return 'two'
            return None

        def del_call(index):
            if index == ACTIVE:
                self.delete_called = True

        listbox.delete = mock.Mock(side_effect = del_call)
        listbox.get = mock.Mock(side_effect=call_back)

        delete_item(listbox)

        # self.assertEqual(self._read_tasks(), ['one', 'three'])
        self.assertTasks(['one', 'three'])
    
    def test_load_tasks(self):
        self._setup_tasks(['one', 'two', 'three'])

        listbox = mock.Mock()
        load_tasks(listbox)
        listbox.insert.assert_has_calls([
            mock.call(END, 'one'),
            mock.call(END, 'two'),
            mock.call(END, 'three')
        ])
        




if __name__ == '__main__':
    main()
