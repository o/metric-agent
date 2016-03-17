import sys
import unittest

from metricd import SystemCollector


# TODO: psutil mocks for collector, tests for reporters (mocking of requests and logging)

class TestMetricD(unittest.TestCase):
    def test_merge_dicts(self):
        collector = SystemCollector(10, 'localhost')
        self.assertDictEqual({'foo': 'bar', 'baz': 'bogus'}, collector.merge_dicts({'foo': 'bar'}, {'baz': 'bogus'}))

    def test_get_derived(self):
        collector = SystemCollector(10, 'localhost')
        self.assertEqual(0, collector.get_derived('foo', 10))
        self.assertEqual(1, collector.get_derived('foo', 20))
        self.assertEqual(10, collector.get_derived('foo', 120))

    def test_collect_load(self):
        collector = SystemCollector(10, 'localhost')
        r = collector.collect_load()
        self.assertEqual(len(r), 3)
        self.assertIn('load.shortterm', r)
        self.assertIn('load.midterm', r)
        self.assertIn('load.longterm', r)

    def test_collect_memory(self):
        collector = SystemCollector(10, 'localhost')
        r = collector.collect_memory()
        self.assertGreaterEqual(len(r), 5)
        self.assertIn('memory.percent', r)
        self.assertIn('memory.total', r)
        self.assertIn('memory.used', r)
        self.assertIn('memory.free', r)
        self.assertIn('memory.available', r)
        self.assertLessEqual(r['memory.percent'], 100)

    def test_collect_swap(self):
        collector = SystemCollector(10, 'localhost')
        r = collector.collect_swap()
        self.assertEqual(len(r), 4)
        self.assertIn('swap.percent', r)
        self.assertIn('swap.total', r)
        self.assertIn('swap.used', r)
        self.assertIn('swap.free', r)
        self.assertLessEqual(r['swap.percent'], 100)

    def test_collect_cpu(self):
        collector = SystemCollector(10, 'localhost')
        r = collector.collect_cpu()
        self.assertGreaterEqual(len(r), 6)
        self.assertIn('cpu.cores', r)
        self.assertIn('cpu.percent', r)
        self.assertIn('cpu.user', r)
        self.assertIn('cpu.nice', r)
        self.assertIn('cpu.system', r)
        self.assertIn('cpu.idle', r)
        self.assertGreaterEqual(r['cpu.cores'], 1)

    def test_collect_interfaces(self):
        collector = SystemCollector(10, 'localhost')
        r = collector.collect_interfaces()
        self.assertGreaterEqual(len(r), 8)

    def test_collect_io(self):
        collector = SystemCollector(10, 'localhost')
        r = collector.collect_io()
        self.assertGreaterEqual(len(r), 4)

    # TODO: Test for total
    def test_collect_connections(self):
        collector = SystemCollector(10, 'localhost')
        r = collector.collect_connections()
        if sys.platform.find('linux') != -1:
            self.assertEqual(len(r), 6)
