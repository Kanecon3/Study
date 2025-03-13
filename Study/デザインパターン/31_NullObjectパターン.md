# Null Object パターン

※Null Object パターンはGoFのデザインパターンではありません。

下記のような  

```
if (a != null) {
  // nullじゃなかったら処理する
}

if (b != null) {
  // nullじゃなかったら処理する
}
```

よくあるnullオブジェクトをチェックするコードだらけになるのを防ぐパターンです。  

## メリット

クライアントがnullチェックをするコードだらけになるのを防げます。  

## デメリット

使用する側がNull Objectパターンで実装されていることを知っていないと問題が発生する可能性が高くなります。  

## 実装例

```CSharp
// Null Objectパターンのサンプル(C#)

using System;

namespace NullObjectPattern
{
	class Program
	{
		static void Main(string[] args)
		{
#if false
			IUser user = null;
#else
			IUser user = new NullUser();	// null初期値の代わりとしてNullUserをnewする
#endif

			// userにインスタンスをセットしていない場合としてテスト
			{
				int id = user.GetID();
				string name = user.GetName();
				Console.WriteLine("id = " + id);
				Console.WriteLine("name = " + id);
			}

			// userにインスタンスをセットした場合のテスト
			{
				user = new User();

				int id = user.GetID();
				string name = user.GetName();
				Console.WriteLine("id = " + id);
				Console.WriteLine("name = " + id);
			}



#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}
	}


	interface IUser
	{
		int GetID();
		string GetName();
	}

	class User : IUser
	{
		int m_id = 0;
		string m_name = "";

		public int GetID()
		{
			return m_id;
		}

		public string GetName()
		{
			return m_name;
		}
	}

	// nullの代わりのNullクラスを作成する
	public class NullUser : IUser
	{
		public int GetID()
		{
			return -1;  // エラーコードとして返す
		}

		public string GetName()
		{
			return "Unknown"; // エラーコードとして返す
		}
	}
}
```

## 補足

IsNullメソッド（もしくはプロパティ）を作っておくパターンもあるようですが、これはアンチパターンのようです。  
これは、クライアントに  

```
if (xxxx.IsNull() == true)
{
    // 何らかの処理
}
```

というコードが大量発生してしまい、結局はnullチェックと同じになってしまうからです。  
