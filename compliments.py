import random

adjectives = ["amazing", "awesome", "brilliant", "crazy", "fantastic", "groovy", "incredible", "marvelous", "outstanding", "splendid", "wonderful"]
nouns = ["champion", "genius", "legend", "master", "ninja", "rockstar", "superstar", "wizard"]

def generate_compliment():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"You are a {adjective} {noun}!"

for _ in range(5):
    compliment = generate_compliment()
    print(compliment)
