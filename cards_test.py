import gym_cards
import gymnasium as gym
import re

from math_verify import parse, verify
from math_verify.parser import ExprExtractionConfig

env = gym.make('gym_cards/Points24-v0')

observation, info = env.reset()

equation_str = "(3*6)+6"
answer_str = "24"

numbers = re.findall(r'\d+', equation_str)
numbers = [int(num) for num in numbers]

print(numbers)

for number in numbers:
    if number not in info['Numbers']:
        print(f"illegal number {number}")

# Parse the expressions using ExprExtractionConfig
equation = parse(equation_str, extraction_config=[ExprExtractionConfig()])
answer = parse(answer_str, extraction_config=[ExprExtractionConfig()])

print(verify(equation, answer))

print(info)

from PIL import Image

print(type(observation))

img = Image.fromarray(observation)

img.save("test.png")