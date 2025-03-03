# Singleton パターン：デザインパターン

Singleton パターンはよく使用されるデザインパターンです。  
このデザインパターンは便利な使い方も出来てしまうので、むやみに乱用してまうとデメリットを生み出してしまいます。使用法に気を付けなければなりません。  

## Singleton パターン

### メリット

あるクラスに対してインスタンスが1つしか存在しないことを保証する  
＝インスタンスが1つしか存在しないことが重要な場合がある（複数生成されたらバグの元になるとか）

### デメリット

グローバルにどこからでもアクセス出来てしまう（結局グローバル変数になってしまう）ので、多用すると依存関係を複雑にさせてしまう  
- **単体テストなどがやりづらくなる**
- 依存関係逆転の原則に反してしまう

## 実装例

実装例1. GetInstanceメソッドを呼んだタイミングで、インスタンスを生成する例:

```CSharp
// Singletonパターンのサンプル(C#)

using System;

namespace Singleton
{
	// シングルトンで実装したクラス
	public class SingletonPatternClass
	{
		static SingletonPatternClass m_instance = null;

		// SingletonPatternClassクラスのコンストラクタ
		private SingletonPatternClass()
		{
			// NOTE：
			//  コンストラクタは一度しか呼ばれないはず
			//  2回呼ばれていたらNG
			Console.WriteLine("constructor SingletonPatternClass");
		}

		// インスタンスを取得するためのメソッド
		// NOTE：このメソッドを初めて呼んだタイミングでSingletonPatternClassのインスタンスが一度だけ生成される
		public static SingletonPatternClass GetInstance()
		{
			if (m_instance == null) {
				m_instance = new SingletonPatternClass();
			}

			return m_instance;
		}
	}

	// メインプログラム
	class Program
	{
		static void Main(string[] args)
		{
			// 初回呼び出し
			SingletonPatternClass instance = SingletonPatternClass.GetInstance();

			// 2回目の呼び出し（NOTE：この呼び出しではSingletonPatternClassのインスタンスは生成されない）
			SingletonPatternClass instance2 = SingletonPatternClass.GetInstance();

#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}
	}
}
```

実装例2. GetInstanceメソッドでnullチェックしてインスタンスを生成する処理を省く例:

```CSharp
// Singletonパターンのサンプル(C#)

using System;

namespace Singleton
{
	// シングルトンで実装したクラス
	public class SingletonPatternClass
	{
		// GetInstanceメソッドでnullチェックを回避するためのインナークラス
		private class SingletonPatternClassHolder
		{
			public static SingletonPatternClass Instance { get; private set; } = new SingletonPatternClass();
		}

		// SingletonPatternClassクラスのコンストラクタ
		private SingletonPatternClass()
		{
			// NOTE：
			//  コンストラクタは一度しか呼ばれないはず
			//  2回呼ばれていたらNG
			Console.WriteLine("constructor SingletonPatternClass");
		}

		// インスタンスを取得するためのメソッド
		// NOTE：このメソッドを初めて呼んだタイミングでSingletonPatternClassのインスタンスが一度だけ生成される
		public static SingletonPatternClass GetInstance()
		{
			return SingletonPatternClassHolder.Instance;
		}
	}

	// メインプログラム
	class Program
	{
		static void Main(string[] args)
		{
			// 初回呼び出し
			SingletonPatternClass instance = SingletonPatternClass.GetInstance();

			// 2回目の呼び出し（NOTE：この呼び出しではSingletonPatternClassのインスタンスは生成されない）
			SingletonPatternClass instance2 = SingletonPatternClass.GetInstance();


#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}
	}
}
```

なお、上記2つのパターンともに下記の処理が必要な場合には、追加の処理の実装が必要になります。  
- スレッドセーフ
- インスタンスを削除（delete）したい
