import pytest
import re
from my_code import generate_directed_graph, calc_shortest_path

wordsRegex = re.compile(r'\w+')
with open('text.txt', 'r') as f:
    text = f.read()

content = wordsRegex.findall(text)
G = generate_directed_graph(content)

@pytest.mark.parametrize("input1, input2, expected_output",[
    ('take', 'shower', 6),
    ('take', 'eat', None),
    ('eat', 'take', None),
    ('one', 'eat', None),
    ('forty', 'five', None)
])

def test_calc_shortest_path(input1, input2, expected_output):
    result = calc_shortest_path(input1, input2)
    assert result == expected_output