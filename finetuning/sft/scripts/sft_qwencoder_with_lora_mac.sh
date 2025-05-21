export PATH=/path/to/miniconda3/envs/qwen-coder-sft/bin:$PATH;

MODEL_SIZE=${1}
DATA_PATH=${2}
PRETRAINED_MODEL=${3}
OUTPUT_DIR=${4}

if [ -z "$MODEL_SIZE" ]; then   
    echo "MODEL_SIZE is not set"
    exit 1
fi

DATA_PATH=${DATA_PATH:-"./data/processed/sft.jsonl"}
PRETRAINED_MODEL=${PRETRAINED_MODEL:-"/Users/ailabuser7-1/Documents/models/Qwen2.5-Coder-${MODEL_SIZE}-Instruct/"}
OUTPUT_DIR=${OUTPUT_DIR:-"./checkpoints/sft_lora_model/${MODEL_SIZE}"}

PEFT_CONFIG_FOLDER="./configs/lora"

LR=1e-5
MIN_LR=1e-6
WARMUP_STEPS=100
WEIGHT_DECAY=0.01
MAX_LENGTH=4096
MAX_GRAD_NORM=1.0

echo "DATA_PATH: $DATA_PATH"
echo "PRETRAINED_MODEL: $PRETRAINED_MODEL"
echo "OUTPUT_DIR: $OUTPUT_DIR"
echo "LR: $LR"
echo "MIN_LR: $MIN_LR"
echo "WARMUP_STEPS: $WARMUP_STEPS"
echo "WEIGHT_DECAY: $WEIGHT_DECAY"
echo "MAX_LENGTH: $MAX_LENGTH"
echo "MAX_GRAD_NORM: $MAX_GRAD_NORM"

cd /Users/ailabuser7-1/Documents/cursor-workspace/qwen-2.5-coder-finetune/finetuning/sft/

python train.py \
    --model_name_or_path ${PRETRAINED_MODEL} \
    --data_path $DATA_PATH \
    --model_max_length ${MAX_LENGTH} \
    --output_dir ${OUTPUT_DIR} \
    --num_train_epochs 3 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 8 \
    --per_device_eval_batch_size 1 \
    --save_strategy "steps" \
    --save_steps 100 \
    --save_total_limit 100 \
    --learning_rate ${LR} \
    --weight_decay ${WEIGHT_DECAY} \
    --warmup_steps ${WARMUP_STEPS} \
    --lr_scheduler_type "cosine" \
    --logging_strategy "steps" \
    --logging_steps 1 \
    --truncate_source False \
    --use_peft True \
    --peft_config_path ${PEFT_CONFIG_FOLDER} \
    --max_grad_norm ${MAX_GRAD_NORM} \
    --gradient_checkpointing True \