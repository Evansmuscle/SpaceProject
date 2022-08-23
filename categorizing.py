limits = {
    "Iron": 500000,
    "Silver": 50000,
    "Gold": 30000,
    "Platinum": 20000,
}

class Categorizer:
    @staticmethod
    def categorize(asteroids):
        for asteroid in asteroids:
            for metal in asteroid.metals:
                if limits[metal[0]] and limits[metal[0]] <= metal[1]:
                    asteroid.worth = True
                    continue
                asteroid.worth = False
                break
