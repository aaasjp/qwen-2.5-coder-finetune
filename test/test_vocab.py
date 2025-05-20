from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("/Users/ailabuser7-1/Documents/cursor-workspace/qwen-2.5-coder-finetune/finetuning/sft/checkpoints/sft_model/7B")
vocab = tokenizer.get_vocab()
#print(vocab)

# 打印vocab中每个token的详细信息
'''
for token, idx in vocab.items():
    print(f"Token: {token}, Index: {idx}")
'''

text = "你好，我是通义千问，由通义实验室开发。"

tokens = tokenizer(text)
print(tokens)

tokens = tokenizer.encode(text)
print(tokens)

text = tokenizer.decode(tokens)
print(text)
