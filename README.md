# Awesome Masked Image Modeling for Visual Represention Learning

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![GitHub stars](https://img.shields.io/github/stars/Lupin1998/Awesome-MIM?color=blue) ![GitHub forks](https://img.shields.io/github/forks/Lupin1998/Awesome-MIM?color=yellow&label=Fork)

## Introduction

**We summarize awesome Masked Image Modeling (MIM) methods proposed for self-supervised visual representation learning.*

The list of awesome MIM methods is summarized in chronological order and is on updating. The main branch is modified according to [Awesome-MIM](https://github.com/Westlake-AI/openmixup/blob/main/docs/en/awesome_selfsup/MIM.md) in [OpenMixup](https://github.com/Westlake-AI/openmixup). If you find any typos or any missed paper, please feel free to open an issue or send a pull request. Currently, we are working on a survey of MIM pre-training methods.

* To find related papers and their relationships, check out [Connected Papers](https://www.connectedpapers.com/), which visualizes the academic field in a graph representation.
* To export BibTeX citations of papers, check out [ArXiv](https://arxiv.org/) or [Semantic Scholar](https://www.semanticscholar.org/) of the paper for professional reference formats.

## Table of Contents

- [Awesome Masked Image Modeling for Visual Represention Learning](#awesome-masked-image-modeling-for-visual-represention-learning)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [MIM for Backbones](#mim-for-backbones)
    - [MIM for Transformers](#mim-for-transformers)
    - [MIM with Constrastive Learning](#mim-with-constrastive-learning)
    - [MIM for Transformers and CNNs](#mim-for-transformers-and-cnns)
    - [MIM with Advanced Masking](#mim-with-advanced-masking)
  - [MIM for Downstream Tasks](#mim-for-downstream-tasks)
    - [Object Detection](#object-detection)
    - [Video Rrepresentation](#video-rrepresentation)
    - [Knowledge Distillation](#knowledge-distillation)
    - [Efficient Fine-tuning](#efficient-fine-tuning)
    - [Medical Image](#medical-image)
    - [Face Recognition](#face-recognition)
    - [Scene Text Recognition (OCR)](#scene-text-recognition-ocr)
    - [Remote Sensing Image](#remote-sensing-image)
    - [3D Point Cloud](#3d-point-cloud)
    - [Reinforcement Learning](#reinforcement-learning)
    - [Audio](#audio)
  - [Analysis and Understanding of MIM](#analysis-and-understanding-of-mim)
  - [Survey](#survey)
  - [Contribution](#contribution)
  - [Related Project](#related-project)
    - [Paper List of Masked Image Modeling](#paper-list-of-masked-image-modeling)
    - [Project of Self-supervised Learning](#project-of-self-supervised-learning)


## MIM for Backbones

### MIM for Transformers

* **iGPT**: Mark Chen, Alec Radford, Rewon Child, Jeff Wu, Heewoo Jun, David Luan, Ilya Sutskever.
   - Generative Pretraining from Pixels. [[ICML'2020](http://proceedings.mlr.press/v119/chen20s/chen20s.pdf)] [[code](https://github.com/openai/image-gpt)]
   <p align="center"><img width="95%" src="https://user-images.githubusercontent.com/44519745/204300433-a0b6b25b-9f6f-431b-bbfd-19169d8cbca6.png" /></p>
* **ViT**: Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby.
   - An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. [[ICLR'2021](https://arxiv.org/abs/2010.11929)] [[code](https://github.com/google-research/vision_transformer)]
   <p align="center"><img width="75%" src="https://user-images.githubusercontent.com/44519745/204301490-5673cc4c-93d1-435d-a266-ec5a0294bf3b.png" /></p>
* **BEiT**: Hangbo Bao, Li Dong, Furu Wei.
   - BEiT: BERT Pre-Training of Image Transformers. [[ICLR'2022](https://arxiv.org/abs/2106.08254)] [[code](https://github.com/microsoft/unilm/tree/master/beit)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204301720-156e15e1-a00a-4946-b17f-d2620d2be3d6.png" /></p>
* **iBOT**: Jinghao Zhou, Chen Wei, Huiyu Wang, Wei Shen, Cihang Xie, Alan Yuille, Tao Kong.
   - iBOT: Image BERT Pre-Training with Online Tokenizer. [[ICLR'2022](https://arxiv.org/abs/2111.07832)] [[code](https://github.com/bytedance/ibot)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204301946-1b18e2a8-b205-4d85-8ea9-bd2e4d529a70.png" /></p>
* **MAE**: Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, Ross Girshick.
   - Masked Autoencoders Are Scalable Vision Learners. [[CVPR'2022](https://arxiv.org/abs/2111.06377)] [[code](https://github.com/facebookresearch/mae)]
   <p align="center"><img width="65%" src="https://user-images.githubusercontent.com/44519745/204302185-1b854627-597b-416a-aa85-23dc6c87b59e.png" /></p>
* **SimMIM**: Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin, Jianmin Bao, Zhuliang Yao, Qi Dai, Han Hu.
   - SimMIM: A Simple Framework for Masked Image Modeling. [[CVPR'2022](https://arxiv.org/abs/2111.09886)] [[code](https://github.com/microsoft/simmim)]
   <p align="center"><img width="65%" src="https://user-images.githubusercontent.com/44519745/204302529-8075a5cc-a2e8-4245-891b-8f74c1bc1734.png" /></p>
* **MaskFeat**: Chen Wei, Haoqi Fan, Saining Xie, Chao-Yuan Wu, Alan Yuille, Christoph Feichtenhofer.
   - Masked Feature Prediction for Self-Supervised Visual Pre-Training. [[CVPR'2022](https://arxiv.org/abs/2112.09133)] [[code](https://github.com/facebookresearch/SlowFast)]
   <p align="center"><img width="60%" src="https://user-images.githubusercontent.com/44519745/204302699-10f1f1d4-2bb4-428a-b43b-2972ba915286.png" /></p>
* **data2vec**: Alexei Baevski, Wei-Ning Hsu, Qiantong Xu, Arun Babu, Jiatao Gu, Michael Auli.
   - data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language. [[ICML'2022](https://arxiv.org/abs/2202.03555)] [[code](https://github.com/facebookresearch/fairseq/tree/main/examples/data2vec)]
   <p align="center"><img width="95%" src="https://user-images.githubusercontent.com/44519745/204302962-e44f4eed-b7d0-4b64-8696-ae6f349400fb.png" /></p>
* **MP3**: Shuangfei Zhai, Navdeep Jaitly, Jason Ramapuram, Dan Busbridge, Tatiana Likhomanenko, Joseph Yitan Cheng, Walter Talbott, Chen Huang, Hanlin Goh, Joshua Susskind.
   - Position Prediction as an Effective Pretraining Strategy. [[ICML'2022](https://arxiv.org/abs/2207.07611)]
   <p align="center"><img width="70%" src="https://user-images.githubusercontent.com/44519745/206919419-aa867bf6-f729-4bf7-8f70-c21f17bf8cec.png" /></p>
* **PeCo**: Xiaoyi Dong, Jianmin Bao, Ting Zhang, Dongdong Chen, Weiming Zhang, Lu Yuan, Dong Chen, Fang Wen, Nenghai Yu.
   - PeCo: Perceptual Codebook for BERT Pre-training of Vision Transformers. [[ArXiv'2021](https://arxiv.org/abs/2111.12710)] [[code](https://github.com/microsoft/PeCo)]
* **MC-SSL0.0**: Sara Atito, Muhammad Awais, Ammarah Farooq, Zhenhua Feng, Josef Kittler.
   - MC-SSL0.0: Towards Multi-Concept Self-Supervised Learning. [[ArXiv'2021](https://arxiv.org/abs/2111.15340)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204303461-5d4fb0a1-bff5-4f0a-afea-ee0d81ce17ba.png" /></p>
* **mc-BEiT**: Xiaotong Li, Yixiao Ge, Kun Yi, Zixuan Hu, Ying Shan, Ling-Yu Duan.
   - mc-BEiT: Multi-choice Discretization for Image BERT Pre-training. [[ECCV'2022](https://arxiv.org/abs/2203.15371)] [[code](https://github.com/lixiaotong97/mc-BEiT)]
   <p align="center"><img width="75%" src="https://user-images.githubusercontent.com/44519745/204304102-a17e3bb2-ffe5-4b42-bf5f-4dece8809391.png" /></p>
* **BootMAE**: Xiaoyi Dong, Jianmin Bao, Ting Zhang, Dongdong Chen, Weiming Zhang, Lu Yuan, Dong Chen, Fang Wen, Nenghai Yu.
   - Bootstrapped Masked Autoencoders for Vision BERT Pretraining. [[ECCV'2022](https://arxiv.org/abs/2207.07116)] [[code](https://github.com/LightDXY/BootMAE)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204304317-0cbe6647-769b-4737-9f65-85c4e47ec944.png" /></p>
* **SdAE**: Yabo Chen, Yuchen Liu, Dongsheng Jiang, Xiaopeng Zhang, Wenrui Dai, Hongkai Xiong, Qi Tian.
   - SdAE: Self-distillated Masked Autoencoder. [[ECCV'2022](https://arxiv.org/abs/2208.00449)] [[code](https://github.com/AbrahamYabo/SdAE)]
   <p align="center"><img width="80%" src="https://user-images.githubusercontent.com/44519745/204304730-edc6fe19-b12a-4986-922a-9694230e9ef2.png" /></p>
* **MultiMAE**: Roman Bachmann, David Mizrahi, Andrei Atanov, Amir Zamir.
   - MultiMAE: Multi-modal Multi-task Masked Autoencoders. [[ECCV'2022](https://arxiv.org/abs/2204.01678)] [[code](https://github.com/EPFL-VILAB/MultiMAE)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204304575-577cc0f0-3ac7-4f02-b884-48ec8d061476.png" /></p>
* **SupMAE**: Feng Liang, Yangguang Li, Diana Marculescu.
   - SupMAE: Supervised Masked Autoencoders Are Efficient Vision Learners. [[ArXiv'2022](https://arxiv.org/abs/2205.14540)] [[code](https://github.com/cmu-enyac/supmae)]
   <p align="center"><img width="65%" src="https://user-images.githubusercontent.com/44519745/204305079-c99782a4-ba5f-4785-a2c6-4990da13a493.png" /></p>
* **MVP**: Longhui Wei, Lingxi Xie, Wengang Zhou, Houqiang Li, Qi Tian.
   - MVP: Multimodality-guided Visual Pre-training. [[ArXiv'2022](https://arxiv.org/abs/2203.05175)]
   <p align="center"><img width="80%" src="https://user-images.githubusercontent.com/44519745/204305240-24cee1ff-13d6-4936-93a1-8a4614faed99.png" /></p>
* **Ge2AE**: Hao Liu, Xinghua Jiang, Xin Li, Antai Guo, Deqiang Jiang, Bo Ren.
   - The Devil is in the Frequency: Geminated Gestalt Autoencoder for Self-Supervised Visual Pre-Training. [[AAAI'2023](https://arxiv.org/abs/2204.08227)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204305475-c462edf5-6e20-4f43-a1e1-f06641d13966.png" /></p>
* **ConvMAE**: Peng Gao, Teli Ma, Hongsheng Li, Ziyi Lin, Jifeng Dai, Yu Qiao.
   - ConvMAE: Masked Convolution Meets Masked Autoencoders. [[NIPS'2022](https://arxiv.org/abs/2205.03892)] [[code](https://github.com/Alpha-VL/ConvMAE)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/204305687-8f04d9f7-dc60-4ff0-8f94-5e72795774ca.png" /></p>
* **MR-MAE (ConvMAE.V2)**: Peng Gao, Renrui Zhang, Rongyao Fang, Ziyi Lin, Hongyang Li, Hongsheng Li, Qiao Yu.
   - Mimic before Reconstruct: Enhancing Masked Autoencoders with Feature Mimicking. [[arXiv'2023](https://arxiv.org/abs/2303.05475)] [[code](https://github.com/alpha-vl/convmae)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/236312228-1038fc6c-af93-46f2-b0aa-6f121f8388be.png" /></p>
* **GreenMIM**: Lang Huang, Shan You, Mingkai Zheng, Fei Wang, Chen Qian, Toshihiko Yamasaki.
   - Green Hierarchical Vision Transformer for Masked Image Modeling. [[NIPS'2022](https://arxiv.org/abs/2205.13515)] [[code](https://github.com/LayneH/GreenMIM)]
   <p align="center"><img width="75%" src="https://user-images.githubusercontent.com/44519745/204305942-b22b5064-26d9-4f0b-9a2a-88012873f4fa.png" /></p>
* **TTT-MAE**: Yossi Gandelsman, Yu Sun, Xinlei Chen, Alexei A. Efros.
   - Test-Time Training with Masked Autoencoders. [[NIPS'2022](https://arxiv.org/abs/2209.07522)] [[code](https://github.com/yossigandelsman/test_time_training_mae)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/204306169-63fd5383-ee33-47f0-a955-971cfbd150ae.png" /></p>
* **HiViT**: Xiaosong Zhang, Yunjie Tian, Wei Huang, Qixiang Ye, Qi Dai, Lingxi Xie, Qi Tian.
   - HiViT: Hierarchical Vision Transformer Meets Masked Image Modeling. [[ICLR'2023](https://arxiv.org/abs/2205.14949)]
   <p align="center"><img width="80%" src="https://user-images.githubusercontent.com/44519745/204306642-4764b620-0a1d-4625-8f22-e0fbcc3f5b2e.png" /></p>
* **FD**: Yixuan Wei, Han Hu, Zhenda Xie, Zheng Zhang, Yue Cao, Jianmin Bao, Dong Chen, Baining Guo.
   - Contrastive Learning Rivals Masked Image Modeling in Fine-tuning via Feature Distillation. [[ArXiv'2022](https://arxiv.org/abs/2205.14141)] [[code](https://github.com/SwinTransformer/Feature-Distillation)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204306965-8c8ccfd7-353d-431a-819b-9872cc95bf9b.png" /></p>
* **ObjMAE**: Jiantao Wu, Shentong Mo.
   - Object-wise Masked Autoencoders for Fast Pre-training. [[ArXiv'2022](https://arxiv.org/abs/2205.14338)]
   <p align="center"><img width="80%" src="https://user-images.githubusercontent.com/44519745/204307186-fcca6049-8ed6-4010-967b-b7cf93bd0619.png" /></p>
* **LoMaR**: Jun Chen, Ming Hu, Boyang Li, Mohamed Elhoseiny.
   - Efficient Self-supervised Vision Pretraining with Local Masked Reconstruction. [[ArXiv'2022](https://arxiv.org/abs/2206.00790)] [[code](https://github.com/junchen14/LoMaR)]
   <p align="center"><img width="70%" src="https://user-images.githubusercontent.com/44519745/204307493-233177c7-3a18-4228-9d3b-34678dee8fe3.png" /></p>
* **ExtreMA**: Zhirong Wu, Zihang Lai, Xiao Sun, Stephen Lin.
   - Extreme Masking for Learning Instance and Distributed Visual Representations. [[ArXiv'2022](https://arxiv.org/abs/2206.04667)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204307667-973af3e2-e50a-4cf7-9a31-035668aed4e3.png" /></p>
* **BEiT.V2**: Zhiliang Peng, Li Dong, Hangbo Bao, Qixiang Ye, Furu Wei.
   - BEiT v2: Masked Image Modeling with Vector-Quantized Visual Tokenizers. [[ArXiv'2022](http://arxiv.org/abs/2208.06366)] [[code](https://aka.ms/beit)]
   <p align="center"><img width="95%" src="https://user-images.githubusercontent.com/44519745/204307878-40ba7e59-2894-4a8e-93d5-8a8d43f12744.png" /></p>
* **MILAN**: Zejiang Hou, Fei Sun, Yen-Kuang Chen, Yuan Xie, Sun-Yuan Kung.
   - MILAN: Masked Image Pretraining on Language Assisted Representation. [[ArXiv'2022](https://arxiv.org/abs/2208.06049)] [[code](https://github.com/zejiangh/milan)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204308146-edae9cfb-3f03-4b13-bf11-51620ebc945d.png" /></p>
* **BEiT.V3**: Wenhui Wang, Hangbo Bao, Li Dong, Johan Bjorck, Zhiliang Peng, Qiang Liu, Kriti Aggarwal, Owais Khan Mohammed, Saksham Singhal, Subhojit Som, Furu Wei.
   - Image as a Foreign Language: BEiT Pretraining for All Vision and Vision-Language Tasks. [[ArXiv'2022](https://arxiv.org/abs/2208.10442)] [[code](https://github.com/microsoft/unilm/tree/master/beit)]
   <p align="center"><img width="70%" src="https://user-images.githubusercontent.com/44519745/204308318-b1d80584-2b7e-4c35-bb68-171c9bfaf299.png" /></p>
* **DMAE**: Yutong Bai, Zeyu Wang, Junfei Xiao, Chen Wei, Huiyu Wang, Alan Yuille, Yuyin Zhou, Cihang Xie.
   - Masked Autoencoders Enable Efficient Knowledge Distillers. [[ArXiv'2022](https://arxiv.org/abs/2208.12256)] [[code](https://github.com/UCSC-VLAA/DMAE)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204308505-f730651b-6e24-4496-9c6d-879b2f446793.png" /></p>
* **RC-MAE**: Youngwan Lee, Jeffrey Willette, Jonghee Kim, Juho Lee, Sung Ju Hwang.
   - Exploring The Role of Mean Teachers in Self-supervised Masked Auto-Encoders. [[ICLR'2023](https://arxiv.org/abs/2210.02077)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204310107-ff38a657-9fac-4271-89a2-e28a2805bf5a.png" /></p>
* **DMAE**: Quanlin Wu, Hang Ye, Yuntian Gu, Huishuai Zhang, Liwei Wang, Di He.
   - Denoising Masked AutoEncoders are Certifiable Robust Vision Learners. [[ArXiv'2022](https://arxiv.org/abs/2210.06983)] [[code](https://github.com/quanlin-wu/dmae)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204310334-f2bb8c49-d2a5-4017-9501-b0bd76340bdc.png" /></p>
* **MaskDistill**: Zhiliang Peng, Li Dong, Hangbo Bao, Qixiang Ye, Furu Wei.
   - A Unified View of Masked Image Modeling. [[ArXiv'2022](https://arxiv.org/abs/2210.10615)] [[code](https://aka.ms/unimim)]
   <p align="center"><img width="80%" src="https://user-images.githubusercontent.com/44519745/204310534-7c1bf6fc-690b-4dd3-889d-4488b8a892ea.png" /></p>
* **MaskVLM**: Gukyeong Kwon, Zhaowei Cai, Avinash Ravichandran, Erhan Bas, Rahul Bhotika, Stefano Soatto.
   - Masked Vision and Language Modeling for Multi-modal Representation Learning. [[ICLR'2023](https://arxiv.org/abs/2208.02131)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204310845-3e7777dc-5726-4c94-9506-8f88efd1966b.png" /></p>
* **DILEMMA**: Sepehr Sameni, Simon Jenni, Paolo Favaro.
   - DILEMMA: Self-Supervised Shape and Texture Learning with Transformers. [[AAAI'2023](https://arxiv.org/abs/2204.04788)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/206920238-6f520585-e9c1-4e7a-89eb-3d9379931279.png" /></p>
* **MaskCLIP**: Xiaoyi Dong, Yinglin Zheng, Jianmin Bao, Ting Zhang, Dongdong Chen, Hao Yang, Ming Zeng, Weiming Zhang, Lu Yuan, Dong Chen, Fang Wen, Nenghai Yu.
   - MaskCLIP: Masked Self-Distillation Advances Contrastive Language-Image Pretraining. [[ArXiv'2022](https://arxiv.org/abs/2208.12262)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/209704378-5c467c07-8096-441d-b8a4-37fe27d1ac07.png" /></p>
* **i-MAE**: Kevin Zhang, Zhiqiang Shen.
   - i-MAE: Are Latent Representations in Masked Autoencoders Linearly Separable? [[ArXiv'2022](https://arxiv.org/abs/2210.11470)] [[code](https://github.com/vision-learning-acceleration-lab/i-mae)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/211220785-5031f97c-c9a3-4ade-b344-48db01fc3760.png" /></p>
* **EVA**: Yuxin Fang, Wen Wang, Binhui Xie, Quan Sun, Ledell Wu, Xinggang Wang, Tiejun Huang, Xinlong Wang, Yue Cao.
   - EVA: Exploring the Limits of Masked Visual Representation Learning at Scale. [[CVPR'2023](https://arxiv.org/abs/2211.07636)] [[code](https://github.com/baaivision/EVA)]
   <p align="center"><img width="60%" src="https://user-images.githubusercontent.com/44519745/206920442-4d896aca-1765-4e66-9afb-c76017bc3521.png" /></p>
* **CAE**: Xiaokang Chen, Mingyu Ding, Xiaodi Wang, Ying Xin, Shentong Mo, Yunhao Wang, Shumin Han, Ping Luo, Gang Zeng, Jingdong Wang.
   - Context Autoencoder for Self-Supervised Representation Learning. [[ArXiv'2022](https://arxiv.org/abs/2202.03026)] [[code](https://github.com/lxtGH/CAE)]
   <p align="center"><img width="75%" src="https://user-images.githubusercontent.com/44519745/234667973-6f98f65e-662c-4934-be85-efa60f3fc20a.png" /></p>
* **CAE.V2**: Xinyu Zhang, Jiahui Chen, Junkun Yuan, Qiang Chen, Jian Wang, Xiaodi Wang, Shumin Han, Xiaokang Chen, Jimin Pi, Kun Yao, Junyu Han, Errui Ding, Jingdong Wang.
   - CAE v2: Context Autoencoder with CLIP Target. [[ArXiv'2022](https://arxiv.org/abs/2211.09799)]
   <p align="center"><img width="95%" src="https://user-images.githubusercontent.com/44519745/206920593-c703518b-47f9-4f61-a319-5ba0099c902d.png" /></p>
* **FastMIM**: Jianyuan Guo, Kai Han, Han Wu, Yehui Tang, Yunhe Wang, Chang Xu.
   - FastMIM: Expediting Masked Image Modeling Pre-training for Vision. [[ArXiv'2022](https://arxiv.org/abs/2212.06593)]
   <p align="center"><img width="95%" src="https://user-images.githubusercontent.com/44519745/210276245-83f9b564-2bdb-48b7-922c-dc36e3d5c20f.png" /></p>
* **dBOT**: Xingbin Liu, Jinghao Zhou, Tao Kong, Xianming Lin, Rongrong Ji.
   - Exploring Target Representations for Masked Autoencoders. [[ArXiv'2022](https://arxiv.org/abs/2209.03917)] [[code](https://github.com/liuxingbin/dbot)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/225108834-36affd27-fbae-46f0-92ca-d5a35a39023d.png" /></p>
* **Data2Vec.V2**: Alexei Baevski, Arun Babu, Wei-Ning Hsu, and Michael Auli.
   - Efficient Self-supervised Learning with Contextualized Target Representations for Vision, Speech and Language. [[ArXiv'2022](https://arxiv.org/abs/2212.07525)] [[code](https://github.com/facebookresearch/fairseq/tree/main/examples/data2vec)]
   <p align="center"><img width="95%" src="https://user-images.githubusercontent.com/44519745/207722013-4fc539f7-3d45-4eb8-8037-c4fa210738d6.png" /></p>
* **FLIP**: Yanghao Li, Haoqi Fan, Ronghang Hu, Christoph Feichtenhofer, Kaiming He.
   - Scaling Language-Image Pre-training via Masking. [[ArXiv'2022](https://arxiv.org/abs/2212.00794)]
   <p align="center"><img width="55%" src="https://user-images.githubusercontent.com/44519745/209705278-368b8125-cb14-4800-8523-09800b1728d4.png" /></p>
* **A-CLIP**: Yifan Yang, Weiquan Huang, Yixuan Wei, Houwen Peng, Xinyang Jiang, Huiqiang Jiang, Fangyun Wei, Yin Wang, Han Hu, Lili Qiu, Yuqing Yang.
   - Attentive Mask CLIP. [[ArXiv'2022](https://arxiv.org/abs/2212.08653)]
   <p align="center"><img width="55%" src="https://user-images.githubusercontent.com/44519745/209704869-a0eee2b2-0b21-4be1-8bfa-074758f3b4a2.png" /></p>
* **SDMAE**: Jiawei Mao, Honggu Zhou, Xuesong Yin, Yuanqi Chang. Binling Nie. Rui Xu.
   - Masked autoencoders are effective solution to transformer data-hungry. [[ArXiv'2022](https://arxiv.org/abs/2212.05677)] [[code](https://github.com/Talented-Q/SDMAE)]
   <p align="center"><img width="95%" src="https://user-images.githubusercontent.com/44519745/211220908-70f4c587-80a9-4427-8a68-b17593de8b0a.png" /></p>
* **TinyMIM**: Sucheng Ren, Fangyun Wei, Zheng Zhang, Han Hu.
   - TinyMIM: An Empirical Study of Distilling MIM Pre-trained Models. [[ArXiv'2023](https://arxiv.org/abs/2301.01296)] [[code](https://github.com/OliverRensu/TinyMIM)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/210646611-f5022c04-9c34-465c-b4dd-53ca097f47d8.png" /></p>
* **DMJD**: Xin Ma, Chang Liu, Chunyu Xie, Long Ye, Yafeng Deng, Xiangyang Ji.
   - Disjoint Masking with Joint Distillation for Efficient Masked Image Modeling. [[ArXiv'2023](https://arxiv.org/abs/2301.00230)] [[code](https://github.com/mx-mark/dmjd)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/210645728-7a066877-9eea-4fdb-a13a-df6863a287e6.png" /></p>
* **MAGE**: Tianhong Li, Huiwen Chang, Shlok Kumar Mishra, Han Zhang, Dina Katabi, Dilip Krishnan.
   - MAGE: MAsked Generative Encoder to Unify Representation Learning and Image Synthesis. [[CVPR'2023](https://arxiv.org/abs/2211.09117)] [[code](https://github.com/lth14/mage)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/224833197-6d95863c-cb83-4d9d-a900-b4f61baba785.png" /></p>
* **MixedAE**: Kai Chen, Zhili Liu, Lanqing Hong, Hang Xu, Zhenguo Li, Dit-Yan Yeung.
   - Mixed Autoencoder for Self-supervised Visual Representation Learning. [[CVPR'2023](https://arxiv.org/abs/2303.17152)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/229929023-1ea53237-ebfb-4203-8b93-dd761d937b27.png" /></p>
* **LocalMAE**: Haoqing Wang, Yehui Tang, Yunhe Wang, Jianyuan Guo, Zhi-Hong Deng, Kai Han.
   - Masked Image Modeling with Local Multi-Scale Reconstruction. [[CVPR'2023](https://arxiv.org/abs/2303.05251)] [[code](https://github.com/Haoqing-Wang/LocalMIM)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/233732370-4ad8b717-5a86-4957-8d8a-494cc9198685.png" /></p>
* **MaskAlign**: Hongwei Xue, Peng Gao, Hongyang Li, Yu Qiao, Hao Sun, Houqiang Li, Jiebo Luo.
   - Stare at What You See: Masked Image Modeling without Reconstruction. [[CVPR'2023](https://arxiv.org/abs/2211.08887)] [[code](https://github.com/OpenPerceptionX/maskalign)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/236316028-df4132f1-2e76-4cef-8f88-ce1d3e84b127.png" /></p>
* **MOMA**: Yuchong Yao, Nandakishor Desai, Marimuthu Palaniswami.
   - MOMA: Distill from Self-Supervised Teachers. [[arXiv'2023](https://arxiv.org/abs/2302.02089)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/236316583-28639d42-3574-4dcc-8bd4-da377cce29a4.png" /></p>
* **PixMIM**: Yuan Liu, Songyang Zhang, Jiacheng Chen, Kai Chen, Dahua Lin.
   - PixMIM: Rethinking Pixel Reconstruction in Masked Image Modeling. [[arXiv'2023](https://arxiv.org/abs/2303.02416)] [[code](https://github.com/open-mmlab/mmselfsup/tree/dev-1.x/configs/selfsup/pixmim)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/236320141-75a1c36e-ab6e-4bbe-bc46-b94f91db1439.png" /></p>
* **Img2Vec**: Heng Pan, Chenyang Liu, Wenxiao Wang, Li Yuan, Hongfa Wang, Zhifeng Li, Wei Liu.
   - Img2Vec: A Teacher of High Token-Diversity Helps Masked AutoEncoders. [[arXiv'2023](https://arxiv.org/abs/2304.12535)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/236318192-b39c9900-db30-4e18-bb1b-a5020723b906.png" /></p>

<p align="right">(<a href="#top">back to top</a>)</p>

### MIM with Constrastive Learning

* **MST**: Zhaowen Li, Zhiyang Chen, Fan Yang, Wei Li, Yousong Zhu, Chaoyang Zhao, Rui Deng, Liwei Wu, Rui Zhao, Ming Tang, Jinqiao Wang.
   - MST: Masked Self-Supervised Transformer for Visual Representation. [[NIPS'2021](https://arxiv.org/abs/2106.05656)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204311330-9652d5d0-4b94-4f9a-afcd-efc12c712279.png" /></p>
* **SplitMask**: Alaaeldin El-Nouby, Gautier Izacard, Hugo Touvron, Ivan Laptev, Hervé Jegou, Edouard Grave.
   - Are Large-scale Datasets Necessary for Self-Supervised Pre-training? [[ArXiv'2021](https://arxiv.org/abs/2112.10740)]
   <p align="center"><img width="60%" src="https://user-images.githubusercontent.com/44519745/204311839-6f1310c9-88b2-4f43-90ff-927cf8aba720.png" /></p>
* **MSN**: Mahmoud Assran, Mathilde Caron, Ishan Misra, Piotr Bojanowski, Florian Bordes, Pascal Vincent, Armand Joulin, Michael Rabbat, Nicolas Ballas.
   - Masked Siamese Networks for Label-Efficient Learning. [[ArXiv'2022](https://arxiv.org/abs/2204.07141)] [[code](https://github.com/facebookresearch/msn)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/204312102-a35d65ac-61e6-46ba-bb86-6c18b8562966.png" /></p>
* **SIM**: Chenxin Tao, Xizhou Zhu, Gao Huang, Yu Qiao, Xiaogang Wang, Jifeng Dai.
   - Siamese Image Modeling for Self-Supervised Vision Representation Learning. [[ArXiv'2022](https://arxiv.org/abs/2206.01204)] [[code](https://github.com/fundamentalvision/Siamese-Image-Modeling)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204312408-fe573880-62ac-4f6e-b7ed-c9163f0cea96.png" /></p>
* **ConMIM**: Kun Yi, Yixiao Ge, Xiaotong Li, Shusheng Yang, Dian Li, Jianping Wu, Ying Shan, Xiaohu Qie.
   - Masked Image Modeling with Denoising Contrast. [[ICLR'2023](https://arxiv.org/abs/2205.09616)] [[code](https://github.com/TencentARC/ConMIM)]
   <p align="center"><img width="80%" src="https://user-images.githubusercontent.com/44519745/204312585-13d5094b-c90c-4ab6-88d1-b88d46d8ae62.png" /></p>
* **RePre**: Luya Wang, Feng Liang, Yangguang Li, Honggang Zhang, Wanli Ouyang, Jing Shao.
   - RePre: Improving Self-Supervised Vision Transformer with Reconstructive Pre-training. [[ArXiv'2022](https://arxiv.org/abs/2201.06857)]
   <p align="center"><img width="95%" src="https://user-images.githubusercontent.com/44519745/204312825-03953a52-0c1a-4f7e-bf12-e13841c2d371.png" /></p>
* **MSCN**: Li Jing, Jiachen Zhu, Yann LeCun.
   - Masked Siamese ConvNets. [[ArXiv'2022](https://arxiv.org/abs/2206.07700)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/216648027-99790176-87fa-4fc6-ad5f-a8fe255c60e6.png" /></p>
* **CMAE**: Zhicheng Huang, Xiaojie Jin, Chengze Lu, Qibin Hou, Ming-Ming Cheng, Dongmei Fu, Xiaohui Shen, Jiashi Feng.
   - Contrastive Masked Autoencoders are Stronger Vision Learners. [[ArXiv'2022](https://arxiv.org/abs/2207.13532)] [[code](https://github.com/ZhichengHuang/CMAE)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/204313292-54630e16-e8ea-4281-a922-1b08c860e721.png" /></p>
* **CAN**: Shlok Mishra, Joshua Robinson, Huiwen Chang, David Jacobs, Aaron Sarna, Aaron Maschinot, Dilip Krishnan.
   - A simple, efficient and scalable contrastive masked autoencoder for learning visual representations. [[ArXiv'2022](https://arxiv.org/abs/2210.16870)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/204313772-7c0bf6d4-8df1-4b05-8733-da5024513e10.png" /></p>
* **MimCo**: Qiang Zhou, Chaohui Yu, Hao Luo, Zhibin Wang, Hao Li.
   - MimCo: Masked Image Modeling Pre-training with Contrastive Teacher. [[ArXiv'2022](https://arxiv.org/abs/2209.03063)]
   <p align="center"><img width="95%" src="https://user-images.githubusercontent.com/44519745/216651122-8fe6a039-37a8-4bec-8988-2760006da0af.png" /></p>
* **ccMIM**: Shaofeng Zhang, Feng Zhu, Rui Zhao, Junchi Yan.
   - Contextual Image Masking Modeling via Synergized Contrasting without View Augmentation for Faster and Better Visual Pretraining. [[ICLR'2023](https://openreview.net/forum?id=A3sgyt4HWp)] [[code](https://github.com/Sherrylone/ccMIM)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204314041-63c5e06d-b870-482d-8f6b-e70e1af9d642.png" /></p>
* **U-MAE**: Qi Zhang, Yifei Wang, Yisen Wang.
   - How Mask Matters: Towards Theoretical Understandings of Masked Autoencoders. [[NIP'2022](https://arxiv.org/abs/2210.08344)] [[code](https://github.com/vision-learning-acceleration-lab/i-mae)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/234359652-b34cb444-1c6b-4721-94e3-6bd60347ca55.png" /></p>
* **Layer Grafted**: Ziyu Jiang, Yinpeng Chen, Mengchen Liu, Dongdong Chen, Xiyang Dai, Lu Yuan, Zicheng Liu, Zhangyang Wang.
   - Layer Grafted Pre-training: Bridging Contrastive Learning And Masked Image Modeling For Label-Efficient Representations. [[ICLR'2023](https://openreview.net/forum?id=jwdqNwyREyh)] [[code](https://github.com/VITA-Group/layerGraftedPretraining_ICLR23)]
   <p align="center"><img width="80%" src="https://user-images.githubusercontent.com/44519745/224830983-13cfcbf5-f1df-481b-9e7c-24667d041fe4.png" /></p>

<p align="right">(<a href="#top">back to top</a>)</p>

### MIM for Transformers and CNNs

* **Context-Encoder**: Deepak Pathak, Philipp Krahenbuhl, Jeff Donahue, Trevor Darrell, Alexei A. Efros.
   - Context Encoders: Feature Learning by Inpainting. [[CVPR'2016](https://arxiv.org/abs/1604.07379)] [[code](https://github.com/pathak22/context-encoder)]
   <p align="center"><img width="70%" src="https://user-images.githubusercontent.com/44519745/204314544-4ad0e4a8-f7b8-47f9-80e9-67ef87c1b14a.png" /></p>
* **CIM**: Yuxin Fang, Li Dong, Hangbo Bao, Xinggang Wang, Furu Wei.
   - Corrupted Image Modeling for Self-Supervised Visual Pre-Training. [[ICLR'2023](https://arxiv.org/abs/2202.03382)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204315003-182e9ba5-5ab3-4d84-9544-8e0a3d8590c5.png" /></p>
* **A2MIM**: Siyuan Li, Di Wu, Fang Wu, Zelin Zang, Kai Wang, Lei Shang, Baigui Sun, Hao Li, Stan.Z.Li.
   - Architecture-Agnostic Masked Image Modeling - From ViT back to CNN. [[ICML'2023](https://arxiv.org/abs/2205.13943)] [[code](https://github.com/Westlake-AI/openmixup)] [[project](https://github.com/Westlake-AI/A2MIM)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204314681-d953cffc-8ba7-481c-925e-c89084f83c56.png" /></p>
* **MFM**: Jiahao Xie, Wei Li, Xiaohang Zhan, Ziwei Liu, Yew Soon Ong, Chen Change Loy.
   - Masked Frequency Modeling for Self-Supervised Visual Pre-Training. [[ICLR'2023](https://arxiv.org/abs/2206.07706)] [[code](https://github.com/CoinCheung/MFM)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/204315329-1a58598f-35cb-439c-91ee-303ddd36fa6c.png" /></p>
* **MixMIM**: Jihao Liu, Xin Huang, Yu Liu, Hongsheng Li.
   - MixMIM: Mixed and Masked Image Modeling for Efficient Visual Representation Learning. [[ArXiv'2022](https://arxiv.org/abs/2205.13137)] [[code](https://github.com/Sense-X/MixMIM)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204315480-5c59ed60-7b5f-4da9-85fb-551a961fd731.png" /></p>
* **MRA**: Haohang Xu, Shuangrui Ding, Xiaopeng Zhang, Hongkai Xiong, Qi Tian.
   - Masked Autoencoders are Robust Data Augmentors. [[ArXiv'2022](https://arxiv.org/abs/2206.04846)] [[code](https://github.com/haohang96/mra)]
   <p align="center"><img width="75%" src="https://user-images.githubusercontent.com/44519745/204315634-212c14b9-7d6d-4ad0-880b-35cafb623249.png" /></p>
* **SparK**: Keyu Tian, Yi Jiang, Qishuai Diao, Chen Lin, Liwei Wang, Zehuan Yuan.
   - Designing BERT for Convolutional Networks: Sparse and Hierarchical Masked Modeling. [[ArXiv'2023](https://arxiv.org/abs/2301.03580)] [[OpenReview'2022](https://openreview.net/pdf?id=NRxydtWup1S)] [[code](https://github.com/keyu-tian/spark)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/204315983-d5a24e55-fab4-4336-a1ed-3428a997aebd.png" /></p>
* **ConvNeXt.V2**: Sanghyun Woo, Shoubhik Debnath, Ronghang Hu, Xinlei Chen, Zhuang Liu, In So Kweon, Saining Xie.
   - ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders. [[ArXiv'2023](https://arxiv.org/abs/2301.00808)] [[code](https://github.com/facebookresearch/ConvNeXt-V2)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/211898674-caa94c81-9aea-4544-8f5f-2cf410724bb4.png" /></p>

<p align="right">(<a href="#top">back to top</a>)</p>

### MIM with Advanced Masking

* **ADIOS**: Yuge Shi, N. Siddharth, Philip H.S. Torr, Adam R. Kosiorek.
   - Adversarial Masking for Self-Supervised Learning. [[ICML'2022](https://arxiv.org/abs/2201.13100)] [[code](https://github.com/YugeTen/adios)]
   <p align="center"><img width="70%" src="https://user-images.githubusercontent.com/44519745/204316447-66b223b7-1518-477d-9d5f-66bd3148eecd.png" /></p>
* **AttMask**: Ioannis Kakogeorgiou, Spyros Gidaris, Bill Psomas, Yannis Avrithis, Andrei Bursuc, Konstantinos Karantzalos, Nikos Komodakis.
   - What to Hide from Your Students: Attention-Guided Masked Image Modeling. [[ECCV'2022](https://arxiv.org/abs/2203.12719)] [[code](https://github.com/gkakogeorgiou/attmask)]
   <p align="center"><img width="65%" src="https://user-images.githubusercontent.com/44519745/204316717-191ef56d-c703-4b12-9c71-28bd14371d32.png" /></p>
* **UnMAE**: Xiang Li, Wenhai Wang, Lingfeng Yang, Jian Yang.
   - Uniform Masking: Enabling MAE Pre-training for Pyramid-based Vision Transformers with Locality. [[ArXiv'2022](https://arxiv.org/abs/2205.10063)] [[code](https://github.com/implus/um-mae)]
   <p align="center"><img width="80%" src="https://user-images.githubusercontent.com/44519745/204316895-a04d2141-4dc9-47db-9176-001d71dcc704.png" /></p>
* **SemMAE**: Gang Li, Heliang Zheng, Daqing Liu, Chaoyue Wang, Bing Su, Changwen Zheng.
   - SemMAE: Semantic-Guided Masking for Learning Masked Autoencoders. [[NIPS'2022](https://arxiv.org/abs/2206.10207)] [[code](https://github.com/ucasligang/semmae)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/204317096-f6ade707-6f66-4826-823e-e14d0784b960.png" /></p>
* **HPM**: Haochen Wang, Kaiyou Song, Junsong Fan, Yuxi Wang, Jin Xie, Zhaoxiang Zhang.
   - Hard Patches Mining for Masked Image Modeling. [[CVPR'2023](https://arxiv.org/abs/2304.05919)] [[code](https://github.com/Haochen-Wang409/HPM)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/232319362-d6a5419f-6a95-4405-a615-f8ded42c1896.png" /></p>
* **AutoMAE**: Haijian Chen, Wendong Zhang, Yunbo Wang, Xiaokang Yang.
   - Improving Masked Autoencoders by Learning Where to Mask. [[arXiv'2023](https://arxiv.org/abs/2303.06583)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/236310631-a11eee44-3e70-414f-9caa-ad09a231ce31.png" /></p>

<p align="right">(<a href="#top">back to top</a>)</p>

## MIM for Downstream Tasks

### Object Detection

* **MIMDet**: Yuxin Fang, Shusheng Yang, Shijie Wang, Yixiao Ge, Ying Shan, Xinggang Wang.
   - Unleashing Vanilla Vision Transformer with Masked Image Modeling for Object Detection. [[ArXiv'2022](https://arxiv.org/abs/2204.02964)] [[code](https://github.com/hustvl/MIMDet)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/207723589-e1fd22e3-0719-422e-b94d-371c51b164e5.png" /></p>
* **SeqCo-DETR**: Guoqiang Jin, Fan Yang, Mingshan Sun, Ruyi Zhao, Yakun Liu, Wei Li, Tianpeng Bao, Liwei Wu, Xingyu Zeng, Rui Zhao.
   - SeqCo-DETR: Sequence Consistency Training for Self-Supervised Object Detection with Transformers. [[ArXiv'2022](https://arxiv.org/abs/2303.08481)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/226742022-7b823b2b-a08c-4579-8f33-8f35b282069a.png" /></p>
* **iTPN**: Yunjie Tian, Lingxi Xie, Zhaozhi Wang, Longhui Wei, Xiaopeng Zhang, Jianbin Jiao, Yaowei Wang, Qi Tian, Qixiang Ye.
   - Integrally Pre-Trained Transformer Pyramid Networks. [[CVPR'2023](https://arxiv.org/abs/2211.12735)] [[code](https://github.com/sunsmarterjie/iTPN)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/231279943-851af288-fe43-44ba-aa85-3ca6ee72a247.png" /></p>

### Video Rrepresentation

* **VideoMAE**: Zhan Tong, Yibing Song, Jue Wang, Limin Wang.
   - VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training. [[NIPS'2022](https://arxiv.org/abs/2203.12602)] [[code](https://github.com/MCG-NJU/VideoMAE)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/207724710-e4093d2e-8d6c-40b9-bf7d-ab519eb97dd2.png" /></p>
* **VideoMAE.V2**: Limin Wang, Bingkun Huang, Zhiyu Zhao, Zhan Tong, Yinan He, Yi Wang, Yali Wang, Yu Qiao.
   - VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking. [[CVPR'2023](https://arxiv.org/abs/2303.16727)] [[code](https://github.com/MCG-NJU/VideoMAE)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/231277665-7027e34b-7b2c-4306-ac73-7be08b176f09.png" /></p>
* **MAE**: Christoph Feichtenhofer, Haoqi Fan, Yanghao Li, Kaiming He.
   - Masked Autoencoders As Spatiotemporal Learners. [[NIPS'2022](https://arxiv.org/abs/2205.09113)] [[code](https://github.com/facebookresearch/SlowFast)]
   <p align="center"><img width="75%" src="https://user-images.githubusercontent.com/44519745/207725088-8bccb8df-a9c8-4ba6-b7cd-5f259c0959c1.png" /></p>
* **FMNet**: Yiran Wang, Zhiyu Pan, Xingyi Li, Zhiguo Cao, Ke Xian, Jianming Zhang.
   - Less is More: Consistent Video Depth Estimation with Masked Frames Modeling. [[ACMMM'2022](https://arxiv.org/abs/2208.00380)] [[code](https://github.com/RaymondWang987/FMNet)]
   <p align="center"><img width="80%" src="https://user-images.githubusercontent.com/44519745/207725289-efef0f35-77a7-4ad4-896a-f1c84503cbb5.png" /></p>
* **MaskViT**: Agrim Gupta, Stephen Tian, Yunzhi Zhang, Jiajun Wu, Roberto Martín-Martín, Li Fei-Fei.
   - MaskViT: Masked Visual Pre-Training for Video Prediction. [[CVPR'2022](https://arxiv.org/abs/2206.11894)] [[code](https://github.com/agrimgupta92/maskvit)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/207725785-e8b125ff-22c1-451a-b1d8-101c13113189.png" /></p>
* **OmniMAE**: Rohit Girdhar, Alaaeldin El-Nouby, Mannat Singh, Kalyan Vasudev Alwala, Armand Joulin, Ishan Misra.
   - OmniMAE: Single Model Masked Pretraining on Images and Videos. [[ArXiv'2022](http://arxiv.org/abs/2206.08356)] [[code](https://github.com/facebookresearch/omnivore)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/207725594-3beaf158-74f6-4fed-a330-d34755d1f37a.png" /></p>
* **MILES**: Yuying Ge, Yixiao Ge, Xihui Liu, Alex Jinpeng Wang, Jianping Wu, Ying Shan, Xiaohu Qie, Ping Luo.
   - MILES: Visual BERT Pre-training with Injected Language Semantics for Video-text Retrieval. [[ArXiv'2022](https://arxiv.org/abs/2204.12408)] [[code](https://github.com/tencentarc/mcq)]
   <p align="center"><img width="95%" src="https://user-images.githubusercontent.com/44519745/207725934-fc1c45cc-3946-4617-9eff-f93bd2903ba6.png" /></p>
* **MAR**: Zhiwu Qing, Shiwei Zhang, Ziyuan Huang, Xiang Wang, Yuehuan Wang, Yiliang Lv, Changxin Gao, Nong Sang.
   - MAR: Masked Autoencoders for Efficient Action Recognition. [[ArXiv'2022](http://arxiv.org/abs/2207.11660)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/207726266-39eb361a-7e3c-4737-a51b-bfda8ad8ed06.png" /></p>
* **MotionMAE**: Haosen Yang, Deng Huang, Bin Wen, Jiannan Wu, Hongxun Yao, Yi Jiang, Xiatian Zhu, Zehuan Yuan.
   - Self-supervised Video Representation Learning with Motion-Aware Masked Autoencoders. [[ArXiv'2022](https://arxiv.org/abs/2210.04154)] [[code](https://github.com/happy-hsy/MotionMAE)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/207726409-07a0255c-a7ae-4e6c-aa25-fdfa77393788.png" /></p>
* **MAM2**: Yuxin Song, Min Yang, Wenhao Wu, Dongliang He, Fu Li, Jingdong Wang.
   - It Takes Two: Masked Appearance-Motion Modeling for Self-supervised Video Transformer Pre-training. [[ArXiv'2022](https://arxiv.org/abs/2210.05234)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/234365532-88126c05-712d-4f1f-bba6-4d20a33a9c12.png" /></p>
* **MIMT**: Jinxi Xiang, Kuan Tian, Jun Zhang.
   - MIMT: Masked Image Modeling Transformer for Video Compression. [[ICLR'2023](https://openreview.net/forum?id=j9m-mVnndbm)]
   <p align="center"><img width="80%" src="https://user-images.githubusercontent.com/44519745/207726629-e9481b07-58a4-4afb-be42-1a315bccd10c.png" /></p>
* **DropMAE**: Qiangqiang Wu, Tianyu Yang, Ziquan Liu, Baoyuan Wu, Ying Shan, Antoni B. Chan.
   - DropMAE: Masked Autoencoders with Spatial-Attention Dropout for Tracking Tasks. [[CVPR'2023](https://arxiv.org/abs/2304.00571)] [[code](https://github.com/jimmy-dq/dropmae)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/229926942-c661dff0-1cba-43cd-a206-435f223d8fd6.png" /></p>
* **MAGVIT**: Lijun Yu, Yong Cheng, Kihyuk Sohn, José Lezama, Han Zhang, Huiwen Chang, Alexander G. Hauptmann, Ming-Hsuan Yang, Yuan Hao, Irfan Essa, Lu Jiang.
   - MAGVIT: Masked Generative Video Transformer. [[CVPR'2023](https://arxiv.org/abs/2212.05199)] [[code](https://github.com/MAGVIT/magvit)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/234349205-1831ce49-2e39-440b-a9b6-916d831f0502.png" /></p>
* **CMAE-V**: Cheng-Ze Lu, Xiaojie Jin, Zhicheng Huang, Qibin Hou, Ming-Ming Cheng, Jiashi Feng.
   - CMAE-V: Contrastive Masked Autoencoders for Video Action Recognition. [[arXiv'2023](https://arxiv.org/abs/2301.06018)]
   <p align="center"><img width="85%" src="https://user-images.githubusercontent.com/44519745/236318547-a6b49259-bcd5-4e76-b5a9-c20c19a65719.png" /></p>

### Knowledge Distillation

* **G2SD**: Wei Huang, Zhiliang Peng, Li Dong, Furu Wei, Jianbin Jiao, Qixiang Ye.
   - Generic-to-Specific Distillation of Masked Autoencoders. [[CVPR'2023](https://arxiv.org/abs/2302.14771)] [[code](https://github.com/pengzhiliang/G2SD)]
   <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/229930409-40ca4ec9-68df-4eed-ae49-67f513a99277.png" /></p>

### Efficient Fine-tuning

* **MAE-CT**: Johannes Lehner, Benedikt Alkin, Andreas Fürst, Elisabeth Rumetshofer, Lukas Miklautz, Sepp Hochreiter.
   - Contrastive Tuning: A Little Help to Make Masked Autoencoders Forget. [[arXiv'2023](https://arxiv.org/abs/2304.10520)] [[code](https://github.com/ml-jku/MAE-CT)]
   <!-- <p align="center"><img width="90%" src="https://user-images.githubusercontent.com/44519745/236308666-b5904b49-dd4e-4dc5-9ee2-158eb3e616e5.png" /></p> -->

### Medical Image

* **MedMAE**: Lei Zhou, Huidong Liu, Joseph Bae, Junjun He, Dimitris Samaras, Prateek Prasanna.
   - Self Pre-training with Masked Autoencoders for Medical Image Analysis. [[ArXiv'2022](https://arxiv.org/abs/2203.05573)]
* **SD-MAE**: Yang Luo, Zhineng Chen, Xieping Gao.
   - Self-distillation Augmented Masked Autoencoders for Histopathological Image Classification. [[ArXiv'2022](https://arxiv.org/abs/2203.16983)]
* **GCMAE**: Hao Quan, Xingyu Li, Weixing Chen, Qun Bai, Mingchen Zou, Ruijie Yang, Tingting Zheng, Ruiqun Qi, Xinghua Gao, Xiaoyu Cui.
   - Global Contrast Masked Autoencoders Are Powerful Pathological Representation Learners. [[ArXiv'2022](https://arxiv.org/abs/2205.09048)] [[code](https://github.com/staruniversus/gcmae)]
* **FreMAE**: Wenxuan Wang, Jing Wang, Chen Chen, Jianbo Jiao, Lichao Sun, Yuanxiu Cai, Shanshan Song, Jiangyun Li.
   - FreMAE: Fourier Transform Meets Masked Autoencoders for Medical Image Segmentation. [[ArXiv'2023](https://arxiv.org/abs/2304.10864)]

* **3DMIM_Medical**: Zekai Chen, Devansh Agarwal, Kshitij Aggarwal, Wiem Safta, Samit Hirawat, Venkat Sethuraman, Mariann Micsinai Balan, Kevin Brown.
   - Masked Image Modeling Advances 3D Medical Image Analysis. [[WACV'2023](https://arxiv.org/abs/2204.11716)] [[code](https://github.com/ZEKAICHEN/MIM-Med3D.)]

### Face Recognition

* **FaceMAE**: Kai Wang, Bo Zhao, Xiangyu Peng, Zheng Zhu, Jiankang Deng, Xinchao Wang, Hakan Bilen, Yang You.
   - FaceMAE: Privacy-Preserving Face Recognition via Masked Autoencoders. [[ArXiv'2022](https://arxiv.org/abs/2205.11090)] [[code](https://github.com/kaiwang960112/FaceMAE)]

### Scene Text Recognition (OCR)

* **MaskOCR**: Pengyuan Lyu, Chengquan Zhang, Shanshan Liu, Meina Qiao, Yangliu Xu, Liang Wu, Kun Yao, Junyu Han, Errui Ding, Jingdong Wang.
   - MaskOCR: Text Recognition with Masked Encoder-Decoder Pretraining. [[ArXiv'2022](https://arxiv.org/abs/2206.00311)]
* **DocMAE**: Shaokai Liu, Hao Feng, Wengang Zhou, Houqiang Li, Cong Liu, Feng Wu.
   - DocMAE: Document Image Rectification via Self-supervised Representation Learning. [[ICME'2023](https://arxiv.org/abs/2304.10341)]

### Remote Sensing Image

* **SatMAE**: Yezhen Cong, Samar Khanna, Chenlin Meng, Patrick Liu, Erik Rozi, Yutong He, Marshall Burke, David B. Lobell, Stefano Ermon.
   - SatMAE: Pre-training Transformers for Temporal and Multi-Spectral Satellite Imagery. [[ArXiv'2022](https://arxiv.org/abs/2207.08051)]
* **CMID**: Dilxat Muhtar, Xueliang Zhang, Pengfeng Xiao, Zhenshi Li, Feng Gu.
   - CMID: A Unified Self-Supervised Learning Framework for Remote Sensing Image Understanding. [[TGRS'2023](https://arxiv.org/abs/2304.09670)] [[code](https://github.com/NJU-LHRS/official-CMID)]

### 3D Point Cloud

* **PointBERT**: Xumin Yu, Lulu Tang, Yongming Rao, Tiejun Huang, Jie Zhou, Jiwen Lu.
   - Pre-Training 3D Point Cloud Transformers with Masked Point Modeling. [[CVPR'2022](https://arxiv.org/abs/2111.14819)] [[code](https://github.com/lulutang0608/Point-BERT)]
* **PointMAE**: Yatian Pang, Wenxiao Wang, Francis E.H. Tay, Wei Liu, Yonghong Tian, Li Yuan.
   - Masked Autoencoders for Point Cloud Self-supervised Learning. [[ECCV'2022](https://arxiv.org/abs/2203.06604)] [[code](https://github.com/Pang-Yatian/Point-MAE)]
* **MaskPoint**: Haotian Liu, Mu Cai, Yong Jae Lee.
   - Masked Discrimination for Self-Supervised Learning on Point Clouds. [[ECCV'2022](https://arxiv.org/abs/2203.11183)] [[code](https://github.com/haotian-liu/MaskPoint)]
* **MeshMAE**: Yaqian Liang, Shanshan Zhao, Baosheng Yu, Jing Zhang, Fazhi He.
   - MeshMAE: Masked Autoencoders for 3D Mesh Data Analysis. [[ECCV'2022](http://arxiv.org/abs/2207.10228)]
* **VoxelMAE**: Chen Min, Xinli Xu, Dawei Zhao, Liang Xiao, Yiming Nie, Bin Dai.
   - Voxel-MAE: Masked Autoencoders for Pre-training Large-scale Point Clouds. [[ArXiv'2022](https://arxiv.org/abs/2206.09900)]
* **Point-M2AE**: Renrui Zhang, Ziyu Guo, Peng Gao, Rongyao Fang, Bin Zhao, Dong Wang, Yu Qiao, Hongsheng Li.
   - Point-M2AE: Multi-scale Masked Autoencoders for Hierarchical Point Cloud Pre-training. [[NIPS'2022](https://arxiv.org/abs/2205.14401)] [[code](https://github.com/zrrskywalker/point-m2ae)]

### Reinforcement Learning

* **MLR**: Tao Yu, Zhizheng Zhang, Cuiling Lan, Yan Lu, Zhibo Chen.
   - Mask-based Latent Reconstruction for Reinforcement Learning. [[ArXiv'2022](https://arxiv.org/abs/2201.12096)]

### Audio

* **MAM**: Junkun Chen, Mingbo Ma, Renjie Zheng, Liang Huang.
   - MAM: Masked Acoustic Modeling for End-to-End Speech-to-Text Translation. [[ArXiv'2021](https://arxiv.org/abs/2010.11445)]
* **MAE-AST**: Alan Baade, Puyuan Peng, David Harwath.
   - MAE-AST: Masked Autoencoding Audio Spectrogram Transformer. [[ArXiv'2022](https://arxiv.org/abs/2203.16691)] [[code](https://github.com/AlanBaade/MAE-AST-Public)]
* **MaskSpec**: Dading Chong, Helin Wang, Peilin Zhou, Qingcheng Zeng.
   - Masked Spectrogram Prediction For Self-Supervised Audio Pre-Training. [[ArXiv'2022](https://arxiv.org/abs/2204.12768)] [[code](https://github.com/wanghelin1997/maskspec)]
* **Audio-MAE**: Po-Yao Huang, Hu Xu, Juncheng Li, Alexei Baevski, Michael Auli, Wojciech Galuba, Florian Metze, Christoph Feichtenhofer.
   - Masked Autoencoders that Listen. [[NIPS'2022](https://arxiv.org/abs/2207.06405)] [[code](https://github.com/facebookresearch/audiomae)]
* **CAV-MAE**: Yuan Gong, Andrew Rouditchenko, Alexander H. Liu, David Harwath, Leonid Karlinsky, Hilde Kuehne, James Glass.
   - Contrastive Audio-Visual Masked Autoencoder. [[ICLR'2023](https://arxiv.org/abs/2210.07839)]

<p align="right">(<a href="#top">back to top</a>)</p>

## Analysis and Understanding of MIM

* Yao-Hung Hubert Tsai, Yue Wu, Ruslan Salakhutdinov, Louis-Philippe Morency.
   - Demystifying Self-Supervised Learning: An Information-Theoretical Framework. [[ICLR'2021](https://arxiv.org/abs/2006.05576)] [[code](https://github.com/yaohungt/Self_Supervised_Learning_Multiview)]
* Nikunj Saunshi, Sadhika Malladi, Sanjeev Arora.
   - A Mathematical Exploration of Why Language Models Help Solve Downstream Tasks. [[ICLR'2021](https://arxiv.org/abs/2010.03648)]
* Jason D. Lee, Qi Lei, Nikunj Saunshi, Jiacheng Zhuo.
   - Predicting What You Already Know Helps: Provable Self-Supervised Learning. [[NIPS'2021](https://arxiv.org/abs/2008.01064)]
* Shuhao Cao, Peng Xu, David A. Clifton.
   - How to Understand Masked Autoencoders. [[ArXiv'2022](https://arxiv.org/abs/2202.03670)]
* Bingbin Liu, Daniel Hsu, Pradeep Ravikumar, Andrej Risteski.
   - Masked prediction tasks: a parameter identifiability view. [[ArXiv'2022](https://arxiv.org/abs/2202.09305)]
* Zhenda Xie, Zigang Geng, Jingcheng Hu, Zheng Zhang, Han Hu, Yue Cao.
   - Revealing the Dark Secrets of Masked Image Modeling. [[ArXiv'2022](https://arxiv.org/abs/2205.13543)]
* Siyuan Li, Di Wu, Fang Wu, Zelin Zang, Kai Wang, Lei Shang, Baigui Sun, Hao Li, Stan.Z.Li.
   - Architecture-Agnostic Masked Image Modeling - From ViT back to CNN. [[ArXiv'2022](https://arxiv.org/abs/2205.13943)] [[code](https://github.com/Westlake-AI/openmixup)]
* Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin, Yixuan Wei, Qi Dai, Han Hu.
   - On Data Scaling in Masked Image Modeling. [[CVPR'2023](https://arxiv.org/abs/2206.04664)] [[code](https://github.com/microsoft/Swin-Transformer)]
* Jiachun Pan, Pan Zhou, Shuicheng Yan.
   - Towards Understanding Why Mask-Reconstruction Pretraining Helps in Downstream Tasks. [[ArXiv'2022](https://arxiv.org/abs/2206.03826)]
* Gokul Karthik Kumar, Sahal Shaji Mullappilly, Abhishek Singh Gehlot.
   - An Empirical Study Of Self-supervised Learning Approaches For Object Detection With Transformers. [[ArXiv'2022](https://arxiv.org/abs/2205.05543)] [[code](https://github.com/gokulkarthik/deformable-detr)]
* Xiangwen Kong, Xiangyu Zhang.
   - Understanding Masked Image Modeling via Learning Occlusion Invariant Feature. [[ArXiv'2022](http://arxiv.org/abs/2208.04164)] [[code](https://github.com/zhangq327/u-mae)]
* Qi Zhang, Yifei Wang, Yisen Wang.
   - How Mask Matters: Towards Theoretical Understandings of Masked Autoencoders. [[NIP'2022](https://arxiv.org/abs/2210.08344)] [[code](https://github.com/vision-learning-acceleration-lab/i-mae)]
* Kevin Zhang, Zhiqiang Shen.
   - i-MAE: Are Latent Representations in Masked Autoencoders Linearly Separable? [[ArXiv'2022](https://arxiv.org/abs/2210.11470)]
* Yann Dubois, Tatsunori Hashimoto, Percy Liang.
   - Evaluating Self-Supervised Learning via Risk Decomposition. [[ICML'2023](https://arxiv.org/abs/2302.03068)] [[code](https://github.com/yanndubs/ssl-risk-decomposition)]
* Xu Tan, Tao Qin, Jiang Bian, Tie-Yan Liu, Yoshua Bengio.
   - Regeneration Learning: A Learning Paradigm for Data Generation. [[ArXiv'2023](https://arxiv.org/abs/2301.08846)]

<p align="right">(<a href="#top">back to top</a>)</p>

## Survey

* Chaoning Zhang, Chenshuang Zhang, Junha Song, John Seon Keun Yi, Kang Zhang, In So Kweon.
   - A Survey on Masked Autoencoder for Self-supervised Learning in Vision and Beyond. [[ArXiv'2022](https://arxiv.org/abs/2208.00173)]

<p align="right">(<a href="#top">back to top</a>)</p>

## Contribution

Feel free to send [pull requests](https://github.com/Lupin1998/Awesome-MIM/pulls) to add more links with the following Markdown format. Note that the Abbreviation, the code link, and the figure link are optional attributes.

```markdown
* **Abbreviation**: Author List.
  - Paper Name. [[Conference'Year](link)] [[code](link)]
  <p align="center"><img width="90%" src="link_to_image" /></p>
```

Current contributors include: Siyuan Li ([@Lupin1998](https://github.com/Lupin1998)), Daisuke Niizumi ([@daisukelab](https://github.com/daisukelab)). We thank all contributors for `Awesome-MIM`!

<p align="right">(<a href="#top">back to top</a>)</p>

## Related Project

### Paper List of Masked Image Modeling

- [Awesome-Masked-Autoencoders](https://github.com/EdisonLeeeee/Awesome-Masked-Autoencoders): A collection of literature after or concurrent with Masked Autoencoder (MAE).
- [awesome-MIM](https://github.com/ucasligang/awesome-MIM): Reading list for research topics in Masked Image Modeling.
- [Awesome-MIM](https://github.com/Westlake-AI/openmixup/blob/main/docs/en/awesome_selfsup/MIM.md): Awesome list of masked image modeling methods for self-supervised visual representation.
- [awesome-self-supervised-learning](https://github.com/jason718/awesome-self-supervised-learning): A curated list of awesome self-supervised methods.

### Project of Self-supervised Learning

- [OpenMixup](https://github.com/Westlake-AI/openmixup): CAIRI Supervised, Semi- and Self-Supervised Visual Representation Learning Toolbox and Benchmark.
- [MMPretrain](https://github.com/open-mmlab/mmpretrain): OpenMMLab self-supervised pre-training toolbox and benchmark.
- [solo-learn](https://github.com/vturrisi/solo-learn): A library of self-supervised methods for visual representation learning powered by Pytorch Lightning.
- [unilm](https://github.com/microsoft/unilm): Large-scale Self-supervised Pre-training Across Tasks, Languages, and Modalities.
- [VISSL](https://github.com/facebookresearch/vissl): FAIR's library of extensible, modular and scalable components for SOTA Self-Supervised Learning with images. 
