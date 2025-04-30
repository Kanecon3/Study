# Composite パターン

イメージ的には、「ディレクトリ」と「ファイル」を意識せずに同じインターフェイス（同じコマンド）で容易に追加／削除できるファイルシステムのような実装パターンです。  

“Composite”は英語で「複合物」を表す言葉です。  

Composite パターンは「容器と中身を同一視する」ことで、再帰的な構造の取り扱いを容易にするデザインパターンです。  

## 実装例

```CSharp
// Compositeパターンのサンプル(C#)

using System;
using System.Collections.Generic;

namespace Composite
{
	// 抽象クラス（共通処理も入っている）
	public abstract class ComponentFileSystem
	{
		public List<ComponentFileSystem> Children { get; set; }

		public abstract string GetFileSystemType();
		public abstract string GetName();

		// 共通処理
		public void Entry(ComponentFileSystem parent)
		{
			if (parent.GetFileSystemType() == "DIRECTORY") {
				parent.Children.Add(this);
			}
		}
	}

	// ファイルとして扱う時のクラス
	public class FileData : ComponentFileSystem
	{
		readonly string m_name;

		public FileData(string name)
		{
			m_name = name;
		}

		public override string GetFileSystemType()
		{
			return "FILE";
		}

		public override string GetName()
		{
			return m_name;
		}
	}

	// ディレクトリとして扱う時のクラス
	public class DirectoryData : ComponentFileSystem
	{
		readonly string m_name;

		public DirectoryData(string name)
		{
			m_name = name;
			Children = new List<ComponentFileSystem>();
		}

		public override string GetFileSystemType()
		{
			return "DIRECTORY";
		}

		public override string GetName()
		{
			return m_name;
		}
	}


	//// メインプログラム /////
	class Program
	{
		static void Main(string[] args)
		{
			var root = new DirectoryData("root");

			var file1 = new FileData("File1");
			file1.Entry(root);

			var dict2 = new DirectoryData("Dict2");
			dict2.Entry(root);
			{
				var file2_1 = new FileData("File2_1");
				file2_1.Entry(dict2);

				var dict3 = new DirectoryData("Dict3");
				dict3.Entry(dict2);
				{
					var file3_1 = new FileData("File3_1");
					file3_1.Entry(dict3);
				}

				var file2_2 = new FileData("File2_2");
				file2_2.Entry(dict2);
			}

			// 表示
			int hierarchyCnt = 0;
			List<ComponentFileSystem> list = root.Children;
			DispData(list, hierarchyCnt);

#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}

		// 木構造を再帰で表示する関数
		static void DispData(List<ComponentFileSystem> list, int hierarchyCnt)
		{
			foreach (ComponentFileSystem cont in list) {
				string type = cont.GetFileSystemType();
				Console.Write(new string(' ', (hierarchyCnt*2)));
				Console.WriteLine("name:{0} type:{1}", cont.GetName(), cont.GetFileSystemType());
				if (type == "DIRECTORY") {
					DispData(cont.Children, hierarchyCnt+1);
				}
			}
		}
	}
}
```
