
choices = ["metaMask_Sum", "metaMask_AbSum"]
label_cols = ["PicVocab_AgeAdj", "ReadEng_AgeAdj", "PicSeq_AgeAdj", 
            "ListSort_AgeAdj", "CardSort_AgeAdj", "Flanker_AgeAdj"]
models = ["PlainGCN", "GIN", "GraphSage", "GraphConv"]

import os 
output_dir = "/nfs/turbo/coe-vvh/lgt/IGS/exp/results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 一样的道理 用output_dir specify你想你的 最后log file在什么位置 
# 剩下改变量名即可

for choice in choices:
    for label_col in label_cols:
        for model in models:
            script_name = f"{label_col}_{model}_{choice}"
            output_name = f"{output_dir}/{script_name}.log"
            with open(f"{script_name}.sh", 'w') as f:
                f.write("#!/bin/bash\n")
                f.write(f"#SBATCH --job-name={script_name}\n")
                f.write("#SBATCH --time=48:00:00\n")
                f.write("#SBATCH --account=vvh0\n")
                f.write("#SBATCH --gres=gpu:1\n")
                f.write("#SBATCH --partition=spgpu\n")
                f.write("#SBATCH --nodes=1\n")
                f.write("#SBATCH --mem-per-gpu=48g\n")
                f.write("#SBATCH --cpus-per-task=4\n")
                f.write(f"#SBATCH --output={output_name}\n\n")
                f.write(f"python ./src/main.py --method IGS --model {model} --label_col {label_col} --{choice}")