"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn("having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        rsvp_d = self.client.get("/")
        self.assertIn("Please RSVP", rsvp_d.data)
        self.assertNotIn("Magic Unicorn", rsvp_d.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        self.assertIn("Magic Unicorn", result.data)
        self.assertNotIn("Please RSVP", result.data)
    

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        rsvp_info = {"name": "Mel", "email": "mel@ubermelon.com".lower()}

        result = self.client.post("/rsvp", data=rsvp_info, follow_redirects=True)

        self.assertNotIn("Magic Unicorn", result.data)
        self.assertIn("Please RSVP", result.data)


if __name__ == "__main__":
    unittest.main()
