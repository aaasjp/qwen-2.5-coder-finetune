import pandas as pd
import json

def convert_to_sft_format():
    # 读取CSV文件
    df = pd.read_csv('train_data.csv')
    
    # 过滤掉prompt或标注json结果为空的行
    df = df.dropna(subset=['prompt', '标注json结果'])
    df = df[df['prompt'].str.strip() != '']
    df = df[df['标注json结果'].str.strip() != '']
    
    # 系统提示词
    system_prompt = """你是一个专业的代码专家，精通Java、Python、Go、Vue等多种编程语言。
你擅长代码审查、调试和优化，能够提供高质量的代码建议和解决方案。
你的回答总是准确、专业且易于理解。"""

    # 打开输出文件
    with open('sft.jsonl', 'w', encoding='utf-8') as f:
        # 处理每一行数据
        for _, row in df.iterrows():
            # 构建消息格式
            message = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": row['prompt']},
                    {"role": "assistant", "content": row['标注json结果']}
                ],
                "format": "chatml"
            }
            # 写入JSONL文件
            f.write(json.dumps(message, ensure_ascii=False) + '\n')

def validate_jsonl_file(file_path):
    """验证JSONL文件的有效性"""
    try:
        total_lines = 0
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                try:
                    # 尝试解析每一行的JSON
                    data = json.loads(line.strip())
                    
                    # 验证必要的字段是否存在
                    if 'messages' not in data:
                        print(f"第{i}行缺少'messages'字段")
                        return False
                    
                    # 验证messages数组中的内容
                    messages = data['messages']
                    if len(messages) != 3:
                        print(f"第{i}行的messages数组长度不是3")
                        return False
                    
                    # 验证每个消息的role和content
                    required_roles = ['system', 'user', 'assistant']
                    for msg, required_role in zip(messages, required_roles):
                        if msg.get('role') != required_role:
                            print(f"第{i}行的role顺序不正确")
                            return False
                        if 'content' not in msg:
                            print(f"第{i}行的消息缺少content字段")
                            return False
                    
                    # 验证format字段
                    if data.get('format') != 'chatml':
                        print(f"第{i}行的format不是'chatml'")
                        return False
                    
                    total_lines += 1
                        
                except json.JSONDecodeError:
                    print(f"第{i}行JSON解析失败")
                    return False
                    
        print(f"JSONL文件验证通过！总共有 {total_lines} 条有效数据。")
        return True
        
    except Exception as e:
        print(f"验证过程中发生错误: {str(e)}")
        return False

def print_first_jsonl(file_path):
    """打印第一条JSONL数据的详细内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            if first_line:
                data = json.loads(first_line)
                print("\n第一条JSONL数据的详细内容：")
                print("=" * 50)
                print(f"format: {data['format']}")
                print("\nmessages数组内容：")
                for i, msg in enumerate(data['messages'], 1):
                    print(f"\n消息 {i}:")
                    print(f"  role: {msg['role']}")
                    print(f"  content: {msg['content']}")
                    print("=" * 100)
    except Exception as e:
        print(f"读取第一条数据时发生错误: {str(e)}")

if __name__ == "__main__":
    # 转换数据
    convert_to_sft_format()
    
    # 验证生成的文件
    print("开始验证生成的JSONL文件...")
    if validate_jsonl_file('sft.jsonl'):
        print_first_jsonl('sft.jsonl')
