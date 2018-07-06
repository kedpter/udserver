
import unittest
from unittest.mock import patch, mock_open

import pjutils


class TestEditor(unittest.TestCase):

    """Test case docstring."""

    def test_editline_with_regex(self):
        test_data = ("# import os\n"
                     "# import sys\n"
                     "# sys.path.insert(0, os.path.abspath('.'))\n")

        with patch('pjutils.open', mock_open(read_data=test_data), create=True) as m:
            self.editor = pjutils.Editor('foo')

        self.editor.editline_with_regex(r'^# import os', 'import os')
        self.assertEqual(self.editor._swp_lines[0], 'import os')


class TestProjectInfo(unittest.TestCase):

    """Test ProjectInfo Class"""

    def setUp(self):
        self.pjinfo = pjutils.ProjectInfo()

    def tearDown(self):
        pass

    def test_init(self):
        pjinfo = self.pjinfo
        self.assertEqual(pjinfo.author_fakename, 'kedpter')
        # self.assertEqual(pjinfo.author_truename, '')
        # self.assertEqual(pjinfo.email, '')
        # self.assertEqual(pjinfo.project_name, '')
        # self.assertEqual(pjinfo.project_version, '')


class TestSphinx(unittest.TestCase):

    """Docstring for TestSphinx. """

    def setUp(self):
        self.pjinfo = pjutils.ProjectInfo()
        self.sphinx = pjutils.Sphinx(self.pjinfo)

    def test_init(self):
        sphinx = self.sphinx

        self.expected_code_fpath = ''
        self.test_code_fdpath = sphinx.code_fdpath

        # self.assertEqual(self.test_code_fdpath, self.expected_code_fpath)

    def test_sphinx_quickstart_cmd(self):
        sphinx = self.sphinx
        expected_cmd = 'sphinx-quickstart docs -p easyenv -a kedpter -v 0.1.0 -r 0.1.0 -l en --ext-autodoc --makefile --quiet'

        self.assertEqual(' '.join(sphinx.sphinx_quickstart_cmd), expected_cmd)

    def test_all(self):
        sphinx = self.sphinx

        sphinx.quickstart()
        sphinx.gen_code_api()
        sphinx.rst2html()


class TestPyOfflineDist(unittest.TestCase):

    """Test PyOfflineDist"""

    def setUp(self):
        self.pod = pjutils.PyOfflineDist()
        pass

    def tearDown(self):
        pass

    def test_freeze_deps(self):
        self.pod.freeze_deps()

    def test_download_deps(self):
        self.pod.download_deps()
        print(' '.join(self.pod._download_deps_cmd))

    def test_install_deps(self):
        self.pod.install_deps()

    def test_clean_deps(self):
        self.pod.clean_deps()

    # python -m unittest test_pjutils.TestPyOfflineDist.test_pyinstaller_mkbinary
    def test_pyinstaller_mkbinary(self):
        self.pod.pyinstaller_mkbinary('cli.py')
        pass

    def test_clean(self):
        self.pod.clean_binary()
        pass


if __name__ == '__main__':
    unittest.main()
