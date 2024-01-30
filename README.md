1120212497 刘毅葳
# RhythmicHead
实现使用RhythmicHead进行训练

## 使用方法
### 环境依赖
```
absl-py==2.0.0
addict==2.4.0
aiosignal==1.3.1
appdirs==1.4.4
attrs==23.1.0
audioread==3.0.1
basicsr==1.3.4.7
cachetools==5.3.2
certifi==2020.12.5
cffi==1.16.0
charset-normalizer==3.3.2
click==8.1.7
cloudpickle==3.0.0
colorama==0.4.6
colorlog==6.7.0
contourpy==1.1.1
cycler==0.12.1
decorator==5.1.1
dlib==19.22.1
docker-pycreds==0.4.0
face-alignment==1.3.5
ffmpeg==1.4
filelock==3.13.1
fonttools==4.44.0
frozenlist==1.4.0
future==0.18.3
gitdb==4.0.11
GitPython==3.1.40
glob2==0.7
google-auth==2.23.4
google-auth-oauthlib==0.4.6
grpcio==1.59.2
hyperopt==0.2.5
idna==3.4
imageio==2.9.0
imageio-ffmpeg==0.4.5
importlib-metadata==6.8.0
importlib-resources==6.1.0
joblib==1.3.2
jsonschema==4.19.2
jsonschema-specifications==2023.7.1
kiwisolver==1.4.5
kornia==0.5.5
lazy_loader==0.3
librosa==0.10.1
llvmlite==0.37.0
lmdb==1.2.1
lws==1.2.7
Markdown==3.5.1
MarkupSafe==2.1.3
matplotlib==3.6.3
msgpack==1.0.7
networkx==3.1
numba==0.54.1
numpy==1.20.3
oauthlib==3.2.2
opencv-python==3.4.9.33
packaging==23.2
pandas==1.3.4
pathtools==0.1.2
Pillow==6.2.1
pkgutil_resolve_name==1.3.10
platformdirs==3.11.0
plotly==5.18.0
pooch==1.8.0
protobuf==4.25.0
psutil==5.9.6
pyasn1==0.5.0
pyasn1-modules==0.3.0
pycparser==2.21
pyparsing==3.1.1
python-dateutil==2.8.2
python-speech-features==0.6
python_abi== 3.8
pytorch-fid==0.3.0 
pytorch-msssim== 1.0.0
pytorch-fid==0.3.0
pytz==2023.3.post1
PyWavelets==1.4.1
PyYAML==5.3.1
ray==2.6.3
referencing==0.30.2
requests==2.31.0
requests-oauthlib==1.3.1
rpds-py==0.12.0
rsa==4.9
scikit-image==0.16.2
scikit-learn==1.3.2
scipy==1.5.0
sentry-sdk==1.34.0
setproctitle==1.3.3
six==1.16.0
smmap==5.0.1
soundfile==0.12.1
soxr==0.3.7
tabulate==0.9.0
tb-nightly==2.12.0a20230126
tenacity==8.2.3
tensorboard==2.7.0
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
texttable==1.7.0
thop==0.1.1.post2209072238
threadpoolctl==3.2.0
tomli==2.0.1
torch==1.13.1+cu116
torchaudio==0.13.1+cu116
torchvision==0.14.1+cu116
tqdm==4.66.1
trimesh==3.9.20
typing_extensions==4.8.0
tzdata==2023.3
urllib3==2.0.7
wandb==0.15.12
Werkzeug==3.0.1
yapf==0.40.2
zipp==3.17.0

```

需要使用[Flownet](https://drive.google.com/file/d/1hF8vS6YeHkx3j2pfCeQqqZGwA_PJq_Da/view)对voxcelab2的视频进行预处理
运行
```bash
python single_video_preprocess.py --extract_landmark --video_path=/dataset/vxl2
```

### 训练和评估
![Alt text](image-1.png)
运行
```bash
python run_talkingface.py --model=RhythmicHead --dataset=vxl2 
```




