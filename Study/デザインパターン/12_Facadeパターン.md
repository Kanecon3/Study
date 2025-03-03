# Facade パターン

Facade パターンは、ある機能を使う時に複雑な手順が必要な場合、その複雑な手順をまとめてシンプルなAPI／関数を作成し、クライアントに提供するパターンです。  

Facade（ファサード）とは「建物の正面」を意味します。  

## 実装例

Facadeパターン**実装後**の例:

```CSharp
// Facadeパターンのサンプル(C#)

using System;
using System.Collections.Generic;

namespace Facade
{
	// このクラスは通信用のソケットだとします
	public class OriginalSocket
	{
		public void Request(string reqStr)
		{
			// 要求処理
		}

		public string Response()
		{
			// 要求に対する受け取り処理
			return "response";
		}
	}

	// ソケットを使って送受信する、ログを保持する
	public class CommunicationData
	{
		private List<string> m_logSend = new List<string>();
		private List<string> m_logRecv = new List<string>();

		public void SendJsonString(OriginalSocket socket, string jsonStr)
		{
			socket.Request(jsonStr);
			m_logSend.Add(jsonStr);
		}

		public string ReceiveResponse(OriginalSocket socket)
		{
			string recv = socket.Response();
			m_logRecv.Add(recv);
			return recv;
		}
	}

	// 送信する文字列をJson形式にコンバートする
	public class ConvertSendString
	{
		public string CreateSendJson(string str)
		{
			string jsonStr;
			jsonStr = $"{{msg:{str}}}";
			return jsonStr;
		}
	}

	// Facadeパターン用のクラス
	public class TransceiverDataAPI
	{
		OriginalSocket m_socket = new OriginalSocket();
		ConvertSendString m_converter = new ConvertSendString();
		CommunicationData m_communication = new CommunicationData();

		public void SendData(string sendStr)
		{
			string jsonStr = m_converter.CreateSendJson(sendStr);
			m_communication.SendJsonString(m_socket, jsonStr);
		}

		public string ReceiveResponse()
		{
			return m_communication.ReceiveResponse(m_socket);
		}
	}


	//// メインプログラム /////
	class Program
	{
		static void Main(string[] args)
		{
			var transceiver = new TransceiverDataAPI();

			// 送信1
			string sendStr1 = "Hello";
			transceiver.SendData(sendStr1);
			string recvResponce1 = transceiver.ReceiveResponse();

			// 送信2
			string sendStr2 = " World";
			transceiver.SendData(sendStr2);
			string recvResponce2 = transceiver.ReceiveResponse();


#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}
	}
}
```

Facadeパターン**実装前**の例:

```CSharp
// Facadeパターン実装前のサンプル(C#)

using System;
using System.Collections.Generic;

namespace FacadeBefore
{
	// このクラスは通信用のソケットだとします
	public class OriginalSocket
	{
		public void Request(string reqStr)
		{
			// 要求処理
		}

		public string Response()
		{
			// 要求に対する受け取り処理
			return "response";
		}
	}

	// ソケットを使って送受信する、ログを保持する
	public class CommunicationData
	{
		private List<string> m_logSend = new List<string>();
		private List<string> m_logRecv = new List<string>();

		public void SendJsonString(OriginalSocket socket, string jsonStr)
		{
			socket.Request(jsonStr);
			m_logSend.Add(jsonStr);
		}

		public string ReceiveResponse(OriginalSocket socket)
		{
			string recv = socket.Response();
			m_logRecv.Add(recv);
			return recv;
		}
	}

	// 送信する文字列をJson形式にコンバートする
	public class ConvertSendString
	{
		public string CreateSendJson(string str)
		{
			string jsonStr;
			jsonStr = $"{{msg:{str}}}";
			return jsonStr;
		}
	}


	//// メインプログラム /////
	class Program
	{
		static void Main(string[] args)
		{
			var socket = new OriginalSocket();
			var converter = new ConvertSendString();
			var communication = new CommunicationData();

			// 送信1
			string sendStr1 = "Hello";
			string jsonStr1 = converter.CreateSendJson(sendStr1);
			communication.SendJsonString(socket, jsonStr1);
			string recvResponce1 = communication.ReceiveResponse(socket);

			// 送信2
			string sendStr2 = " World";
			string jsonStr2 = converter.CreateSendJson(sendStr2);
			communication.SendJsonString(socket, jsonStr2);
			string recvResponce2 = communication.ReceiveResponse(socket);


#if true	// テスト専用のコード
			Console.ReadKey();
#endif
		}
	}
}
```
