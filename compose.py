#!/usr/bin/env python 

import string
import random

from graph import Graph

def get_words_from_text(text_path: str) -> list[str]:
    with open(text_path, 'r') as f:
        text = f.read()
        text = ' '.join(text.split())
        text = text.lower() # Make everything lowercase for comparison
        text = text.translate(str.maketrans('', '', string.punctuation)) # Remove all punctuation

    words = text.split()
    return words


def make_graph(words: list[str]) -> Graph:
    g = Graph()
    previous_word = None

    for word in words:
        word_vertex = g.get_vertex(word)

        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex

    g.generate_probability_mappings()

    return g


def compose(g: Graph, words: list[str], length: int = 50) -> list[str]:
    composition = []
    word = g.get_vertex(random.choice(words)) # Pick random word to start
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main() -> str:
    words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    g = make_graph(words)

    composition = compose(g, words, 50)
    return ' '.join(composition)


if __name__ == '__main__':
    print(main())
