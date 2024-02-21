<div align="center">
<h1>PROGrasp: Pragmatic Human-Robot Communication for Object Grasping</h1>

**[Gi-Cheon Kang][2], &nbsp; [Junghyun Kim][3], &nbsp; [Jaein Kim][4], &nbsp; [Byoung-Tak Zhang][5]** <br>

**[ICRA 2024][6] ([Paper][1])**
</div>

This repository contains the pytorch implementation for the ICRA'24 paper titled "PROGrasp: Pragmatic Human-Robot Communication for Object Grasping". The repository is now under construction, and we will release the source code soon.





## Demo Video
<video autoplay="true" loop="true" src="https://github.com/gicheonkang/prograsp/assets/23380257/5df0071c-26a0-45f5-872b-1c7b7ba6536c"></video>



Download Data
----------------------
Download the preprocessed and raw data. Simply run the following scripts. 
```shell
chmod +x scripts/download_data.sh
./scripts/download_data.sh
```



Pre-trained Checkpoints
--------------------------------------
Please download the checkpoints below.

| Model | Link |
|:-------:|:---------:|
|Visual Grounding | [Download](https://www.dropbox.com/scl/fi/61b3ty5d8xzunqc9rmubb/vg.pt?rlkey=3sd8yjmlg6e8t4jwwauv9j1he&dl=0)|
|Question Generation |[Download](https://www.dropbox.com/scl/fi/qiehwcmcwxgl0c1ayjwod/q_gen.pt?rlkey=s89qkvavw8bbslc00we2n23a3&dl=0)|
|Answer Interpretation | [Download](https://www.dropbox.com/scl/fi/x4lasshsixnovwa6sktju/a_int.pt?rlkey=3w6nze2w82th2fd8o2s72gdi2&dl=0)|



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

License
-------
MIT License





[1]: https://arxiv.org/abs/2205.12502
[2]: https://gicheonkang.com
[3]: https://jhkim-snu.github.io
[4]: https://bi.snu.ac.kr/
[5]: https://bi.snu.ac.kr/~btzhang/
[6]: https://2024.ieee-icra.org
