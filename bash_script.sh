#!/bin/bash
#SBATCH --job-name=test
#SBATCH --time=48:00:00
#SBATCH --account=vvh0
#SBATCH --gres=gpu:1
#SBATCH --partition=spgpu
#SBATCH --nodes=1
#SBATCH --mem-per-gpu=48g
#SBATCH --cpus-per-task=4
#SBATCH --output=/nfs/turbo/coe-vvh/lgt/test_script/test_output.log

python /nfs/turbo/coe-vvh/lgt/test_script/check_version.py