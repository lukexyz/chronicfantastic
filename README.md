
## Setup develoment environment with `nbdev`

* Ubuntu / WSL
```
git clone https://github.com/lukexyz/chronicfantastic.git  
conda create -n chronicfantastic python=3.9 jupyter twine
conda activate chronicfantastic  
pip install nbdev
pip install -r requirements.txt  
```
  
  
* Install githooks from project folder  
```
nbdev_install_git_hooks
```

### Nbdev commands  

#### 1. 🏗️ **Build lib** from notebooks  
> `nbdev_build_lib` 


#### 2. 📝 **Build docs** from notebooks  
> `nbdev_build_docs` 
