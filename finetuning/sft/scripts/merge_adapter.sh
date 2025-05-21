# bash  ./scripts/merge_adapter.sh   /Users/ailabuser7-1/Documents/models/Qwen2.5-Coder-${MODEL_SIZE}-Instruct/ ./checkpoints/sft_lora_model/${MODEL_SIZE}/ ./merged_models/${MODEL_SIZE}/
export PATH=/Users/ailabuser7-1/Documents/miniconda3/envs/qwen-coder-sft/bin:$PATH;
cd /Users/ailabuser7-1/Documents/cursor-workspace/qwen-2.5-coder-finetune/finetuning/sft/
INPUT_MODEL_PATH=${1}
INPUT_ADAPTER_PATH=${2}
OUTPUT_PATH=${3}

INPUT_MODEL_PATH=${INPUT_MODEL_PATH:-"./pretrained_models"}
INPUT_ADAPTER_PATH=${INPUT_ADAPTER_PATH:-"./adapter"}
OUTPUT_PATH=${OUTPUT_PATH:-"./merged_models"}

echo "INPUT_MODEL_PATH: ${INPUT_MODEL_PATH}"
echo "INPUT_ADAPTER_PATH: ${INPUT_ADAPTER_PATH}"
echo "OUTPUT_PATH: ${OUTPUT_PATH}"
python merge_adapter.py --base_model_path ${INPUT_MODEL_PATH} --train_adapters_path ${INPUT_ADAPTER_PATH} --output_path ${OUTPUT_PATH}



