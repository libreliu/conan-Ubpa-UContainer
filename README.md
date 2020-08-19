# conan-Ubpa-UContainer

[U 神](https://github.com/Ubpa) 的 UContainer 的 Conan 版本

> UCMake 实在太混乱了，我 “port” 到了 Conan，请 U 神不要打我（呜呜

## TODO
- [ ] 写个通用 Patch
- [x] Git commit 哈希写进去
- [ ] 补充 `test()` 方法

## 思路

1. Conan 的 settings 机制可以处理 Debug/Release 版本切换，所以不需要 `CMAKE_DEBUG_POSTFIX`
2. 不想拖家带口的编译，所以把 UCMake Patch 掉了

## License

U 神原来仓库里面的是 MIT，这里的脚本也是 MIT

> patches 里面基本是直接从 UCMake 抄的