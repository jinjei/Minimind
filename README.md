<div align="center">

![logo](./images/logo.png)

</div>



<div align="center">

中文 | [English](./README_en.md)


</div>

本项目是基于 [MiniMind](https://github.com/jingyaogong/minimind) 架构理念的独立复现版本。在致谢原作者优秀工作的同时，本项目重点在于从零构建大模型的完整训练全流程。区别于简单的代码克隆或推理测试，我独立完成了从原始语料的数据预处理、基于随机初始化的预训练（Pretrain），到指令微调（SFT）的完整实现，旨在深入探究 LLM 的底层训练细节与收敛特性。



* 此开源项目旨在完全从0开始，仅用3块钱成本 + 2小时！即可训练出仅为25.8M的超小语言模型**MiniMind**。
* **MiniMind**系列极其轻量，最小版本体积是 GPT-3 的 $\frac{1}{7000}$，力求做到最普通的个人GPU也可快速训练。
* 项目同时开源了大模型的极简结构-包含拓展共享混合专家(MoE)、数据集清洗、预训练(Pretrain)、监督微调(SFT)、LoRA微调、直接偏好优化(DPO)、强化学习训练(RLAIF: PPO/GRPO等)、模型蒸馏等全过程代码。
* 项目所有核心算法代码均从0使用PyTorch原生重构！不依赖第三方库提供的抽象接口。
* 这不仅是大语言模型的全阶段开源复现，也是一个入门LLM的教程。

> 为防止误解，“2小时” 基于NVIDIA 3090硬件设备（单卡）测试，“3块钱”指GPU服务器租用成本，具体规格详情见下文。

---


<div align="center">

![minimind2](./images/minimind2.gif)

[🔗🍓推理模型](https://www.modelscope.cn/studios/gongjy/MiniMind-Reasoning) | [🔗🤖常规模型](https://www.modelscope.cn/studios/gongjy/MiniMind) | [🔗🎞️视频介绍](https://www.bilibili.com/video/BV12dHPeqE72/?share_source=copy_web&vd_source=670c2504f88726f8cf4a21ef6147c0e8)


<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://huggingface.co/collections/jingyaogong/minimind-66caf8d999f5c7fa64f399e5" style="text-decoration: none;">
          <img src="./images/and_huggingface.png" alt="Hugging Face Logo" style="vertical-align: middle; width: auto; max-width: 100%;" />
        </a>
      </td>
      <td align="center">
        <a href="https://www.modelscope.cn/profile/gongjy" style="text-decoration: none;">
          <img src="./images/and_modelscope.png" alt="ModelScope Logo" style="vertical-align: middle; width: auto; max-width: 100%;" />
        </a>
      </td>
    </tr>
  </table>
</div>


</div>

# 📌 Introduction


> [!NOTE]
> （截至2025-10）MiniMind系列已完成多个型号模型的预训练，最小仅需25.8M（0.02B），即可具备流畅对话能力！

<details style="color:rgb(128,128,128)">
<summary>Models List</summary>

| 模型 (大小)                 | 推理占用 (约) | Release    | 
|-------------------------|----------|------------|
| MiniMind2-small (26M)   | 0.5 GB   | 2025.04.26 |
| MiniMind2-MoE (145M)    | 1.0 GB   | 2025.04.26 |
| MiniMind2 (104M)        | 1.0 GB   | 2025.04.26 |
| minimind-v1-small (26M) | 0.5 GB   | 2024.08.28 |
| minimind-v1-moe (4×26M) | 1.0 GB   | 2024.09.17 |
| minimind-v1 (108M)      | 1.0 GB   | 2024.09.01 |

</details>

**项目包含**

- MiniMind-LLM结构的全部代码（Dense+MoE模型）。
- 包含Tokenizer分词器详细训练代码。
- 包含Pretrain、SFT、LoRA、RLHF-DPO、RLAIF(PPO/GRPO/SPO)、模型蒸馏的全过程训练代码。
- 收集、蒸馏、整理并清洗去重所有阶段的高质量数据集，且全部开源。
- 从0实现预训练、指令微调、LoRA、DPO/PPO/GRPO/SPO强化学习，白盒模型蒸馏。关键算法几乎不依赖第三方封装的框架，且全部开源。
- 同时兼容`transformers`、`trl`、`peft`等第三方主流框架。
- 训练支持单机单卡、单机多卡(DDP、DeepSpeed)训练，支持wandb/swanlab可视化训练流程。支持动态启停训练。
- 在第三方测评榜（C-Eval、C-MMLU、OpenBookQA等）进行模型测试，支持YaRN算法执行RoPE长文本外推。
- 实现Openai-Api协议的极简服务端，便于集成到第三方ChatUI使用（FastGPT、Open-WebUI等）。
- 基于streamlit实现最简聊天WebUI前端。
- 全面兼容社区热门`llama.cpp`、`vllm`、`ollama`推理引擎或`Llama-Factory`训练框架。
- 复现(蒸馏/RL)大型推理模型DeepSeek-R1的MiniMind-Reason模型，**数据+模型**全部开源！

希望此开源项目可以帮助LLM初学者快速入门！


**致谢**
特别感谢 MiniMind 项目提供的出色架构设计与灵感。在原项目的基础上，本仓库记录了我对 LLM 训练流水线的端到端实践，包括环境的从零配置、模型权重的从头训练（Pretrain + SFT）以及最终的性能评估，完成了对原项目的完整复现与验证


