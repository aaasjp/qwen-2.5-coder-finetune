export PATH=/path/to/miniconda3/envs/qwen-coder-sft/bin:$PATH;
INPUT_PATH=${1}
OUTPUT_PATH=${2}
TOKENIZER_PATH=${3}
INPUT_PATH=${INPUT_PATH:-"./data/raw/sft.jsonl"}
OUTPUT_PATH=${OUTPUT_PATH:-"./data/processed/sft.jsonl"}
TOKENIZER_PATH=${TOKENIZER_PATH:-"/Users/ailabuser7-1/Documents/models/Qwen2.5-Coder-32B-Instruct/"}
python binarize_data.py -input_path ${INPUT_PATH} -output_path ${OUTPUT_PATH} -workers 64 -tokenizer_path ${TOKENIZER_PATH}  -save_format .jsonl