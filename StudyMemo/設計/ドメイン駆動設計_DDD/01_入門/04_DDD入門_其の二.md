# 其の二

## エンティティ

同一性によって識別されるドメインオブジェクトです。値オブジェクトと同じようにドメイン駆動設計において重要なドメインオブジェクトになります。  

### エンティティの性質

1. 可変である
2. 同じ属性であっても区別される
3. 同一性によって区別される  

エンティティは、値オブジェクトの性質を真逆にしたような性質もあります。  

#### 可変である

エンティティの属性は変化することが許容されています。  
しかし、すべての属性を可変にする必要はありません。可能な限り不変にしておくことはよい習慣です。  

例えば、ユーザー情報  
人生において実際の名前を変更するケースはそれほど頻繁にはありませんが、システム上のユーザー名を変更することはあると思います。  

ユーザー名変更のコードの例:  

```CSharp
class User
{
    private string m_name;

    public User(string name)
    {
        Debug.Assert(string.IsNullOrEmpty(name));
        m_name = name;
    }

    // ユーザー名変更用のメソッド
    public void ChangeName(string name)
    {
        Debug.Assert(string.IsNullOrEmpty(name));
        m_name = name;
    }
}
```

プロパティのsetterで変更するのではなく、ふるまいが何であるかを表現するユーザー名の変更用のメソッドを用意しています。  

#### 同じ属性であっても区別される

値オブジェクトは同じ属性であれば同じものとして扱われましたが、エンティティはたとえ同じ属性であっても区別されます。  

例えば、同姓同名の人間がいたとします。同姓同名であっても同一人物ではありませんね。わたしたち人間の区別はもっと別のところにあるということと、エンティティは同じです。  
エンティティを区別するためには識別子（Identity）が利用されます。  
さきほどのユーザー情報であれば、UserIdという属性を作るのが一般的でしょう。  

```CSharp
// ユーザーID
class UserId
{
    private readonly int m_value;

    public UserId(int value)
    {
        // 注：本来であればUserIdが被らないように自動採番する機能が必要
        m_value = value;
    }

    public int Value { get { return m_value; }}
}

// ユーザー情報
class User
{
    private readonly UserId m_userId;
    private string m_name;

    public User(UserId userId, string name)
    {
        Debug.Assert(userId != null);
        Debug.Assert(string.IsNullOrEmpty(name));

        m_userId = userId;
        m_name = name;
    }

    public bool IsCompareUser(User checkUser)
    {
        Debug.Assert(checkUser != null);

        bool result = (m_userId.Value == checkUser.m_userId.Value);
        return result;
    }
}
```

```CSharp
User user1 = new User(new UserId(1), "yamada taro");
User user2 = new User(new UserId(2), "yamada taro");
bool result = user1.IsCompareUser(user2);
// 名前が同じユーザーだが、識別子（UserId)が違うので、比較しても同一人物とはならない
```

#### 同一性によって区別される

さきほどのユーザー情報を例にあげると、名前を変えても同一の人物と認識するシステムがほとんどではないでしょうか。識別子だけを比較することにより、同一性の比較が可能になります。  
このように属性が異なっていたとしても同じものとしてみなす必要があるものが存在します。
