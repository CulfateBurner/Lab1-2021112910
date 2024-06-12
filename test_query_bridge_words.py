import pytest
import re
from my_code import generate_directed_graph, query_bridge_words

wordsRegex = re.compile(r'\w+')
with open('text.txt', 'r') as f:
    text = f.read()

content = wordsRegex.findall(text)
G = generate_directed_graph(content)

@pytest.mark.parametrize("input1, input2, expected_output",[
    ('eat', 'take', None),
    ('have', 'one', ['have'])
])

def test_query_bridge_words(input1, input2, expected_output):
    result = query_bridge_words(input1, input2)
    assert result == expected_output

