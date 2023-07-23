
choices = ["metaMask_Sum", "metaMask_AbSum"]
label_cols = ["PicVocab_AgeAdj", "ReadEng_AgeAdj", "PicSeq_AgeAdj", 
            "ListSort_AgeAdj", "CardSort_AgeAdj", "Flanker_AgeAdj"]
models = ["PlainGCN", "GIN", "GraphSage", "GraphConv"]

# 以上是不同参数 用list表示 如果你有自己想用的参数 则修改即可

input_prefix = "/nfs/turbo/coe-vvh/lgt/IGS/exp/tuning"
# input prefix是这个script的前置directory 是为了让你在不同的directory python file还可以执行的了 


with open("bash.sh", "w") as f:
    for choice in choices:
        for label_col in label_cols:
            for model in models:
                script_name = f"{label_col}_{model}_{choice}.sh"
                f.write(f"sbatch {input_prefix}/{script_name}\n")
            
            
