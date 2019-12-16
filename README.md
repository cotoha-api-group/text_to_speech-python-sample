COTOHA 音声合成API サンプルコード(Python)
====
一括音声合成APIを利用して、合成音声を保存したwavファイルを生成するPythonコードです。

# Usage
1. `sample_py.py`の8,9行目の`input client id here`及び`input client secret here`と書かれている部分にCOTOHA API Portalアカウントページで表示される`client id`及び`client secret`をそれぞれ入力してください。
1. `/sample_json`内のjsonファイルを参考にして、作成したい合成音声の設定を記載したjsonファイルを作成してください。以後、このjsonファイルを`[your_tts_json]`と表記します。
1. コマンド`python3 sample_py.py [your_tts_json]`を実行してください。実行したディレクトリに、合成音声が保存された`output.wav`が生成されます。
また、コマンド`python3 sample_py.py [your_tts_json] [output_wav_name]`を実行すると、合成音声が`[output_wav_name]`で指定したファイル名で保存されます。

**出力例**
以下のように出力されれば、音声の生成が成功しています。
```
$ python3 sample_py.py sample_json/simple.json test.wav
getToken completed successfully.
inputFromFile completed successfully.
post data: {'text': '今日の天気は晴れです。', 'speakerId': 'ja_JP-F-S0005-T002-E01-SR0'}
postAndRecieve completed successfully.
outputToFile completed successfully.
test.wav has been generated.
```

# Requirements
動作確認を行ったバージョンとなります。
- Python 3.x
- urllib