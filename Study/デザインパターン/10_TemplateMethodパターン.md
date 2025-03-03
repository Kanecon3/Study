# Template Method パターン

Template Method パターンは、似たような流れの処理を共通化したい時によく使用されます。  

1. スーパークラス（親クラス／抽象クラス）で共通の処理を実装します。個別処理は抽象メソッドなどを用意しておきます。
2. サブクラス（子クラス／具象クラス）にて個別処理を実装します。  

## メリット

共通処理がスーパークラスにまとまっているので、サブクラスごとに同じ処理を書かなくて済みます。  

## デメリット

サブクラスの処理を実装する際にスーパークラスの実装内容を知っている必要があります。  

## 注意事項
同じスーパークラスを継承しているサブクラスは、クライアントからは同じような動作をしているようにみえなければなりません。  

<参考>  
リスコフの置換原則: サブタイプのオブジェクトはスーパータイプのオブジェクトの仕様に従わなければならない、という原則  

## 実装例

```CSharp
// Template Methodパターンの継承のサンプル(C#)

using System;

namespace TemplateMethod_Inheritance
{
	// スーパークラス
	public abstract class AbstractTemplateMethodBaseClass
	{
		// 下記のメソッドはサブクラスで実装しなければならない
		public abstract void Start();
		public abstract int Calc();
	}

	// サブクラス1
	public class SubClass1 : AbstractTemplateMethodBaseClass
	{
		// スーパークラスの抽象メソッドを実装
		public override void Start()
		{
			Console.WriteLine("SubClass1");
		}

		// スーパークラスの抽象メソッドを実装
		public override int Calc()
		{
			return 1;
		}
	}

	// サブクラス2
	public class SubClass2 : AbstractTemplateMethodBaseClass
	{
		// スーパークラスの抽象メソッドを実装
		public override void Start()
		{
			Console.WriteLine("SubClass2");
		}

		// スーパークラスの抽象メソッドを実装
		public override int Calc()
		{
			return 2;
		}
	}

	// メインプログラム
	class Program
	{
		static void Main(string[] args)
		{
			int ans1 = Calculation(new SubClass1());
			Console.WriteLine(ans1);

			int ans2 = Calculation(new SubClass2());
			Console.WriteLine(ans2);

#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}

		// 抽象化されたクラスのインスタンスを処理する関数
		public static int Calculation(AbstractTemplateMethodBaseClass instance)
		{
			instance.Start();
			int ans = instance.Calc();
			return ans;
		}
	}
}
```
