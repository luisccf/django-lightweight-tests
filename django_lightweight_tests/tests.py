import unittest
from io import StringIO
from unittest import TestCase, mock

from django.conf import settings
from lightweight_test import LightweightTest


class AddOptionTestCase(TestCase):
    def test_should_instantiate_option_class(self):
        option_class = mock.Mock()
        LightweightTest().add_option(option_class)
        option_class.assert_called_once()

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_should_print_msg_when_verbosity_1(self, mock_stdout):
        option_class = mock.Mock()
        option_class.return_value.msg = 'msg'
        LightweightTest.option_classes = [option_class]
        LightweightTest(verbosity=1)
        self.assertEqual(mock_stdout.getvalue(), 'msg\n')

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_should_not_print_msg_when_verbosity_0(self, mock_stdout):
        option_class = mock.Mock()
        option_class.return_value.msg = 'msg'
        LightweightTest.option_classes = [option_class]
        LightweightTest(verbosity=0)
        self.assertEqual(mock_stdout.getvalue(), '')


class InitTestCase(TestCase):
    @mock.patch('lightweight_test.LightweightTest.add_option')
    def test_should_call_add_option_for_each_option_class(self, mock_add_option):
        LightweightTest.option_classes = [
            mock.Mock(),
            mock.Mock(),
            mock.Mock(),
        ]
        LightweightTest()
        self.assertEqual(mock_add_option.call_count, 3)

    @mock.patch('lightweight_test.LightweightTest.add_option')
    def test_should_call_add_option_with_option_class_as_arg(self, mock_add_option):
        LightweightTest.option_classes = [
            mock.Mock(),
            mock.Mock(),
            mock.Mock(),
        ]
        LightweightTest()
        mock_add_option.assert_has_calls([
            mock.call(LightweightTest.option_classes[0]),
            mock.call(LightweightTest.option_classes[1]),
            mock.call(LightweightTest.option_classes[2]),
        ])

if __name__ == '__main__':
    settings.configure()
    unittest.main()
