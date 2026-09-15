#!/usr/bin/env python3
"""
BJ Jang Signature EDA Chart Generator (eda_charts.py)
Generates publication-quality, branded business charts for presentation slides
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

try:
    import koreanize_matplotlib
except ImportError:
    pass

# BJ Jang Signature Brand Colors
COLOR_PRIMARY = "#1E40AF"      # Deep Royal Blue
COLOR_ACCENT = "#2563EB"       # Electric Blue
COLOR_ACCENT_SOFT = "#EFF6FF"  # Soft Tint Blue
COLOR_BG = "#F8FAFC"           # Slate Off-White
COLOR_CARD_BG = "#FFFFFF"      # Crisp White
COLOR_TEXT = "#0F172A"         # Deep Slate
COLOR_TEXT_MUTED = "#64748B"   # Slate Gray
COLOR_POSITIVE = "#059669"     # Emerald Green
COLOR_NEGATIVE = "#DC2626"     # Crimson Red
COLOR_GRID = "#E2E8F0"         # Light Gray Grid


class BJChartGenerator:
    def __init__(self, df: pd.DataFrame, output_dir: str | Path):
        self.df = df
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._setup_style()

    def _setup_style(self):
        plt.rcParams["font.family"] = "sans-serif"
        plt.rcParams["font.sans-serif"] = ["Pretendard", "Noto Sans KR", "Malgun Gothic", "Arial"]
        plt.rcParams["axes.unicode_minus"] = False
        plt.rcParams["figure.facecolor"] = COLOR_BG
        plt.rcParams["axes.facecolor"] = COLOR_CARD_BG
        plt.rcParams["axes.edgecolor"] = COLOR_GRID
        plt.rcParams["axes.grid"] = True
        plt.rcParams["grid.color"] = COLOR_GRID
        plt.rcParams["grid.linestyle"] = "--"
        plt.rcParams["grid.alpha"] = 0.7

    def render_kpi_dashboard(self, eda_summary: Dict[str, Any]) -> Path:
        """Renders 4 executive KPI cards in a 2x2 or 1x4 visual layout."""
        num_stats = eda_summary.get("descriptive", {}).get("numerical", {})
        top_keys = list(num_stats.keys())[:4]

        fig, axes = plt.subplots(1, max(len(top_keys), 1), figsize=(12, 3), dpi=200)
        if len(top_keys) == 1:
            axes = [axes]

        fig.patch.set_facecolor(COLOR_BG)

        for i, key in enumerate(top_keys):
            ax = axes[i]
            stat = num_stats[key]
            mean_val = stat.get("mean", 0)
            sum_val = stat.get("sum", 0)
            max_val = stat.get("max", 0)

            ax.set_facecolor(COLOR_CARD_BG)
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["bottom"].set_color(COLOR_GRID)
            ax.spines["left"].set_color(COLOR_PRIMARY)
            ax.spines["left"].set_linewidth(4)
            ax.set_xticks([])
            ax.set_yticks([])

            ax.text(0.08, 0.75, key, fontsize=13, fontweight="bold", color=COLOR_TEXT, transform=ax.transAxes)
            display_val = f"{sum_val:,.0f}" if sum_val > 10000 else f"{mean_val:,.1f}"
            ax.text(0.08, 0.40, display_val, fontsize=20, fontweight="heavy", color=COLOR_PRIMARY, transform=ax.transAxes)
            ax.text(0.08, 0.15, f"평균 {mean_val:,.1f} · 최대 {max_val:,.1f}", fontsize=9, color=COLOR_TEXT_MUTED, transform=ax.transAxes)

        plt.tight_layout()
        out_path = self.output_dir / "03_kpi_cards.png"
        fig.savefig(out_path, bbox_inches="tight", dpi=200)
        plt.close(fig)
        return out_path

    def render_trend_chart(self, date_col: Optional[str] = None, val_col: Optional[str] = None) -> Path:
        """Renders a sleek time-series trend line with area fill."""
        df = self.df
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if not val_col:
            val_col = num_cols[0] if num_cols else None

        fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
        fig.patch.set_facecolor(COLOR_BG)
        ax.set_facecolor(COLOR_CARD_BG)

        if date_col and date_col in df.columns:
            plot_df = df.copy()
            plot_df[date_col] = pd.to_datetime(plot_df[date_col], errors="coerce")
            plot_df = plot_df.dropna(subset=[date_col]).sort_values(date_col)
            x_vals = plot_df[date_col]
            y_vals = plot_df[val_col]
        else:
            y_vals = df[val_col].iloc[:30] if len(df) > 30 else df[val_col]
            x_vals = range(1, len(y_vals) + 1)

        ax.plot(x_vals, y_vals, color=COLOR_ACCENT, linewidth=2.5, marker="o", markersize=4, label=f"{val_col} 추이")
        ax.fill_between(x_vals, y_vals, alpha=0.15, color=COLOR_PRIMARY)

        # Rolling average
        if len(y_vals) > 7:
            roll = pd.Series(y_vals).rolling(window=5, min_periods=1).mean()
            ax.plot(x_vals, roll, color=COLOR_POSITIVE, linestyle="--", linewidth=1.5, label="이동평균(5구간)")

        ax.set_title(f"{val_col} 변동 추세 및 성장 분석", fontsize=15, fontweight="bold", color=COLOR_TEXT, pad=15)
        ax.set_xlabel("기간 / 인덱스", fontsize=11, color=COLOR_TEXT_MUTED, labelpad=8)
        ax.set_ylabel(val_col, fontsize=11, color=COLOR_TEXT_MUTED, labelpad=8)
        ax.legend(frameon=True, facecolor=COLOR_CARD_BG, edgecolor=COLOR_GRID)

        out_path = self.output_dir / "04_trend_chart.png"
        fig.savefig(out_path, bbox_inches="tight", dpi=200)
        plt.close(fig)
        return out_path

    def render_category_ranking(self, cat_col: Optional[str] = None, val_col: Optional[str] = None) -> Path:
        """Renders ranked horizontal bar chart."""
        df = self.df
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()

        if not cat_col and cat_cols:
            cat_col = cat_cols[0]
        if not val_col and num_cols:
            val_col = num_cols[0]

        fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
        fig.patch.set_facecolor(COLOR_BG)
        ax.set_facecolor(COLOR_CARD_BG)

        if cat_col and val_col:
            grouped = df.groupby(cat_col)[val_col].sum().sort_values(ascending=True).tail(8)
            y_pos = range(len(grouped))
            bars = ax.barh(y_pos, grouped.values, color=COLOR_PRIMARY, height=0.6, alpha=0.9)
            if len(bars) > 0:
                bars[-1].set_color(COLOR_ACCENT)  # Highlight top 1

            ax.set_yticks(y_pos)
            ax.set_yticklabels(grouped.index, fontsize=11, color=COLOR_TEXT)

            for bar in bars:
                w = bar.get_width()
                ax.text(w * 1.01, bar.get_y() + bar.get_height() / 2, f"{w:,.0f}",
                        va="center", ha="left", fontsize=10, color=COLOR_TEXT, fontweight="bold")

            ax.set_title(f"카테고리({cat_col})별 {val_col} 기여도 랭킹 (Top 8)", fontsize=15, fontweight="bold", color=COLOR_TEXT, pad=15)
        else:
            ax.text(0.5, 0.5, "충분한 범주형 데이터 없음", ha="center", va="center")

        out_path = self.output_dir / "05_category_chart.png"
        fig.savefig(out_path, bbox_inches="tight", dpi=200)
        plt.close(fig)
        return out_path

    def render_correlation_heatmap(self) -> Path:
        """Renders correlation matrix heatmap."""
        num_df = self.df.select_dtypes(include=[np.number])
        if num_df.shape[1] > 8:
            num_df = num_df.iloc[:, :8]

        fig, ax = plt.subplots(figsize=(8, 6), dpi=200)
        fig.patch.set_facecolor(COLOR_BG)
        ax.set_facecolor(COLOR_CARD_BG)

        if num_df.shape[1] >= 2:
            corr = num_df.corr()
            mask = np.triu(np.ones_like(corr, dtype=bool))
            cmap = sns.diverging_palette(220, 20, as_cmap=True)
            sns.heatmap(corr, annot=True, fmt=".2f", cmap=cmap, vmin=-1, vmax=1,
                        square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
            ax.set_title("주요 수치형 변수 간 상관관계 매트릭스 (Correlation Heatmap)", fontsize=13, fontweight="bold", pad=15)
        else:
            ax.text(0.5, 0.5, "수치형 변수가 부족하여 상관분석 불가", ha="center", va="center")

        out_path = self.output_dir / "06_correlation_heatmap.png"
        fig.savefig(out_path, bbox_inches="tight", dpi=200)
        plt.close(fig)
        return out_path

    def generate_all(self, eda_summary: Dict[str, Any]) -> Dict[str, str]:
        health = eda_summary.get("health", {})
        date_cols = health.get("datetime_cols", [])
        num_cols = health.get("numerical_cols", [])
        cat_cols = health.get("categorical_cols", [])

        target = eda_summary.get("correlations", {}).get("target_column")

        kpi_p = self.render_kpi_dashboard(eda_summary)
        trend_p = self.render_trend_chart(date_cols[0] if date_cols else None, target or (num_cols[0] if num_cols else None))
        cat_p = self.render_category_ranking(cat_cols[0] if cat_cols else None, target or (num_cols[0] if num_cols else None))
        corr_p = self.render_correlation_heatmap()

        return {
            "kpi_cards": str(kpi_p),
            "trend_chart": str(trend_p),
            "category_chart": str(cat_p),
            "correlation_heatmap": str(corr_p),
        }
