# 其の四

## サービスとは

ソフトウェア開発の文脈で語られる「サービス」は、クライアントのために何かを行うオブジェクトです。  

ドメイン駆動設計におけるサービスは大きく分けて2つ

- ドメインサービス
- アプリケーションサービス

## ドメインサービスとは

値オブジェクトやエンティティに記述すると不自然になってしまうふるまいが存在します。ドメインサービスはそういった不自然さを解決するオブジェクトです。  

例えば...  
システムによってはユーザー名の重複を許可しないことがあり得ます。ユーザー名の重複を許さないというのはドメインのルールです。  
しかし、重複のチェックはどのクラスで行うべきでしょうか？ユーザー情報のエンティティであるUserクラスで行うべきでしょうか？  

Userクラスで行う例:  

```CSharp
class User
{
    public Name { get; }

    public User(string name)
    {
        Name = name;
    }

    // ユーザー名の重複確認の処理
    public bool ExistName(string name)
    {
        // 重複確認処理があるとする
    }
}
```

```CSharp
User user = new User("user1");
bool result = user.ExistName(user.Name);    // 生成した自分自身のオブジェクトに問い合わせしている
```

このようにしてしまうと、生成した自分自身のオブジェクトに問い合わせするという状態になってしまいます。これらは複数のドメインオブジェクトを横断するような操作によく見られます。  

そんなときに活用するのがサービスと呼ばれるオブジェクトです。  

```CSharp
class UserService
{
    // ユーザー名の重複確認の処理
    public bool ExistName(User user)
    {
        ===省略===
        // 重複確認処理があるとする
    }
}
```

```CSharp
var userService = new UserService();

var user1 = new User("Yamada");
bool existResult = userService.ExistName(user1);

if (existResult) {
    // 重複している場合の処理
} else {
    // 重複していない場合の処理
}
```

UserServiceというドメインサービスを用意することで、自分自身に重複を問い合わせする必要がなくなりました。  

サービスは便利な存在です。ドメインオブジェクトに記述すべきふるまいは、やろうと思えば全てサービスに入れてしまうことができます。**重要なのは「不自然なふるまい」のみサービスに記述することです**。可能な限りドメインサービスは避けて下さい。  

### ドメインサービスの命名規則

一般的にドメインサービスの命名規則は次の3つの内のどれかになることが多いようです。  

1. ドメインの概念
2. ドメインの概念＋Service
3. ドメインの概念＋DomainService

ドメインサービスであることがチーム共通認識となるのであればどれを選択してもOKです。  
