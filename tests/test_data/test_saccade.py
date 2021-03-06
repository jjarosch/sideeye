from sideeye import Point, Fixation, Saccade, Region, Item, Trial, Experiment

from nose2.tools import such

class TestData(object):

    @classmethod
    def setUp(cls):
        it.testdata = True

    @classmethod
    def tearDown(cls):
        del it.testdata

with such.A('Saccade') as it:
    @it.has_test_setup
    def setup():
        it.fix1 = Fixation(Point(1, 2), 3, 4)
        it.fix2 = Fixation(Point(1, 2), 5, 6)

    @it.should('only allow valid saccades')
    def test_saccade_validation():
        with it.assertRaises(ValueError):
            Saccade(-10, False, it.fix1, it.fix2)
        with it.assertRaises(ValueError):
            Saccade(-100, True, it.fix1, it.fix2)

    @it.should('have equality defined correctly')
    def test_saccade_equality():
        it.assertTrue(Saccade(10, True, it.fix1, it.fix2) == Saccade(10, True, it.fix1, it.fix2))
        it.assertTrue(Saccade(10, False, it.fix1, it.fix2) != Saccade(50, False, it.fix1, it.fix2))
        it.assertTrue(Saccade(10, False, it.fix1, it.fix2) != Saccade(10, True, it.fix1, it.fix2))

it.createTests(globals())
