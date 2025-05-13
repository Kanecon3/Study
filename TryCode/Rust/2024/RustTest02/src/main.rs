fn do_something() {}

fn main() {
    // rust-analyzerを有効にすると
    // 一度も使用していない i に警告(下に波線)が表示される
    for i in 0..100 {
        do_something();
    }
}
