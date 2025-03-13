# 其の一

## 値オブジェクト

値オブジェクトとは？  
システム固有の値を表したオブジェクト  

例えば、電話番号をInt型ではなくPhoneNumber型を作ることで、ドメインの業務をコード上でわかりやすく示すことができます。  

値オブジェクトのコンセプトは「システム固有の値を作ろう」という単純なものです。システムには、そのシステムならではの値が必ずあるはずです。もちろんプリミティブな値だけでソフトウェアを構築することは可能です。しかし、プリミティブ型は汎用的過ぎて、どうしても表現力が乏しくなってしまいます。  

ドメインにはさまざまなルールがあります。値オブジェクトを定義すると、そういったルールは値オブジェクトに記述され、コードがドキュメントとして機能し始めます。  

値オブジェクトは**ドメインの知識をコードへ落とし込むドメイン駆動設計の基本のパターン**です。ドメインの概念をオブジェクトとして定義しようとするときに、まずは値オブジェクトにあてはめてみることを検討してみて下さい。  

### 値オブジェクトの性質

1. 不変である  
2. 交換可能である
3. 等価性による比較

#### 不変である

```CSharp
class Money
{
    private readonly decimal m_amount;
    private readonly string m_currency;

    public Money(decimal amount, string currency)
    {
        // コンストラクタでしか値をセット出来ないようにすることで
        // 値オブジェクトに不変性を持たせる
        m_amount = amount;
        m_currency = currency;
    }

    // getterのみでsetterは作らない
    public decimal Amount { get { return m_amount; }}
    public decimal Currency { get { return m_currency; }}
}
```

#### 交換可能である

```CSharp
Money money = new Money(1000, "Yen");
money = new Money(100, "Doller");
```

値オブジェクトは不変のために属性の変更はできない。  
代入操作による交換以外で変更を表現できなくなっている。  

#### 等価性による比較

```CSharp
Money money1 = new Money(1000, "Yen");
Money money2 = new Money(1000, "Yen");

// 比較
bool chk = money1.Equals(money2);   // 属性が等価なのでtrueになるはず
```

### ふるまいを持った値オブジェクト

値オブジェクトで重要なことは、独自のふるまいを定義できることです。  

＜例＞お金を表現する  

値オブジェクトで表した場合:  

```CSharp
class Money
{
    private readonly decimal m_amount;
    private readonly string m_currency;

    public Money(decimal amount, string currency)
    {
        Debug.Assert(string.IsNullOrEmpty(currency));

        m_amount = amount;
        m_currency = currency;
    }

    public Money Add(Money arg)
    {
        Debug.Assert(arg != null);
        Debug.Assert(arg.m_currency == arg.m_currency);  // 同一通貨のチェック

        decimal result = m_amount + arg.m_amount;
        return new Money(result, m_currency);
    }
}

// 成功
Money money1 = new Money(1000, "Yen");
Money money2 = new Money(100, "Yen");
Money money3 = money1.Add(money2);  // 通貨が揃っているので成功

// エラー
Money yenMoney = new Money(1000, "Yen");       // 円
Money dollerMoney = new Money(100, "Doller");  // ドル
MOney errMoney = yenMoney.Add(dollerMoney);    // 通貨が揃っていないのでエラー
```

プリミティブ型で表した場合:  

```CSharp
decimal yenMoney = 1000;    // 円
decimal dollerMoney = 100;  // ドル

decimal errMony = yemMoney + dollerMoney;   // 通貨が揃っていないので本来はエラーだが加算出来てしまう
```

このように独自のふるまいを定義することで、システマチックに誤った操作を防止できます。  
値オブジェクトはただのデータ構造体を表しているのではなく、オブジェクトに対する操作をふるまいとして一処にまとめることで、自身に関するルールを語るドメインオブジェクトらしさを表します。  

### 値オブジェクトを採用するメリット

値オブジェクトを表現するということは、プリミティブ型で実装するときより定義するクラスの数が増加していくということです。今までプリミティブ型で実装することに慣れきっている開発者には抵抗があるかもしれません。  

値オブジェクトを採用するメリットには以下のようなものがあるでしょう。  

1. 表現力を増す
2. 不正な値を存在させない
3. 誤った代入を防ぐ
4. ロジックの散在を防ぐ
