# dog-spotter-ai-console-3

🦮🦮🦮 コンソール上で動作するトイプードル・ポメラニアン・ボーダーコリーの犬種を識別するAI！  

## 実行方法

DevContainerに入り、以下のコマンドを実行します。  

```bash
python ./predict.py
```

`Please provide an image URL: `と表示されたら、画像のURLを入力します。  

第一引数に画像のURLを指定して実行することもできます。  

```bash
python ./predict.py "https://example.com/image.jpeg"
```

---

モデルの生成は、`./main.ipynb`を実行してください。  
トレーニングには、Google Colabを使用しています。  

## 参考文献

- [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/)
