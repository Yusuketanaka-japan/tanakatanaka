# 生成AI講師の稼ぎ方を説明するツール

`ai_instructor_income_tool.py` は、生成AIの講師がどのように収益を得ているのかを学生にわかりやすく示すためのCLIツールです。

## 使い方

Python 3 があれば追加の依存は不要です。

### 概要とサンプルの月次収益を表示

```bash
python ai_instructor_income_tool.py
```

### 数字を変えてシミュレーション

以下のようにオプションで金額や人数を変更できます。

```bash
python ai_instructor_income_tool.py \
  --course-price 18000 \
  --course-students 50 \
  --corporate-sessions 3 \
  --corporate-rate 250000 \
  --community-members 80 \
  --subscription-fee 4000 \
  --consulting-hours 8 \
  --consulting-rate 20000 \
  --templates-sales 150 \
  --template-price 2500
```

### 概要だけ見たい場合

```bash
python ai_instructor_income_tool.py --overview-only
```

ツールは主な収益源ごとの説明と実現ステップ、また可変の数字を使った月間収益シミュレーションを表示します。授業でのディスカッション材料としてそのまま画面共有できます。
