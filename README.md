<div align="center">
<h1>PROGrasp: Pragmatic Human-Robot Communication for Object Grasping</h1>

**[Gi-Cheon Kang][2], &nbsp; [Junghyun Kim][3], &nbsp; [Jaein Kim][4], &nbsp; [Byoung-Tak Zhang][5]** <br>

**[ICRA 2024][6] ([Paper][1])**
</div>

This repository contains the pytorch implementation for the ICRA'24 paper titled "PROGrasp: Pragmatic Human-Robot Communication for Object Grasping".





## Demo Video
<video autoplay="true" loop="true" src="https://github.com/gicheonkang/prograsp/assets/23380257/5df0071c-26a0-45f5-872b-1c7b7ba6536c"></video>



Setup and Dependencies
----------------------
The source code is based on PyTorch v1.9.1+, CUDA 11+ and CuDNN 7+. Anaconda/Miniconda is the recommended to set up this codebase: <br>

1. Install Anaconda or Miniconda distribution based on Python3.7+ from their [downloads' site][8].
2. Clone this repository and create an environment:

```shell
git clone https://www.github.com/gicheonkang/gst-visdial
conda create -n prograsp python=3.7.16 -y

# activate the environment and install all dependencies
conda activate prograsp
pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt
```

If you have trouble installing the above, please consult [OFA repository][7]. The repository has rich installation know-how.  



Download Data
----------------------
Download the preprocessed and raw data. Simply run the following scripts. 
```shell
chmod +x scripts/download_data.sh
./scripts/download_data.sh
```


Train
----------------------
Run the following scripts if you want to train the visual grounding module. 
```shell
chmod +x OFA/run_scripts/prograsp/train_progrounding.sh
./OFA/run_scripts/prograsp/train_progrounding.sh
```

If you want to see the data loader for each module, please see `OFA/data/mm_data/`.

The file `OFA/utils/eval_utils.py` contains codes for evaluation 



Pre-trained Checkpoints
--------------------------------------
Please download the checkpoints below.

| Model | Link |
|:-------:|:---------:|
|Visual Grounding | [Download](https://www.dropbox.com/scl/fi/61b3ty5d8xzunqc9rmubb/vg.pt?rlkey=3sd8yjmlg6e8t4jwwauv9j1he&dl=0)|
|Question Generation |[Download](https://www.dropbox.com/scl/fi/qiehwcmcwxgl0c1ayjwod/q_gen.pt?rlkey=s89qkvavw8bbslc00we2n23a3&dl=0)|
|Answer Interpretation | [Download](https://www.dropbox.com/scl/fi/x4lasshsixnovwa6sktju/a_int.pt?rlkey=3w6nze2w82th2fd8o2s72gdi2&dl=0)|


Inference & Evaluation
--------------------------------------
We implement evaluation / inference codes for interactive object discovery. Please check the following jupyter notebook file.
```shell
OFA/prograsp_eval.ipynb
```


Citation
-----------------------------
If you use this code or preprocessed data in your research, please consider citing:
```bibtex
@article{kang2023prograsp,
  title={PROGrasp: Pragmatic Human-Robot Communication for Object Grasping},
  author={Kang, Gi-Cheon and Kim, Junghyun and Kim, Jaein and Zhang, Byoung-Tak},
  journal={arXiv preprint arXiv:2309.07759},
  year={2023}
}
```

Acknowledgements
-----------------
We use [OFA][7] as reference code. Thanks!


License
-------
MIT License





[1]: https://arxiv.org/abs/2309.07759
[2]: https://gicheonkang.com
[3]: https://jhkim-snu.github.io
[4]: https://bi.snu.ac.kr/
[5]: https://bi.snu.ac.kr/~btzhang/
[6]: https://2024.ieee-icra.org
[7]: https://github.com/OFA-Sys/OFA
[8]: https://conda.io/docs/user-guide/install/download.html
