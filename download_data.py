import os
from huggingface_hub import hf_hub_download
import shutil

# 1. 定义文件列表
files_to_download = [
    "pretrain_hq.jsonl",
    "sft_mini_512.jsonl"
]

# 2. 目标文件夹
target_dir = "./dataset"
os.makedirs(target_dir, exist_ok=True)

print(f"🚀 开始下载数据 (修正版)...")

for filename in files_to_download:
    print(f"正在下载: {filename} ...")
    try:
        # 修正点：repo_id 使用下划线 _
        file_path = hf_hub_download(
            repo_id="jingyaogong/minimind_dataset", 
            repo_type="dataset",
            filename=filename,
            local_dir=target_dir,
            local_dir_use_symlinks=False
        )
        print(f"✅ 成功! 文件已保存: {file_path}")
        
    except Exception as e:
        print(f"❌ 下载 {filename} 失败: {e}")
        print("请检查网络或文件名是否正确")

print("🎉 下载结束！")