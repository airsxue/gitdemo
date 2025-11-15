import pandas as pd
import ast

# 构造示例 DataFrame
df = pd.DataFrame({
    "库存ID_工序组代码_智能单元类集合": [
        "('87_AAA_1','87_BBB_2')",   # ✅ 合法 tuple 字符串
        "87_CM_CM_48",               # ⚠️ 无括号（会被自动包成单元素元组）
        "('87_DR_1',)",              # ✅ 单元素 tuple 字符串
        "",                          # ⚠️ 空字符串
        None                         # ⚠️ 空值
    ]
})

# 临时安全处理代码（最小改动版）
df["库存ID_工序组代码_智能单元类集合"] = df["库存ID_工序组代码_智能单元类集合"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith("(") else (x,)
)

# 查看结果
for i, v in enumerate(df["库存ID_工序组代码_智能单元类集合"]):
    print(f"{i}: {v}  ---> 类型: {type(v)}")