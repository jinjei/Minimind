<div align="center">

![logo](./images/logo.png)


[中文](./README.md) | English

This project is an independent reproduction based on the architectural design of [MiniMind](https://github.com/jingyaogong/minimind). While inspired by the original repository, this implementation focuses on a complete from-scratch training lifecycle. Instead of simply cloning the weights, I conducted the entire pipeline—from raw data tokenization and pretraining (from random initialization) to supervised fine-tuning (SFT)—to validate the training dynamics and loss convergence on custom hardware.

</div>

* This open-source project aims to train a super-small language model **MiniMind** with only 3 RMB cost and 2 hours,
  starting completely from scratch.
* The **MiniMind** series is extremely lightweight, with the smallest version being $\frac{1}{7000}$ the size of GPT-3,
  making it possible to train quickly on even the most ordinary personal GPUs.
* The project also open-sources the minimalist structure of the large model, including extensions for shared mixed
  experts (MoE), dataset cleaning, pretraining, supervised fine-tuning (SFT), LoRA fine-tuning, direct preference
  optimization (DPO) algorithms, reinforcement learning from AI feedback (RLAIF: PPO/GRPO/SPO), and model distillation 
  algorithms, along with the full code of the entire process.
* **MiniMind** also expands into vision multimodal VLM: [MiniMind-V](https://github.com/jingyaogong/minimind-v).
* All core algorithm code is reconstructed from scratch using native PyTorch! It does not rely on abstract interfaces
  provided by third-party libraries.
* This is not only a full-stage open-source reproduction of a large language model but also a tutorial for beginners in
  LLM.
* We hope this project will serve as an inspiring example for everyone, helping to enjoy the fun of creation and
  promoting the progress of the wider AI community!

> To avoid misunderstanding, the "2 hours" test is based on NVIDIA 3090 hardware (single GPU), and the "3 RMB" refers to the GPU server rental cost. Details of the specifications can be found below.

---




# 📌 Introduction

The emergence of Large Language Models (LLMs) has sparked unprecedented global attention to AI. 
Whether it's ChatGPT, DeepSeek, or Qwen, they all demonstrate stunning performance that is awe-inspiring.
However, with their massive scale of tens of billions of parameters, they are not only difficult to train on personal devices but nearly impossible to deploy.
Opening the "black box" of large models to explore their internal mechanisms is truly thrilling!
Unfortunately, 99% of exploration can only stop at using techniques like LoRA to perform minor fine-tuning on existing large models to learn new instructions or tasks.
This is like teaching Newton how to use a 21st-century smartphone—while interesting, it completely deviates from the original intent of understanding the essence of physics.
Meanwhile, third-party large model frameworks and toolkits, such as transformers+trl, expose only highly abstract interfaces.
With just 10 lines of code, you can complete the entire workflow of "loading model + loading dataset + inference + reinforcement learning."
While such efficient packaging is convenient, it also acts like a high-speed spacecraft, isolating developers from underlying implementations and hindering deep exploration of LLM core code.
Yet, "building a plane with Lego is far more exciting than flying in first class!"
What's worse, the internet is flooded with expensive courses and marketing accounts selling AI tutorials with countless flaws and superficial understanding.
For this reason, this project's original intention is to lower the barrier to entry for LLM learning, allowing everyone to start by understanding every line of code,
to personally train an extremely small language model from scratch. Yes, from **training from scratch**, not just **inference**!
With less than 3 RMB in server costs, you can personally experience the entire process of building a language model from 0 to 1.
Let's enjoy the fun of creation together!

> [!NOTE]
> (As of 2025-10) The MiniMind series has completed pretraining of multiple model variants, with the smallest being only 25.8M (0.02B), capable of fluent conversation!

<details style="color:rgb(128,128,128)">
<summary>Models List</summary>

| Model (Size)           | Inference Memory (Approx) | Release    | 
|------------------------|---------------------------|------------|
| MiniMind2-small (26M)  | 0.5 GB                    | 2025.04.26 |
| MiniMind2-MoE (145M)   | 1.0 GB                    | 2025.04.26 |
| MiniMind2 (104M)       | 1.0 GB                    | 2025.04.26 |
| minimind-v1-small (26M)| 0.5 GB                    | 2024.08.28 |
| minimind-v1-moe (4×26M)| 1.0 GB                    | 2024.09.17 |
| minimind-v1 (108M)     | 1.0 GB                    | 2024.09.01 |

</details>

**Project Includes**

- Complete code for MiniMind-LLM structure (Dense + MoE models).
- Detailed training code for Tokenizer.
- Complete training code for Pretrain, SFT, LoRA, RLHF-DPO, RLAIF (PPO/GRPO/SPO), and model distillation.
- Collected, distilled, organized and cleaned high-quality datasets for all stages, all open-sourced.
- Implemented from scratch: pretraining, instruction fine-tuning, LoRA, DPO/PPO/GRPO/SPO reinforcement learning, and white-box model distillation. Core algorithms barely depend on third-party framework encapsulation, all open-sourced.
- Compatible with mainstream third-party frameworks like `transformers`, `trl`, `peft`.
- Training supports single GPU, multiple GPUs on a single machine (DDP, DeepSpeed), supports wandb/swanlab visualization of training process. Supports dynamic training start/stop.
- Model testing on third-party evaluation leaderboards (C-Eval, C-MMLU, OpenBookQA, etc.), supports YaRN algorithm for RoPE long-text extrapolation.
- Implements an extremely simple OpenAI API-compliant server, convenient for integration with third-party ChatUI (FastGPT, Open-WebUI, etc.).
- Implements the simplest chat WebUI frontend based on streamlit.
- Fully compatible with popular community inference engines `llama.cpp`, `vllm`, `ollama` or training framework `Llama-Factory`.
- Reproduced (distilled/RL) DeepSeek-R1 reasoning model as MiniMind-Reason model, with **data + models** fully open-sourced!

We hope this open-source project can help LLM beginners get started quickly!


**Acknowledgments**

Special thanks to MiniMind for providing the foundational architecture and inspiration. Building upon the original codebase, this repository represents my end-to-end execution of the LLM training pipeline, including manual environment configuration, full-cycle model training from scratch, and performance evaluation.
