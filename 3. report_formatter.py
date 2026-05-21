#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ContentForge - 选材报告格式化工具（非核心辅助脚本）
"""

from datetime import datetime

def format_scout_report(recommendations: list) -> str:
    """格式化侦察兵选材报告"""
    header = f"""📡 侦察兵选材报告
━━━━━━━━━━━━━━━━
扫描时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}
"""
    content = header
    
    for i, rec in enumerate(recommendations, 1):
        content += f"""
【推荐{i}】{rec.get('title', '未命名标题')}
  来源：{rec.get('source', '未知')}
  热度：{rec.get('hot', '中')}
  评分：{rec.get('score', 0)}分
  推荐理由：{rec.get('reason', '具备爆款潜力')}
━━━━━━━━━━━━━━━━
"""
    return content

# 示例使用
if __name__ == "__main__":
    sample = [
        {"title": "中方回应特朗普相关表态", "source": "头条热榜", "hot": "高", "score": 12, "reason": "时效性强，中国角色突出"}
    ]
    print(format_scout_report(sample))
