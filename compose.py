#!/usr/bin/env python 

import string
import random

from graph import Graph, Vertex

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
    previous_words: list[Vertex] = []

    for word in words:
        word_vertex = g.get_vertex(word)

        if previous_words:
            previous_words[0].increment_edge(word_vertex)
            
            if len(previous_words) > 1:
                previous_words[1].increment_edge2(word_vertex)
                previous_words.pop()

        previous_words.insert(0, word_vertex)

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
