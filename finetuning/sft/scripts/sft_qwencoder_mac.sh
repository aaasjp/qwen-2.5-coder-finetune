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
OUTPUT_DIR=${OUTPUT_DIR:-"./checkpoints/sft_model/${MODEL_SIZE}"}

LR=5e-5
MIN_LR=5e-6
WARMUP_STEPS=100
WEIGHT_DECAY=0.0
MAX_LENGTH=8192

echo "DATA_PATH: $DATA_PATH"
echo "PRETRAINED_MODEL: $PRETRAINED_MODEL"
echo "OUTPUT_DIR: $OUTPUT_DIR"
echo "LR: $LR"
echo "MIN_LR: $MIN_LR"
echo "WARMUP_STEPS: $WARMUP_STEPS"
echo "WEIGHT_DECAY: $WEIGHT_DECAY"
echo "MAX_LENGTH: $MAX_LENGTH"

cd /Users/ailabuser7-1/Documents/cursor-workspace/qwen-2.5-coder-finetune/finetuning/sft/

python train.py \
    --model_name_or_path ${PRETRAINED_MODEL} \
    --data_path $DATA_PATH \
    --model_max_length ${MAX_LENGTH} \
    --output_dir ${OUTPUT_DIR} \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 1 \
    --per_device_eval_batch_size 2 \
    --num_train_epochs 3 \
    --save_strategy "steps" \
    --save_steps 100 \
    --save_total_limit 100 \
    --learning_rate ${LR} \
    --weight_decay ${WEIGHT_DECAY} \
    --warmup_steps ${WARMUP_STEPS} \
    --lr_scheduler_type "cosine" \
    --logging_strategy "steps" \
    --logging_steps 1 \
    --truncate_source False