import random
import time

count = 0

riddles = {
    "What has a face and two hands, but no arms or legs?": ["clock", "watch", "pressure gauge"],
    "What gets wetter the more it dries?": ["towel", "sponge", "dishcloth", "paper towel"],
    "What belongs to you, but other people use it much more than you do?": ["name", "phone number", "username", "reputation"],
    "What can travel around the world while remaining stuck in a single corner?": ["stamp", "postage stamp"],
    "What goes up but never comes down?": ["age", "height", "the year", "smoke", "prices"],
    "I am so fragile that if you say my name, you break me. What am I?": ["silence"],
    "The person who makes it has no need of it; the person who buys it has no use for it. The person who uses it can neither see nor feel it. What is it?": ["coffin", "casket", "tombstone"],
    "What has a head and a tail, but no body?": ["coin", "comet"],
    "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?": ["map", "globe", "atlas"],
    "Forward I am heavy, but backward I am not. What am I?": ["ton"],
    "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?": ["echo", "wind chime"],
    "The more you take, the more you leave behind. What are they?": ["footsteps", "footprints", "photographs", "memories"],
    "What is lighter than a feather, yet even the strongest person cannot hold it for more than five minutes?": ["breath", "your breath"],
    "A box without hinges, key, or lid, yet golden treasure inside is hid. What is it?": ["egg"],
    "I feed on everything: air, earth, plants, and beast. I bite through steel, gnaw through iron, and grind hard stones to meal. What am I?": ["time", "rust", "decay"],
}

#randomising riddles
riddles_list = list(riddles.items())

random.shuffle(riddles_list)

randomised_riddles = dict(riddles_list)

#riddle algorithm
for riddle, answer in randomised_riddles.items():
    user_input = input(f"{riddle}: Answer: (ONE WORD ONLY) ").lower().strip()

    if user_input in answer:
        print("\nCorrect!")
        count += 1
    else:
        print(f"\nIncorrect... The correct answer(s) was: {', '.join(answer)}.")

#calculation
print("Let me calculate your results...")
for i in range(1, 5):
    time.sleep(1)
    print("." * i)

total = 100 * (count/len(riddles))
print(f"You got a {total:.1f}%!")