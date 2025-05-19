# 1.构建conda环境
conda create -n qwen-coder-sft python=3.9
conda activate qwen-coder-sft

# 2.安装依赖
pip install -r requirements.txt

# 3.数据tokenize
样例数据在finetuning/sft/data下面
cd finetuning/sft
bash ./scripts/binarize_data.sh ${INPUT_PATH} ${OUTPUT_PATH} ${TOKENIZER_PATH}

# 4.模型微调(_mac支持在mac上进行微调)

全参数微调--7B可以跑起来，但是32B跑不起来
bash ./scripts/sft_qwencoder_mac.sh

lora微调--7B和32B都可以跑起来
bash ./scripts/sft_qwencoder_with_lora_mac.sh

 