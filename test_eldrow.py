from eldrow import pick_word, color_correct, color_inword, validate, WORD_LENGTH


def test_pick_word():
    word = pick_word()
    assert len(word) == WORD_LENGTH


def test_validate():
    word = "hello"
    guess = "hopla"
    expect = "".join([color_correct('h'), color_inword('o'), 'p', color_correct('l'), 'a'])
    assert validate(guess, word) == expect

