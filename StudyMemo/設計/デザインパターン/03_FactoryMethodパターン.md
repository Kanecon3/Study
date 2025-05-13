# Factory Method パターン：デザインパターン

Template Method パターンをインスタンス生成に利用したパターンです。  
インスタンスの作り方をスーパークラスで定め、具体的な処理をサブクラスで行います。  

 ## メリット

- クライアントが使用するときに、オブジェクトの生成が容易になる
- オブジェクトの生成と具体的な処理を分離することで、より柔軟にオブジェクトの生成、利用ができる

## 実装例

```CSharp
// Factory Methodパターンのサンプル(C#)

using System;

namespace FactoryMethod
{
	///// 抽象クラス /////

	public abstract class TaskSuperClass
	{
		public abstract void Execute();
	}

	public abstract class FactorySuperClass
	{
		public TaskSuperClass Create(string owner)
		{
			TaskSuperClass task = CreateTask(owner);
			return task;
		}

		public abstract TaskSuperClass CreateTask(string owner);
	}


	///// 具象クラス /////

	// サブクラス1
	public class TaskType1 : TaskSuperClass
	{
		private readonly string m_userName = string.Empty;

		internal TaskType1(string owner)
		{
			m_userName = owner;
		}

		public override void Execute()
		{
			Console.WriteLine("task1 user = " + m_userName);
		}
	}

	// サブクラス2
	public class TaskType2 : TaskSuperClass
	{
		internal TaskType2(string owner)
		{
		}

		public override void Execute()
		{
			Console.WriteLine("task2");
		}
	}

	// factoryクラス
	public class TaskFactory : FactorySuperClass
	{
		public override TaskSuperClass CreateTask(string owner)
		{
			if (owner == "user2") {
				return new TaskType2(owner);
			}

			return new TaskType1(owner);
		}
	}


	//// メインプログラム /////
	class Program
	{
		static void Main(string[] args)
		{
			var factory = new TaskFactory();

			{
				TaskSuperClass task = factory.CreateTask("user1");
				task.Execute();
			}

			{
				TaskSuperClass task = factory.CreateTask("user2");
				task.Execute();
			}


#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}
	}
}
```
