# Adapter パターン：デザインパターン

コンセントは各国で違う規格があるが、変換アダプターを間に挟むことで使うことができるようになります。  
Adapter パターンは、このイメージに近いパターンです。  

“Adapter”の言葉の意味　「適合させるもの」  

あるクラスのインターフェース（規格）を、クライアントが求める他のインターフェースに変換するパターンです。  

## メリット
Adapter パターンを用いると、提供済みの既存のクラスに対して修正を加えることなく、インタフェースを変更することができます。  
（提供済みの既存のクラス ＝ 過去にリリース済みの実績のあるクラス／コードや外部から提供されたDLLなど）  

## 注意事項

Adapter役のクラスと提供済みの既存のクラスの機能がかけ離れている場合は、Adapterパターンで実装してはいけません。  

## 実装例

実装例1. 委譲の例  

委譲を利用したAdapterは、利用したいクラスのインスタンスを生成し、そのインスタンスをAdapterクラス内で利用することで実現されます。  

```CShrap
// Adapterパターンの委譲のサンプル(C#)

using System;

namespace AdapterPattern_Delegation
{
	// このクラスは既にリリース済みで変更できないとする
	public class OldDataClass
	{
		// 昔の仕様では数値で返す
		public int GetGameNumber()
		{
			return 1;
		}
	}

	// インターフェース
	public interface IAdapterClass
	{
		string GameNumber();
	}

	// Adapter
	class AdapterDataClass : IAdapterClass
	{
		private OldDataClass m_oldData = new OldDataClass();	// 利用したいクラスのインスタンスを生成

		public string GameNumber()
		{
			int no = m_oldData.GetGameNumber();
			return no.ToString();
		}
	}

	// メインプログラム
	class Program
	{
		static void Main(string[] args)
		{
			string no;	// 現在の仕様では結果を文字列で欲しいとする

			var dataIns = new AdapterDataClass();
			no = dataIns.GameNumber();

#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}
	}
}

実装例2. 継承の例  

```CSharp
// Adapterパターンの継承のサンプル(C#)

using System;

namespace AdapterPattern_Inheritance
{
	// このクラスは変更できないとする
	// 例：既に提供済みで変更できない、外部から提供されたライブラリなど
	public class DataClass
	{
		public int GetGameNumber()
		{
			return 1;
		}
	}

	// インターフェース
	public interface IInterfaceDataClass
	{
		int GameNumber();
	}

	// Adapter
	class AdapterDataClass : DataClass, IInterfaceDataClass
	{
		public int GameNumber()
		{
			return base.GetGameNumber();
		}
	}

	// メインプログラム
	class Program
	{
		// メイン（クライアント）
		static void Main(string[] args)
		{
			AdapterDataClass dataIns = new AdapterDataClass();
			int no = dataIns.GameNumber();
		}
	}
}
```
