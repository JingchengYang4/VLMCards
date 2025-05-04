import re
from typing import Dict, List

from mathruler.grader import extract_boxed_content, grade_answer

import re

from math_verify import parse, verify
from math_verify.parser import ExprExtractionConfig

def compute_score(predicts: List[str], ground_truths: List[str], format_weight: float = 0.1) -> List[Dict[str, float]]:
    scores = []
    for predict, ground_truth in zip(predicts, ground_truths):

        correct = False

        valid_numbers = list(map(int, ground_truth.split(',')))

        match = re.search(r"<equation>(.*?)</equation>", predict)
        if match:
            equation = match.group(1)
            numbers = re.findall(r'\d+', equation)
            numbers = [int(num) for num in numbers]

            correct = True

            for number in numbers:
                if number not in valid_numbers:
                    correct = False

            if correct:
                equation = parse(equation, extraction_config=[ExprExtractionConfig()])
                answer = parse("24", extraction_config=[ExprExtractionConfig()])

                correct = verify(equation, answer)

        score = 0
        if correct:
            score = 1

        scores.append(
            {
                "overall": score,
            }
        )

    return scores
