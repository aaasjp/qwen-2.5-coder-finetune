#Process_prompt.txt和Process_reponse.txt分别是prompt和大模型返回response
#使用qwen2.5的tokenizer来计算Process_prompt_tokens和Process_reponse_tokens
#qwen2.5的模型路径在/Users/ailabuser7-1/Documents/cursor-workspace/qwen-2.5-coder-finetune/finetuning/sft/merged_models/32B

import os
from transformers import AutoTokenizer

def count_tokens(file_path, tokenizer):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    tokens = tokenizer.encode(content)
    return len(tokens)

def count_tokens_without_empty_lines(file_path, tokenizer):
    with open(file_path, 'r', encoding='utf-8') as f:
        # 读取所有行并过滤掉空行
        lines = [line for line in f.readlines() if line.strip()]
        content = ''.join(lines)
    tokens = tokenizer.encode(content)
    return len(tokens)

def main():
    # 设置模型路径
    model_path = "/Users/ailabuser7-1/Documents/cursor-workspace/qwen-2.5-coder-finetune/finetuning/sft/merged_models/32B"
    
    # 初始化tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    
    # 计算prompt的token数量（包含空行）
    prompt_tokens = count_tokens("Process_prompt.txt", tokenizer)
    print(f"Process_prompt_tokens (with empty lines): {prompt_tokens}")
    
    # 计算prompt的token数量（不包含空行）
    prompt_tokens_no_empty = count_tokens_without_empty_lines("Process_prompt.txt", tokenizer)
    print(f"Process_prompt_tokens (without empty lines): {prompt_tokens_no_empty}")
    
    # 计算response的token数量（包含空行）
    response_tokens = count_tokens("Process_response.txt", tokenizer)
    print(f"Process_response_tokens (with empty lines): {response_tokens}")
    
    # 计算response的token数量（不包含空行）
    response_tokens_no_empty = count_tokens_without_empty_lines("Process_response.txt", tokenizer)
    print(f"Process_response_tokens (without empty lines): {response_tokens_no_empty}")
    
    # 计算总token数量（包含空行）
    total_tokens = prompt_tokens + response_tokens
    print(f"Total tokens (with empty lines): {total_tokens}")
    
    # 计算总token数量（不包含空行）
    total_tokens_no_empty = prompt_tokens_no_empty + response_tokens_no_empty
    print(f"Total tokens (without empty lines): {total_tokens_no_empty}")

if __name__ == "__main__":
    main()



