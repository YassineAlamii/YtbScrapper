from youtube_scrapper import Scrapper
import unittest

class TestScrapingMethods(unittest.TestCase):

    def testTitre(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("fQdAcoMoItI")
        expectedTitre = "Interview m3a Younes Filali "Youne99s" - Streamer Fifa 21"
        titre = scrapper.getTitre()
        self.assertEqual(titre, expectedTitre)

   def testVideaste(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("fQdAcoMoItI")
        expectedVideaste = "Lgaming"
        videaste = scrapper.getVideaste()
        self.assertEqual(videaste, expectedVideaste)

    def testPoucesBleu(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("fQdAcoMoItI")
        expectedPoucesBleu = "569"
        poucesBleu = scrapper.getPoucesBleu()
        self.assertEqual(poucesBleu, expectedPoucesBleu)


    def testDescription(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("fQdAcoMoItI")
        expectedDescription = "L'equipe lgamingma a accueilli récemment le streameur de fifa 21 Younes Filali, vous allez découvrir sa passion ses objectifs et sa spontanéité, bon visionnage !
don't forget to Follow  our guest : Youtube : https://www.youtube.com/channel/UCutd...Twitch : https://www.twitch.tv/youne99s #fifa21 #fut #teamoftheyear "
        description = scrapper.getDescription()
        self.assertEqual(description, expectedDescription)


    def testLiens(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("fQdAcoMoItI")
        expectedLiens = [
            "https://www.https://www.youtube.com/channel/UCutdrshx5sQvO3JxrhFxiPA",
            "https://www.twitch.tv/youne99s"
        ]
        liens = scrapper.getLiens()
        self.assertEqual(liens, expectedLiens)


    def testId(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("fQdAcoMoItI")
        expectedId = "fQdAcoMoItI"
        id = scrapper.getId()
        self.assertEqual(id, expectedId)


    def testComments(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("fQdAcoMoItI")
        expectedComments = [
            "Ethrari😂😂",
            "Welcome back Lgaming -",
            "BIEEEEEEEEEEEEEEEEEN JOUUUUUUUEEEEEE",
            "Big UPP Youne99s  👏👍",
            "nice intro",
            "👍🏼👍🏼",
            "🔥🔥🔥",
            "❤🔥",
            "Ooooooh (youness's voice))",
            "💕💕💕"
            
        ]
        comments = scrapper.getComments(10)
        self.assertEqual(comments, expectedComments)


