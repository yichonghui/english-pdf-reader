#!/bin/bash
cd "$(dirname $0)"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/super/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/super/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/super/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/super/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
conda activate torch

python englishPdfReader.py
