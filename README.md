# CUP-HebCUP-combined-Approach

## Training and Running CUP and HebCUP
### CUP
#### Preparing the Environment for Running CUP 
- In order to train CUP on an RIT CS machine, we need to prepare the coda environment, setup nlg-eval, and setup JAVA 8 for evaluating the model 
- Conda Environment and setup NLG Eval
```bash
cd CUP
conda env create -f environment.yml

pip install git+https://github.com/Maluuba/nlg-eval.git@master
# set the data_path
nlg-eval --setup ${any_data_path}
```
- For setting up JAVA 8 on CS machines, we used sdkman
```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install java 8.0.2-zulu
```
#### Training CUP
```bash
cd CUP/scripts
# 0 for GPU 0
./train_model.sh 0 CoAttnBPBAUpdater models.updater.CoAttnBPBAUpdater ${CUP_DATASET}
```
#### Evalulating CUP 

```bash
cd CUP/scripts
# 0 for GPU 0
./infer_eval.sh 0 CoAttnBPBAUpdater models.updater.CoAttnBPBAUpdater ${CUP_DATASET}
```



### HebCUP
#### Evaluating HebCup
```bash
cd HebCUP/source
python HebCup.py --dataPath ${HebCUP_DATASET}
 ```

Here The dataset path `${CUP_DATASET}` and the `${HebCUP_DATASET` should be set to the path where the respective preprocessed data is located
## PreProcessing the Dataset:
### (1) After cloning the repository to your desired location, go to Data/Jasonl-RAW-data and extract the HebCUP_clean_dataset.zip file
### (2) run all the python scripts in Python-Scripts/RAW-Jasonl-To-CSV-script directory, to convert the given dataset from Jasonl files to csv files.
```
python training.py
python testing.py
python validating.py

```
### (3) run all the python scripts in Python-Scripts/CSV-file-labeling-script directory, to create new csv files where each row is labelled for CUP or HebCUP. 
```
python train_label.py
python test_label.py
python valid_label.py

```
### (4) run all the python scripts in Python-Scripts/Create-CUP-Jasonl-data directory, to create new Jasonl files for CUP. 
```
python filtering_CUP_train.py
python filtering_CUP_test.py
python filtering_CUP_valid.py

```
### (5) run all the python scripts in Python-Scripts/Create-HebCUP-Jasonl-data directory, to create new Jasonl files for HebCUP. 
```
python filtering_HebCUP_train.py
python filtering_HebCUP_test.py
python filtering_HebCUP_valid.py

```

The Dataset and the trained mode can be found [here](https://drive.google.com/drive/folders/1yMueleu4cEmlf8qohp2e2lS5HMo0mqEn?usp=sharing)

### References
```
@inproceedings{liu2020automating,
  title={Automating Just-In-Time Comment Updating},
  author={Liu, Zhongxin and Xia, Xin and Yan, Meng and Li, Shanping},
  booktitle={Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering},
  pages={713--725},
  year={2020}
}

```