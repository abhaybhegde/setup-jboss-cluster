import unittest
import coverage

def run_all_unit_tests_and_display_coverage(self):
    """ Runs all the unit test and displays the code coverage."""

    cov = coverage.Coverage(omit='/usr/local/lib/*')
    cov.start()
    tests = unittest.TestLoader().discover('.',pattern='test_*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    cov.html_report()


if __name__=="__main__":
    run_all_unit_tests_and_display_coverage(None)


