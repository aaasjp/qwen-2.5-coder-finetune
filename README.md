# 1.构建conda环境
conda create -n qwen-coder-sft python=3.9
conda activate qwen-coder-sft

# 2.安装依赖
pip install -r dev-requirements.txt

# 3.数据tokenize
样例数据在finetuning/sft/data下面
 ```bash
cd finetuning/sft
bash ./scripts/binarize_data.sh ${INPUT_PATH} ${OUTPUT_PATH} ${TOKENIZER_PATH}
```

# 4.模型微调(_mac支持在mac上进行微调)
 ```bash
全参数微调--7B可以跑起来，但是32B跑不起来
bash ./scripts/sft_qwencoder_mac.sh

lora微调--7B和32B都可以跑起来
bash ./scripts/sft_qwencoder_with_lora_mac.sh
```

# 5. 模型合并
 ```bash
BASE_MODEL_PATH=${1}
TRAIN_ADAPTERS_PATH=${2}
OUTPUT_PATH=${3}
bash ./scripts/merge_adapter.sh ${BASE_MODEL_PATH} ${TRAIN_ADAPTERS_PATH} ${OUTPUT_PATH}
```
 

 # 6. 模型推理
  ```bash
  cd inference/
  修改合并后的模型地址
  python infer.py
  ```