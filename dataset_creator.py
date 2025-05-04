import json
from datasets import Dataset, DatasetDict
from PIL import Image
from io import BytesIO
import json

import gym_cards
import gymnasium as gym
import re
from tqdm import tqdm


target_number = 24

images = []
numbers = []
prompt = []
answer = []

env = gym.make('gym_cards/Points24-v0')

total = 10000

for i in tqdm(range(total)):
    observation, info = env.reset()
    img = Image.fromarray(observation)
    buffer = BytesIO()
    img.save(buffer, format="png")  # Keep the same format (e.g., JPEG, PNG)
    image_bytes = buffer.getvalue()
    images.append([image_bytes])
    numbers.append({"numbers": info['Numbers']})
    prompt.append("<image>")

    numbers_list = ','.join(map(str, info['Numbers']))
    answer.append(numbers_list)

merged_dict = {
    "numbers": numbers,
    "prompt": prompt,
    "answer": answer,
    "images": images
}

ds = Dataset.from_dict(merged_dict)

split_ds = ds.train_test_split(test_size=0.2, seed=492)

train_dataset = split_ds['train']
test_dataset = split_ds['test']

train_dataset.to_parquet("train.parquet")
test_dataset.to_parquet("test.parquet")