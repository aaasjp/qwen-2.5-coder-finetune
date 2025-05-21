from transformers import AutoModelForCausalLM, AutoTokenizer

# model_name = "/Users/ailabuser7-1/Documents/cursor-workspace/qwen-2.5-coder-finetune/finetuning/sft/checkpoints/sft_model/7B"
model_name = "/Users/ailabuser7-1/Documents/cursor-workspace/qwen-2.5-coder-finetune/finetuning/sft/merged_models/32B"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Write a regex expression to match any letter of the alphabet"
messages = [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(f"response: \n{response}")