# Strategy パターン

アプリケーションで使用されるアルゴリズムを動的に切り替える必要がある際に有用なパターンです。  

## 実装例

```CSharp
// Strategyパターンのサンプル(C#)

using System;

namespace Strategy
{
	class StrategySample
	{
		// デリゲート
		public delegate float DelegateStrategy(int en);

		// ストラテジークラスA
		public class StrategyA
		{
			public float Execute(int en)
			{
				return (float)en * 1.08f;
			}
		}

		// ストラテジークラスB
		public class StrategyB
		{
			public float Execute(int en)
			{
				return (float)en * 1.10f;
			}
		}

		// 
		public class Context
		{
			private DelegateStrategy m_delegateStrategy;

			// コンストラクタ
			public Context(DelegateStrategy delegateStrategy)
			{
				m_delegateStrategy = delegateStrategy;
			}

			public float Execute(int en)
			{
				return m_delegateStrategy(en);
			}
		}
	}

	class Program
	{
		///// メインプログラム /////
		static void Main(string[] args)
		{
			StrategySample.Context context;

			// StrategyA
			context = new StrategySample.Context(new StrategySample.StrategyA().Execute);
			Console.WriteLine("StrategyA:Execute = {0}", context.Execute(100));

			// StrategyBに切り替え
			context = new StrategySample.Context(new StrategySample.StrategyB().Execute);
			Console.WriteLine("StrategyB:Execute = {0}", context.Execute(100));

#if true    // テスト専用のコード
			Console.ReadKey();
#endif
		}
	}
}
```
