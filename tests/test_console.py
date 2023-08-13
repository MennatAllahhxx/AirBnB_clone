#!/usr/bin/python3
"""
this is 'test_console' module

unittest for 'console' module
"""
import unittest
from models import storage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    a class to test HBNBCommand class and its methods
    """

    def test_class_doctest(self):
        """
        test to check doctest of class
        :return: nth
        """
        self.assertTrue(len(HBNBCommand.__doc__) > 1)

    def setUp(self):
        """Initializing the unittest
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after the test
        """
        pass

    def test_do_EOF(self):
        """Test to check EOF command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue(), "")

    def test_do_help(self):
        """Test to check help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            self.assertIn("help", output)
            self.assertIn("EOF", output)
            self.assertIn("quit", output)
            self.assertIn("create", output)
            self.assertIn("count", output)
            self.assertIn("show", output)
            self.assertIn("destroy", output)
            self.assertIn("all", output)
            self.assertIn("update", output)

    def test_do_quit(self):
        """Test to check quit command
        """
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_do_create(self):
        """Test to check create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)
            self.assertNotEqual(output, "** class name missing **")
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_do_count(self):
        """Test to check count command
        """
        count = 0
        for key, values in storage.all().items():
            name = key.split(".")
            if name[0] == 'BaseModel':
                count += 1
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, str(count))

    def test_do_show(self):
        """Test to check show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "** class name missing **")
            self.assertNotEqual(output, "** class doesn't exist **")
            self.assertNotEqual(output, "** instance id missing **")
            self.assertNotEqual(output, "** no instance found **")

    def test_do_destroy(self):
        """Test to check destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "** class name missing **")
            self.assertNotEqual(output, "** class doesn't exist **")
            self.assertNotEqual(output, "** instance id missing **")
            self.assertNotEqual(output, "** no instance found **")

    def test_do_all(self):
        """Test to check all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_do_update(self):
        """Test to check update command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'basemodel'")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "** class name missing **")
            self.assertNotEqual(output, "** class doesn't exist **")
            self.assertNotEqual(output, "** instance id missing **")
            self.assertNotEqual(output, "** attribute name missing **")
            self.assertNotEqual(output, "** value missing **")
            self.assertNotEqual(output, "** no instance found **")

    def test_default(self):
        """Test to check default method
         """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show()")  # Using an example command
            output = f.getvalue().strip()
            self.assertNotEqual(output, "** Unknown syntax:")

    def test_emptyline(self):
        """Test to check emptyline method
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")  # Pressing enter
            self.assertEqual(f.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
