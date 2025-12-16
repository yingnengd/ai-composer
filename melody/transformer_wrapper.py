import torch
import random

class MusicTransformerWrapper:
    """
    统一接口：
    输入：上下文（degree / token）
    输出：下一个 scale degree（1~7）
    """

    def __init__(self, model=None, tokenizer=None, device="cpu"):
        self.model = model
        self.tokenizer = tokenizer
        self.device = device

    def predict_next_degree(self, context_degrees):
        """
        context_degrees: [1,5,6,5,...]
        """

        # 👉 1. 还没接模型 = fallback
        if self.model is None:
            return random.choices(
                population=[1,2,3,4,5,6],
                weights=[0.22,0.05,0.10,0.06,0.28,0.20]
            )[0]

        # 👉 2. degrees → tokens
        tokens = self.tokenizer.degrees_to_tokens(context_degrees)
        tokens = torch.tensor(tokens).unsqueeze(0).to(self.device)

        # 👉 3. Transformer 推理
        with torch.no_grad():
            logits = self.model(tokens)
            next_token = self.sample(logits[:, -1, :])

        # 👉 4. token → degree
        return self.tokenizer.token_to_degree(next_token)

    def sample(self, logits, temperature=1.0):
        probs = torch.softmax(logits / temperature, dim=-1)
        return torch.multinomial(probs, num_samples=1).item()
