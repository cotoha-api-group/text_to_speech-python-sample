#coding:utf-8

import sys
import json
import urllib.request

# 認証情報定義
clientId = 'input client id here'
clientSecret = 'input client secret here'

# 接続先定義
oauthUrl = 'https://api.ce-cotoha.com/v1/oauth/accesstokens'
ttsUrl = 'https://api.ce-cotoha.com/api/tts/v1/tts'

# main の処理
# コマンドライン引数1 : 音声合成設定を記入したjsonファイル
# コマンドライン引数2(option) : 出力wavファイル名
# 出力 : 合成音声wavファイル
def main():
    accessToken = getToken(oauthUrl, clientId, clientSecret)
    argv = sys.argv
    if len(argv) <= 1:
        print('usage: python sample_py [input_json_file] [(option)output_wav_file]')
        exit(1)
    inputFilePath = argv[1]
    if len(argv) > 2:
        outputFilePath = argv[2]
    else:
        outputFilePath = 'output.wav'
    postData = inputFromFile(inputFilePath)
    audioData = postAndRecieve(ttsUrl, accessToken, postData)
    outputToFile(audioData,outputFilePath)

# アクセストークン取得
def getToken(postUrl, cId, cSecret):
    data = {}
    data['grantType'] = 'client_credentials'
    data['clientId'] = cId
    data['clientSecret'] = cSecret
    jsonData = json.dumps(data).encode('utf-8')
    
    http = urllib.request.Request(postUrl)
    http.add_header('Content-Type', 'application/json; charset=UTF-8')
    http.add_header('Content-Length', len(jsonData))

    try:
        with urllib.request.urlopen(http, jsonData) as response:
            responseData = response.read()
            responseJson = json.loads(responseData.decode('utf-8'))
            print('getToken completed successfully.')
            return responseJson['access_token']
    except urllib.error.HTTPError as err:
        errData = err.read()
        errJson = json.loads(errData.decode('utf-8'))
        print('[ERROR!(@getToken)] status: ' + str(errJson['status']) + ', message: ' + errJson['message'])
        exit(1)

# JSON ファイルの読み込み
def inputFromFile(inputFilePath):
    jsonFile = open(inputFilePath, 'r',encoding='utf-8')
    jsonData = json.load(jsonFile)
    print('inputFromFile completed successfully.')
    print('post data: ' + str(jsonData))
    return json.dumps(jsonData).encode('utf-8')

# データをポストし合成音声を取得
def postAndRecieve(postUrl, token, postData):
    http = urllib.request.Request(postUrl)
    http.add_header('Authorization', 'Bearer '+token)
    http.add_header('Accept', 'Audio/wav')
    http.add_header('Content-Length', len(postData))
    http.add_header('Content-Type', 'application/json; charset=UTF-8')

    try:
        with urllib.request.urlopen(http, postData) as response:
            responseData = response.read()
            print('postAndRecieve completed successfully.')
            return responseData
    except urllib.error.HTTPError as err:
        errData = err.read()
        errJson = json.loads(errData.decode('utf-8'))
        print('[ERROR!(@post_and_recieve)] status: ' + str(err.code) + ', code: ' + errJson['code'] + ', detail: ' + errJson['detail'])
        exit(1)

# 音声ファイルを出力
def outputToFile(data, outputFilePath):
    outputFile = open(outputFilePath, 'wb')
    outputFile.write(data)
    outputFile.close
    print('outputToFile completed successfully.')
    print(outputFilePath + ' has been generated.')

main()