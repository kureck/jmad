from django.test import TestCase

from jmad.solos.models import Solo


class SoloModelTestCase(TestCase):

    def setUp(self):
        self.solo = Solo.objects.create(
            track='Falling in love with love',
            artist='Oscar Peterson',
            instrument='piano'
        )

        self.drum_solo = Solo.objects.create(
           instrument='drums',
           artist='Rich',
           track='Bugle Call Rag'
        )

        self.bass_solo = Solo.objects.create(
            instrument='saxophone',
            artist='Coltrane',
            track='Mr. PC'
        )

    def test_solo_basic(self):
        """
        Test the basic functionality of Solo
        """
        self.assertEqual(self.solo.artist, 'Oscar Peterson')
