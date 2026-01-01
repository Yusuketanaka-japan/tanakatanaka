from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class RevenueStream:
    name: str
    description: str
    steps: List[str]
    example: str


def yen(amount: int) -> str:
    """Format currency for readability."""
    return f"¥{amount:,}"


def build_revenue_streams() -> List[RevenueStream]:
    return [
        RevenueStream(
            name="オンライン講座の販売",
            description=(
                "動画教材やライブ授業を販売し、受講者から直接収益を得る方法。"
                "初期に作った教材は何度も販売でき、スケールしやすいのが特徴です。"
            ),
            steps=[
                "1. 需要の高いテーマを選び、学習ゴールを明確にする",
                "2. 1本あたり5〜10分の短い動画でカリキュラムを組む",
                "3. Udemyなどのマーケットプレイスまたは自分のサイトで販売する",
                "4. 受講後アンケートを集め、次のアップデートに活かす",
            ],
            example=f"受講料 {yen(15000)} × 80名 = {yen(1_200_000)} / 月",
        ),
        RevenueStream(
            name="法人向け研修",
            description=(
                "企業の研修としてまとまった人数に教えるケース。"
                "単価が高く、リピートを狙いやすいのが強みです。"
            ),
            steps=[
                "1. 企業の課題ヒアリングを行い、社内データや業務例を教材に盛り込む",
                "2. 初回は体験ワークショップ（90分）で小さく導入",
                "3. 成果が見えたら3〜6ヶ月の研修パッケージを提案",
            ],
            example=f"1回 {yen(200_000)} の研修を月2社 = {yen(400_000)}",
        ),
        RevenueStream(
            name="コミュニティ／サブスク",
            description=(
                "質問対応や最新情報の提供を月額で行う継続モデル。"
                "安定収入を作りながらファンを育てられます。"
            ),
            steps=[
                "1. DiscordやSlackで質問部屋と成果共有チャンネルを用意",
                "2. 毎週のライブQAや課題レビューで参加動機を維持",
                "3. コース受講者をアップセルして参加者を増やす",
            ],
            example=f"月額 {yen(3_000)} × 50名 = {yen(150_000)}",
        ),
        RevenueStream(
            name="個別コンサルティング",
            description=(
                "教材ではカバーしきれない実務の壁を一緒に乗り越えるスポット収益。"
            ),
            steps=[
                "1. 60〜90分のオンライン相談枠を用意",
                "2. プロンプト添削や社内ワークフロー改善をテーマにする",
                "3. 改善結果を匿名で共有し、次の教材や営業資料に活かす",
            ],
            example=f"1時間 {yen(15_000)} × 10枠 = {yen(150_000)}",
        ),
        RevenueStream(
            name="資料テンプレートやプロンプト集の販売",
            description=(
                "授業で使った資料やプロンプトをダウンロード販売。"
                "低価格でも数が出ると大きな収益になります。"
            ),
            steps=[
                "1. プロジェクト例・ワークシート・評価基準をパッケージ化",
                "2. 初学者がすぐ使える手順書を添える",
                "3. コース購入者に割引を付けてクロスセルする",
            ],
            example=f"{yen(2_000)} の資料を月200件 = {yen(400_000)}",
        ),
    ]


def simulate_income(
    course_price: int = 15_000,
    course_students: int = 80,
    corporate_sessions: int = 2,
    corporate_rate: int = 200_000,
    community_members: int = 50,
    subscription_fee: int = 3_000,
    consulting_hours: int = 10,
    consulting_rate: int = 15_000,
    templates_sales: int = 200,
    template_price: int = 2_000,
) -> dict[str, int]:
    """Calculate a monthly income scenario for explanation purposes."""
    return {
        "オンライン講座": course_price * course_students,
        "法人研修": corporate_sessions * corporate_rate,
        "コミュニティ": community_members * subscription_fee,
        "個別コンサル": consulting_hours * consulting_rate,
        "テンプレート販売": templates_sales * template_price,
    }


def print_overview(streams: Iterable[RevenueStream]) -> None:
    print("\n===== 生成AI講師の主な収益源 =====\n")
    for stream in streams:
        print(f"■ {stream.name}")
        print(f"  ・{stream.description}")
        for step in stream.steps:
            print(f"    - {step}")
        print(f"  例: {stream.example}\n")


def print_simulation(result: dict[str, int]) -> None:
    print("===== 月間収益シミュレーション（例） =====")
    total = 0
    for name, amount in result.items():
        print(f"{name:<10} : {yen(amount)}")
        total += amount
    print("-" * 35)
    print(f"合計        : {yen(total)}\n")
    print("このように収益源を組み合わせると、安定した基盤を作りながら、\n"
          "学習者への提供価値を高め続けることができます。")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "生成AI講師がどのように稼いでいるかを説明するための簡易ツール。"
            "シミュレーションの数字はオプションで調整できます。"
        )
    )
    parser.add_argument("--course-price", type=int, default=15_000, help="オンライン講座の受講料")
    parser.add_argument("--course-students", type=int, default=80, help="月の受講者数")
    parser.add_argument("--corporate-sessions", type=int, default=2, help="月あたりの法人研修回数")
    parser.add_argument("--corporate-rate", type=int, default=200_000, help="法人研修1回の単価")
    parser.add_argument("--community-members", type=int, default=50, help="コミュニティ会員数")
    parser.add_argument("--subscription-fee", type=int, default=3_000, help="コミュニティ月額")
    parser.add_argument("--consulting-hours", type=int, default=10, help="個別相談の実施時間数")
    parser.add_argument("--consulting-rate", type=int, default=15_000, help="個別相談1時間の単価")
    parser.add_argument("--templates-sales", type=int, default=200, help="テンプレート販売数")
    parser.add_argument("--template-price", type=int, default=2_000, help="テンプレート単価")
    parser.add_argument("--overview-only", action="store_true", help="シミュレーションを表示せず概要のみ表示")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    streams = build_revenue_streams()
    print_overview(streams)

    if args.overview_only:
        return

    simulation = simulate_income(
        course_price=args.course_price,
        course_students=args.course_students,
        corporate_sessions=args.corporate_sessions,
        corporate_rate=args.corporate_rate,
        community_members=args.community_members,
        subscription_fee=args.subscription_fee,
        consulting_hours=args.consulting_hours,
        consulting_rate=args.consulting_rate,
        templates_sales=args.templates_sales,
        template_price=args.template_price,
    )
    print_simulation(simulation)


if __name__ == "__main__":
    main()
