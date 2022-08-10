
# `DanceVision` 
🔴 `DanceVision` live-streaming platform.

![image](https://github.com/lukexyz/chronicfantastic/blob/master/media/splash_title_1.jpg?raw=true)
💪😬💪 💪😙💪 💪🤪💪
</br>  

> VDO.ninja and AlphaPose for seamless interactive live-streamed rooms.

<p align="center">
  <img src="https://github.com/lukexyz/chronicfantastic/blob/master/media/instructions_1.jpg?raw=true">
</p>


## Setup develoment environment with `nbdev`

* Ubuntu / WSL
```
git clone https://github.com/lukexyz/chronicfantastic.git  
conda create -n chronic python=3.9 jupyter
conda activate chronic
pip install nbdev
pip install -r requirements.txt  
```
  
  
* Install githooks from project folder  
```
nbdev_install_git_hooks
```

### Nbdev commands  

#### 1. 🏗️ **Build lib** from notebooks  
> `nbdev_prepare` 


#### 2. 📝 **Build docs** from notebooks (WSL) 
> `nbdev_docs` 

### 🏗️ `nbdev_prepare`

command bundles the following

1.  🏗️ nbdev_export: Builds the .py modules and library from the jupyter
    notebook
2.  🛠️ nbdev_test: Tests all your notebooks
3.  🚿 nbdev_clean: Cleans your notebooks to get rid of extreanous
    output for Github

📝 To build docs from notebooks (including README.md from `index.ipynb`)

> nbdev_docs