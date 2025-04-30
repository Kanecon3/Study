# Abstract Factory パターン

Factory Method パターンのFactory部分も抽象化した感じ？  

## 実装例

```CSharp
// Abstract Factoryパターンのサンプル(C#)

using System;

namespace AbstractFactory
{
	///// 抽象クラス /////

	// 生成されるクラスの抽象クラス（タイヤ）
	public abstract class PartsTire
	{
		public abstract void ToCheck();
	}

	// 生成されるクラスの抽象クラス（ボディ）
	public abstract class PartsBody
	{
		public abstract void ToCheck();
	}

	// Factoryの抽象クラス（工場）
	public abstract class FactoryBase
	{
		public abstract PartsTire CreateTire();
		public abstract PartsBody CreateBody();
	}	


	///// 具象クラス /////

	// 生成される具象クラス（タイヤA）
	public class TireA : PartsTire
	{
		public override void ToCheck()
		{
			Console.WriteLine("TireA");
		}
	}

	// 生成される具象クラス（タイヤB）
	public class TireB : PartsTire
	{
		public override void ToCheck()
		{
			Console.WriteLine("TireB");
		}
	}

	// 生成される具象クラス（ボディA）
	public class BodyA : PartsBody
	{
		public override void ToCheck()
		{
			Console.WriteLine("BodyA");
		}
	}

	// 生成される具象クラス（ボディB）
	public class BodyB : PartsBody
	{
		public override void ToCheck()
		{
			Console.WriteLine("BodyB");
		}
	}

	// Factoryの具象クラス（工場X）
	public class FactoryX : FactoryBase
	{
		public override PartsTire CreateTire()
		{
			return new TireA();
		}

		public override PartsBody CreateBody()
		{
			return new BodyA();
		}

	}

	// Factoryの具象クラス（工場Y）
	public class FactoryY : FactoryBase
	{
		public override PartsTire CreateTire()
		{
			return new TireB();
		}

		public override PartsBody CreateBody()
		{
			return new BodyB();
		}

	}


	//// メインプログラム /////
	class Program
	{
		static void Main(string[] args)
		{
			int factoryType = 0;
			int partsType = 1;
			RequestGenerateParts(factoryType, partsType);

#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}

		static void RequestGenerateParts(int factoryType, int partsType)
		{
			FactoryBase factory;

			if (factoryType == 0) {
				factory = new FactoryX();
			} else {
				factory = new FactoryY();
			}

			if (partsType == 0) {
				PartsTire tire = factory.CreateTire();
				tire.ToCheck();
			} else {
				PartsBody body = factory.CreateBody();
				body.ToCheck();
			}
		}
	}
}
```

メモ  
ProtoType パターンを使って実装する方法もあるらしいよ？  
