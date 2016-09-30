# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

import bob


class BobTests(unittest.TestCase):

    def test_stating_something(self):
        self.assertEqual(
            'Whatever.',
            bob.hey('Tom-ay-to, tom-aaaah-to.')
        ) #PASS

    def test_shouting(self):
        self.assertEqual(
            'Whoa, chill out!',
            bob.hey('WATCH OUT!')
        ) #PASS

    def test_asking_a_question(self):
        self.assertEqual(
            'Sure.',
            bob.hey('Does this cryogenic chamber make me look fat?')
        ) #PASS

    def test_asking_a_numeric_question(self):
        self.assertEqual(
            'Sure.',
            bob.hey('You are, what, like 15?')
        ) #PASS

    def test_talking_forcefully(self):
        self.assertEqual(
            'Whatever.',
            bob.hey("Let's go make out behind the gym!")
        ) #PASS

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            'Whatever.', bob.hey("It's OK if you don't want to go to the DMV.")
        ) #PASS

    def test_forceful_questions(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('WHAT THE HELL WERE YOU THINKING?')
        ) #PASS

    def test_shouting_numbers(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('1, 2, 3 GO!')
        ) #PASS

    def test_only_numbers(self):
        self.assertEqual(
            'Whatever.', bob.hey('1, 2, 3')
        ) #PASS

    def test_question_with_only_numbers(self):
        self.assertEqual(
            'Sure.', bob.hey('4?')
        ) #PASS

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            'Whoa, chill out!',
            bob.hey('ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!')
        ) #PASS

    def test_shouting_with_umlauts(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('ÜMLÄÜTS!')
        ) #PASS

    def test_calmly_speaking_with_umlauts(self):
        self.assertEqual(
            'Whatever.', bob.hey('ÜMLäÜTS!')
        ) #PASS

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('I HATE YOU')
        ) #PASS

    def test_statement_containing_question_mark(self):
        self.assertEqual(
            'Whatever.', bob.hey('Ending with ? means a question.')
        ) #PASS

    def test_prattling_on(self):
        self.assertEqual(
            'Sure.', bob.hey("Wait! Hang on. Are you going to be OK?")
        ) #PASS

    def test_silence(self):
        self.assertEqual(
            'Fine. Be that way!', bob.hey('')
        ) #PASS

    def test_prolonged_silence(self):
        self.assertEqual(
            'Fine. Be that way!', bob.hey('    \t')
        ) #PASS

    def test_starts_with_whitespace(self):
        self.assertEqual(
            'Whatever.', bob.hey('         hmmmmmmm...')
        ) #PASS

    def test_ends_with_whitespace(self):
        self.assertEqual(
            'Sure.', bob.hey('What if we end with whitespace?   ')
        ) #PASS

    def test_non_question_ends_with_whitespace(self):
        self.assertEqual(
            'Whatever.', bob.hey('This is a statement with trailing whitespace   ')
        ) #PASS

if __name__ == '__main__':
    unittest.main()
