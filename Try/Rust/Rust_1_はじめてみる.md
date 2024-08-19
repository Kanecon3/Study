# 概要

世の中で徐々に C/C++ から Rust への移行が始まっているので、Rust を試してみようと思い、環境構築から試してみました。  

同じような記事はネットで沢山あがっていますが、当然ながら古い記事もあり、少しハマりました・・・。  
この記事の内容は 2024/08/15 に試しています。  

# 環境

OS: Windows 10  
Rust: 1.80.1  

# インストール

参考にしたサイト：  
https://www.rust-lang.org/tools/install  
https://qiita.com/rfukudome/items/76fd9251f4885de69edd  


## C++ のビルドツールをインストール

C++ のビルドツール（コンパイラ）が必要  
→自分の環境にはすでにインストールされているので割愛させていただきました。参考にしたサイトなどでご確認ください。  

## Rustのインストール

1. インストーラーをダウンロード
2. インストーラーを起動（ダブルクリック）
3. 選択肢が出るので、デフォルトを選択（そのままリターン）
4. PATH を通す  
  `C:\Users\【ユーザーフォルダ】\.cargo\bin` にPATHを通す（ユーザー環境変数の Path に追加する）

なお、デフォルトでインストールをすると `C:\Users\【ユーザーフォルダ】\.cargo` にインストールされるようです。  

## 動作チェック

1. PowerShell を起動
2. `rustc --version` を実行
3. Rust のバージョンが表示されていればインストール成功

```
PS > rustc --version

rustc 1.80.1 (3f5fd8dd4 2024-08-06)
```

# まずは「Hello World」

1. 適当にフォルダを作成
2. 作成したフォルダ内に `hello.rs` ファイルを作成
3. hello.cs ファイルを VS Code などで編集
```
fn main()
{
	println!("Hello world!!")
}
```
4. PowerShell を起動
5. 1. で作成したフォルダに移動
6. コンパイル
```
PS > rustc hello.rs
```
  エラーの場合は error が表示されます

7. 実行 
```
PS > .\hello.exe

Hello world!!
```

ここまで出来れば、とりあえず Rust のコードを書いて試すことはできます。  
ここから下は、ドキュメントだったり、ちょっとした応用編となります。  

---

## ドキュメント

公式：  
https://doc.rust-lang.org/book/  

日本語訳（注：コミュニティによる日本語訳なので、バージョンが少し古い）：  
https://doc.rust-jp.rs/book-ja/title-page.html  

## コーディングスタイル

公式：  
https://doc.rust-lang.org/nightly/style-guide/  

### フォーマッタ

フォーマッタが公式からリリースされている  
https://doc.rust-jp.rs/book-ja/appendix-04-useful-development-tools.html#rustfmt%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E8%87%AA%E5%8B%95%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88  

インストール：  
```
PS > rustup component add rustfmt

info: component 'rustfmt' for target 'x86_64-pc-windows-msvc' is up to date
```
注：メッセージは環境によって違うはずです  

実行：  
```
PS > rustfmt hello.rs
```
成功していれば、対象のソースコード（hello.cs）がフォーマットされているはず  

# Rust 入門

下記のサイトなどをみてやってみようかなと  
https://zenn.dev/mebiusbox/books/22d4c1ed9b0003  

自分メモ：  
- Rust は標準でオブジェクトを不変（Immutable）で束縛する
- Rust は、ほとんどが式
- セミコロンは、式を文に変化させるもの

# Rustのプロジェクトを作成する

1. 適当なフォルダで下記のコマンドを実行
```
PS > cargo new 【プロジェクト名】
```

# VS Code 拡張機能

## rust-analyzer

公式からリリースされている：  
https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer  

注：使用する時は、プロジェクト作成時に生成される Cargo.toml ファイルが必要になるので、プロジェクトを作成した方が良いです。  

エラーの時は左下の rust-analyzer の箇所が赤く表示されます  

# VS Code の設定

setting.json 等に書く
```
{
	"[rust]": {
		"editor.formatOnSave": true
	}
}
```
- ファイルセーブ時のオートフォーマットを有効



