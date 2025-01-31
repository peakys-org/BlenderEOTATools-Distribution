# Blender EOTA Tools
## インストール
1. https://github.com/peakys-org/BlenderEOTATools-Distribution/releases/ から、最新のリリースの ZIP ファイルをダウンロードします。
2. Blender を起動して、トップバーの編集[Edit] >  プリファレンス...[Preferences…] から、Preference ウィンドウを開き、アドオン[Add-ons] に進みます。
3. ウィンドウの右上の下矢印のメニューから、ディスクからインストール[Install from Disk...] に進み、ダウンロードした ZIP ファイルを選択します。
4. インストール後、一度 Blender を終了します。
![Image](https://github.com/user-attachments/assets/b3ef59cf-718b-4789-8b2a-24d2b850a32b)

## 全体像
EOTA Tools は 3D ビューポート[3D Viewport] のタブとして現れます。

![Image](https://github.com/user-attachments/assets/e7b61ac5-db5e-41c5-92f3-b21933e263cc)

## 各要素解説

### 操作
![Image](https://github.com/user-attachments/assets/75a62976-96d0-43c2-b7b8-e5dcb3c64b2a)

- カメラの位置に関する操作です。

### カメラ一覧
![Image](https://github.com/user-attachments/assets/e3427057-935d-4450-a427-f5b6e96181d7)

- 「カメラからの視野」は、3D ビューポート[3D Viewport] の右側にあるカメラビューを切り替えます[Toggle the camera view] ボタンと等価です。
- リストは、シーンオブジェクトのカメラの一覧(`[obj for obj in context.scene.objects if obj.type=='CAMERA']`)です。このリストからカメラを選択するとそのカメラは、シーンカメラ(`context.scene.camera`)になり、他のカメラは隠される。
  - マウスカーソルがパネル上にある状態で、次のショートカットが使えます。
    - Shift + Alt + w  または 上　 →　リストの上に移動
    - Shift + Alt + s  または 下　 →　リストの下に移動

### 解像度
![Image](https://github.com/user-attachments/assets/f4ea4cda-af88-45ae-b78c-232c7c9871ed)

- 基本となる解像度です。プリセットが用意されています。オーバースキャンが0のときに出力される画素数です。

### カメラへの設定
![Image](https://github.com/user-attachments/assets/bbcc2391-608e-434c-9669-9d1d6805593f)

#### 一段目
- オーバースキャン領域の割合を示します。面積比ではなく相似比です。
- 実際に出力される画素数です。

#### 二段目
- ラベルの通りです。

#### 三段目
- オーバースキャン枠に対する設定です。

### 出力
![Image](https://github.com/user-attachments/assets/154bb9af-86e6-4fa7-9f88-c3a51f389767)

- 「ファイル名」「カメラ名」は、出力先のファイル名にこれらを含ませます。

### 印字
![Image](https://github.com/user-attachments/assets/cabef2a5-9e85-486a-ae60-5c069bd0981b)

- 出力画像に情報を印字します。

### マニュアル
![Image](https://github.com/user-attachments/assets/951bdc06-3154-4640-b573-39037b00d308)

- このページを開きます。
