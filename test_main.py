from tkinter import END
from typing import List
from unittest import main, mock, TestCase

from main import add_item


class MainTest(TestCase):
    task_filename: str = 'tasks.txt'

    def setUp(self):
        super(MainTest, self).setUp()

    def tearDown(self):
        super(MainTest, self).tearDown()

    def _setup_tasks(self, items: List[str]):
        """Set up our tasks.txt file with the given list of tasks"""
        with open(self.task_filename, 'w') as f:
            for item in items:
                f.write('\n' + item)

    def _read_tasks(self) -> List[str]:
        """Read our tasks from tasks.txt and return a list of strings"""
        with open(self.task_filename, 'r') as f:
            return [
                line.rstrip()
                for line in f.readlines()
                if len(line.rstrip()) > 0
            ]

    def test_add_item(self):
        self._setup_tasks(['one', 'two', 'three'])

        entry = mock.MagicMock()
        entry.get = mock.MagicMock(return_value='four')
        listbox = mock.MagicMock()

        add_item(entry, listbox)

        self.assertEqual(self._read_tasks(), ['one', 'two', 'three', 'four'])
        listbox.insert.assert_called_with(END, 'four')



if __name__ == '__main__':
    main()
