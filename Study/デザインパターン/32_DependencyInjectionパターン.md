# Dependency Injection パターン

※Null Object パターンはGoFのデザインパターンではありません。

日本語に訳すと「依存性の注入」となります。  
Dependency Injection の頭文字を取って「DI」と略されることが多いです。  

Dependency Injection パターンはSOLID原則の依存性逆転の解決法として出てくると思われますので、しっかり覚えておきましょう。  

## メリット

テスト（単体テスト）がやりやすくなります。

## デメリット

テストを書かない場合、単にコードが冗長になってしまうだけの実装になってしまいます。  

## 実装例

Dependency Injection パターンを使用していない例です。この例では、ClassAがClassBに依存しているため、ClassAの単体テストがやりづらくなっています。  

```CSharp
// Dependency Injectionパターンのサンプル(C#)

using System;

namespace DependencyInjection
{
	class Program
	{
		static void Main(string[] args)
		{
			var insA = new ClassA();
			bool flg = insA.IsWeatherSunny();

#if true    // テスト専用のコード
			Console.ReadKey();
#endif
		}
	}

	// ClassAの定義
	public class ClassA
	{
		private ClassB m_clsB;

		public ClassA()
		{
			m_clsB = new ClassB();	// ClassAがClassBに依存している状態
		}

		public bool IsWeatherSunny()
		{
			// GetWeatherメソッドの返す値が状態によって変動してしまうため
			// ClassAは単体テストがやりづらくなる
			string weather = m_clsB.GetWeather();

			if (weather == "晴れ") {
				return true;
			}

			return false;
		}
	}

	// ClassBの定義
	public class ClassB
	{
		public string GetWeather()
		{
			// 天気を取ってくるシステムがあると仮定します。
			// 今はそのシステムがないのでランダムで返しています。
			string weather = "";
			var rnd = new Random();
			int result = rnd.Next(0, 2);

			if (result == 0) {
				weather = "晴れ";
			} else if (result == 1) {
				weather = "曇り";
			} else {
				weather = "雨";
			}

			return weather;
		}
	}
}
```

Dependency Injection パターンを使用する実装例  

```CSharp
// Dependency Injectionパターンのサンプル(C#)

using System;

namespace DependencyInjection
{
	class Program
	{
		static void Main(string[] args)
		{
			var insB = new DIClassB();
			var insA = new DIClassA(insB);	// 依存性の注入
			bool flg = insA.IsWeatherSunny();

#if true    // テスト専用のコード
			Console.ReadKey();
#endif
		}
	}

	// インターフェースの定義
	interface IDIClass
	{
		string GetWeather();
	}

	// DIClassAの定義
	class DIClassA
	{
		private IDIClass m_ins;

		// コンストラクタで渡す
		public DIClassA(IDIClass ins)
		{
			if (ins == null) {
				throw new ArgumentNullException("ins is null");
			}

			m_ins = ins;
		}

		public bool IsWeatherSunny()
		{
			string weather = m_ins.GetWeather();

			if (weather == "晴れ") {
				return true;
			}

			return false;
		}
	}

	// DIClassBの定義。インターフェースを継承している
	public class DIClassB : IDIClass
	{
		public string GetWeather()
		{
			// 天気を取ってくるシステムがあると仮定します。
			// 今はそのシステムがないのでランダムで返しています。
			string weather = "";
			var rnd = new Random();
			int result = rnd.Next(0, 2);

			if (result == 0) {
				weather = "晴れ";
			} else if (result == 1) {
				weather = "曇り";
			} else {
				weather = "雨";
			}

			return weather;
		}
	}
}
```

なお、このままだとメリットがありません。テストコードを書いてみます。  
（下記はテストコードだとしてください）

```CSharp
namespace DependencyInjection
{
	class Program
	{
		static void Main(string[] args)
		{
			// 単体テストだとして
			var insB = new MocClassB();		// Mockを生成
			var insA = new DIClassA(insB);	// 依存性の注入
			bool flg = insA.IsWeatherSunny();
			Debug.Assert(flg);	// 必ずtrueが返ってくるテスト

#if true    // テスト専用のコード
			Console.ReadKey();
#endif
		}
	}

	// DIClassAの単体テスト用のMock
	class MocClassB : IDIClass
	{
		public string GetWeather()
		{
			return "晴れ";
		}
	}
}
```

MocClassBは必ず”晴れ”を返すのでDIClassAのテストがやりやすくなります。  

## 補足

new でインスタンスを直接生成するのではなく、Factory経由で生成するのが定石っぽいですね。  
