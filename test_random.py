import torch
import os
# 修正1：文件名是 model_minimind，类名是 MiniMindForCausalLM
from model.model_minimind import MiniMindForCausalLM, MiniMindConfig
from transformers import AutoTokenizer

print("正在初始化模型配置...")
# 1. 初始化一个“空脑子”配置
config = MiniMindConfig()

# 修正2：你的配置类里叫 hidden_size，不叫 dim
config.hidden_size = 512 
config.num_hidden_layers = 8
config.num_attention_heads = 8

# 2. 凭空造一个模型 (随机初始化)
print("正在构建模型结构 (随机参数)...")
model = MiniMindForCausalLM(config).to("cuda")

# 3. 加载分词器
# 修正3：看截图，你的 tokenizer.json 在 model 目录下，不是 dataset/tokenizer_root
tokenizer_path = './model' 
print(f"正在加载分词器: {tokenizer_path} ...")

try:
    # 尝试加载项目自带的分词器
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path, trust_remote_code=True, use_fast=False)
except Exception as e:
    print(f"⚠️ 本地加载失败 ({e})，尝试使用通用 GPT2 分词器作为替身...")
    from transformers import GPT2Tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token

# 4. 让这个空脑子说话
question = "你好，你是谁？"
print(f"\n🧐 输入的问题: {question}")

# 把问题变成数字
# 确保 pad_token_id 存在，防止报错
if tokenizer.pad_token_id is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id

inputs = tokenizer(question, return_tensors='pt').to("cuda")

# 让模型乱猜后面的字
with torch.no_grad():
    outputs = model.generate(
        inputs.input_ids, 
        max_new_tokens=20, 
        temperature=1.0,
        do_sample=True,
        top_k=5,
        pad_token_id=tokenizer.pad_token_id
    )

# 把数字变回字
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(f"🤪 没训练的模型的回答 (应该是乱码):\n >> {answer}")