最近在做一个代码大模型微调的工作，找了bigcode排名第一的qwen-2.5-coder进行微调。下面记录下自己做的工作和遇到的问题：
1.首先把qwen-2.5-coder的report从头到尾看了一遍，coder模型主要是基于qwen-base模型微调而来，最新版本的coder模型，增加了利用fill-in-middle技术，增加了新的token，主要为了进行代码补全和github多文档上下文。
2.查阅了coder模型使用的评估数据集，包括CrossCodeEval，humaneval，cruxeval等。模型的性能跟选取的数据有根本关系，而且qwen-coder对数据处理也进行了各种高质量语料的构建，包括利用大模型进行数据合成
3.看了qwen-2.5-coder的源代码，发现还是有各种问题，主要是文档里面写的不清晰。着重看了下代码中对message套用模版的处理，发现在sft中，并没有使用fill-in-middle的模版，比如：<|fim_prefix|>", "<|fim_middle|>", "<|fim_suffix|>", "<|repo_name|>
4.源代码中使用sft的时候，使用torchrun框架，但是由于我使用的是mac studio，发现跑不起来。明天需要继续解决这个问题。
今日到此结束，nice day