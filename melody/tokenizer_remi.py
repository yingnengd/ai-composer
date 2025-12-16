class DegreeTokenizer:
    """
    把模型 token 映射到 scale degree（1~7）
    """

    def __init__(self, vocab):
        self.vocab = vocab
        self.note_tokens = {
            "C": 1, "D": 2, "E": 3,
            "F": 4, "G": 5, "A": 6,
            "B": 7
        }

    def degrees_to_tokens(self, degrees):
        # degree → NOTE_ON
        tokens = []
        for d in degrees:
            note = self.degree_to_note(d)
            tokens.append(self.vocab[f"NOTE_ON_{note}"])
        return tokens

    def token_to_degree(self, token):
        note = self.vocab.inverse[token]
        return self.note_tokens[note[-1]]

    def degree_to_note(self, degree):
        return list(self.note_tokens.keys())[degree - 1]
