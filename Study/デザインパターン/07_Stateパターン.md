# State パターン
状態ごとのふるまい（処理）を変えやすくするパターンです。  

“State” = 状態  

「状態」に応じて様々な振る舞いが変わるような場合は、このStateパターンを用いると上手くいくでしょう。  

## 実装例

Stateごとに有効なボタンが変わるプログラムの例:

```CSharp
// Stateパターンのサンプル(C#)

using System;
using System.Collections.Generic;

namespace State
{
	public class StateSample
	{
		// Stateパターン用のインターフェース
		interface IStateButton
		{
			bool PushButtonA();
			bool PushButtonB();
			bool PushButtonX();
			bool PushButtonY();
		}

		// 具象クラス
		public class ButtonState1 : IStateButton
		{
			public bool PushButtonA() { return true; }	// 有効
			public bool PushButtonB() { return false; }
			public bool PushButtonX() { return false; }
			public bool PushButtonY() { return false; }
		}

		// 具象クラス
		public class ButtonState2 : IStateButton
		{
			public bool PushButtonA() { return false; }
			public bool PushButtonB() { return false; }
			public bool PushButtonX() { return true; }	// 有効
			public bool PushButtonY() { return true; }	// 有効
		}

		// 具象クラス
		public class ButtonState3 : IStateButton
		{
			public bool PushButtonA() { return true; }	// 有効
			public bool PushButtonB() { return true; }	// 有効
			public bool PushButtonX() { return true; }	// 有効
			public bool PushButtonY() { return true; }	// 有効
		}

		// ボタンが押されたかの監視処理
		public void CheckButton()
		{
			Console.WriteLine("Push Key: a/b/x/y");
			ConsoleKeyInfo keyInfo = Console.ReadKey();
			Console.WriteLine("");
			char keyChar = keyInfo.KeyChar;
			switch (keyChar) {
				case 'a': {
					if (m_button.PushButtonA()) {
						ChangeState();
					}
					break;
				}
				case 'b': {
					if (m_button.PushButtonB()) {
						ChangeState();
					}
					break;
				}
				case 'x': {
					if (m_button.PushButtonX()) {
						ChangeState();
					}
					break;
				}
				case 'y': {
					if (m_button.PushButtonY()) {
						ChangeState();
					}
					break;
				}
				default: {
					break;
				}
			}
		}

		// ステート変更処理
		private void ChangeState()
		{
			m_state += 1;
			if (m_state > 3) { m_state = 1; }
			Console.WriteLine($"Change State = {m_state}");

			switch (m_state) {
				case 1: {
					m_button = new ButtonState1();	// Stateごとの処理を入れ替え
					break;
				}
				case 2: {
					m_button = new ButtonState2();	// Stateごとの処理を入れ替え
					break;
				}
				case 3: {
					m_button = new ButtonState3();	// Stateごとの処理を入れ替え
					break;
				}
			}
		}

		// メンバ変数
		private IStateButton m_button = new ButtonState1();
		private int m_state = 1;
	}

	class Program
	{
		//// メインプログラム /////
		static void Main(string[] args)
		{
			var sample = new StateSample();
			while(true) {
				sample.CheckButton();
			}

#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}
	}
}
```
