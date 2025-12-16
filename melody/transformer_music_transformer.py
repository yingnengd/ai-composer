import torch
from melody.constraint_sampler import constrained_sample

class MusicTransformerAdapter:
    def __init__(self, model, tokenizer, device="cpu"):
        self.model = model.to(device)
        self.model.eval()
        self.tokenizer = tokenizer
        self.device = device

    def predict_next_degree(self, history_degrees):
        # degree → token
        tokens = [
            self.tokenizer.degree_to_token(d)
            for d in history_degrees[-16:]  # 上下文窗口
        ]

        token_ids = self.encode(tokens)

        with torch.no_grad():
            logits = self.model(token_ids)
            probs = torch.softmax(logits[:, -1], dim=-1)
            topk = torch.topk(probs, k=8)

        candidates = [
            self.tokenizer.token_to_degree(self.decode(i))
            for i in topk.indices[0]
            if self.tokenizer.token_to_degree(self.decode(i)) is not None
        ]

        return constrained_sample(
            candidates,
            last_degree=history_degrees[-1],
            last_interval=abs(history_degrees[-1] - history_degrees[-2])
        )

    def encode(self, tokens):
        # TODO: 接原仓库 vocab
        ids = [self.model.vocab[token] for token in tokens]
        return torch.tensor(ids).unsqueeze(0).to(self.device)

    def decode(self, token_id):
        return self.model.inv_vocab[token_id]
