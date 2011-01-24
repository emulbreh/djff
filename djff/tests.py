from djff.diff import UnifiedDiff
from django.test import TestCase

class DjffTest(TestCase):
    diff0 = """
--- foo.txt	(r0)
+++ foo2.txt	(r1)
@@ -1,7 +1,7 @@
-f fo foo
+f fo fou
 --------
 --------
-b ba bar
+b ba baz
 --------
 --------
-b ba baz
+silly test
""".strip()

    def test_udiff(self):
        d = UnifiedDiff(self.diff0)
        self.assertEqual(len(d), 1)
        dl = list(d)
        self.assertEqual(len(dl[0]['chunks']), 1)
        self.assertEqual(dl[0]['new_revision'], '(r1)')
        self.assertEqual(dl[0]['old_revision'], '(r0)')
        
        lines = dl[0]['chunks'][0]
        self.assertEqual(len(lines), 10)
        self.assertEqual(lines[0]['command'], '-')
        self.assertEqual(lines[0]['line'], 'f fo fo<del>o</del>')
        self.assertEqual(lines[1]['command'], '+')
        self.assertEqual(lines[1]['line'], 'f fo fo<ins>u</ins>')
        self.assertEqual(lines[2]['command'], ' ')
        self.assertEqual(lines[2]['line'], '--------')

        
