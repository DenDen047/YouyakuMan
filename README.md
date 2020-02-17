# YouyakuMan

 [![Unstable](https://poser.pugx.org/ali-irawan/xtra/v/unstable.svg)](*https://poser.pugx.org/ali-irawan/xtra/v/unstable.svg*)  [![License](https://poser.pugx.org/ali-irawan/xtra/license.svg)](*https://poser.pugx.org/ali-irawan/xtra/license.svg*)

### Introduction

This is an one-touch extractive summarization machine.

using BertSum as summatization model, extract top N important sentences.

![img](https://cdn-images-1.medium.com/max/800/1*NRamBWCtYuS8U6pqpnDiJQ.png)

---

### Prerequisites

#### General requirement

```
pip install torch
pip install transformers
pip install googletrans
```

#### Japanese specific requirement

- [BERT日本語Pretrainedモデル — KUROHASHI-KAWAHARA LAB](http://nlp.ist.i.kyoto-u.ac.jp/index.php?BERT日本語Pretrainedモデル)
    1. Download `Japanese_L-12_H-768_A-12_E-30_BPE.zip` or `Japanese_L-12_H-768_A-12_E-30_BPE_WWM.zip`
    2. Put the unzipped folder into /model/Japanese
    3. Adjust `src/config.ini` and `JapaneseWorker.bert_model` parameter

---

### Pretrained Model

English: [Here](https://drive.google.com/open?id=1wxf6zTTrhYGmUTVHVMxGpl_GLaZAC1ye)

Japanese: [Here](https://drive.google.com/open?id=10hJX1QBAHfJpErG2I8yhcAl2QB_q28Fi)

Download and put under directory `checkpoint/en` or `checkpoint/jp`

---

### Usage

```sh
$ ./run.sh
```

### Example

```
$ python youyakuman.py -txt_file YOUR_FILE -lang LANG -n 3 --super_long
```

#### Note

Since Bert only takes 512 length as inputs, this summarizer crop articles >512 length.

If --super_long option is used, summarizer automatically parse to numbers of 512 length inputs and summarize per inputs. Number of extraction might slightly altered with --super_long used.


### Train Example

```
$python youyakumanJPN_train.py -data_folder [training_txt_path] -save_path [model_saving_path] -train_from [pretrained_model_file]
```

---
### Version Log:

2020-02-10  Training part added

2019-11-14  Add multiple language support

2019-10-29 	Add auto parse function, available for long article as input

