#!/usr/bin/env python3
# coding=utf-8
"""
slide-ai client — 上传 deck 到 slide-ai 服务

用法：
    python client.py <deck-id> [deck-dir]

参数：
    deck-id   deck 的唯一标识，如 mask-master-intro
    deck-dir  deck 目录路径，默认 decks/<deck-id>

环境变量：
    SLIDE_AI_URL        后端地址，默认 http://localhost:8100
    SLIDE_AI_PUBLIC_URL 对外分享域名，默认 http://slide.liamzheng.cn
"""
import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path


def upload_deck(deck_id: str, deck_dir: Path) -> dict:
    base_url = os.environ.get(
        'SLIDE_AI_URL', 'http://localhost:8100')
    files = {}
    for f in sorted(deck_dir.iterdir()):
        if f.suffix == '.yml':
            files[f.name] = f.read_text(encoding='utf-8')
    if not files:
        print(f"[error] {deck_dir} 下没有找到 .yml 文件")
        sys.exit(1)
    payload = json.dumps(
        {'id': deck_id, 'files': files},
        ensure_ascii=False,
    ).encode('utf-8')
    req = urllib.request.Request(
        f'{base_url}/api/decks',
        data=payload,
        headers={'Content-Type': 'application/json'},
        method='POST',
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"[error] HTTP {e.code}: {body}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    deck_id = sys.argv[1]
    deck_dir = Path(
        sys.argv[2] if len(sys.argv) > 2
        else f'decks/{deck_id}'
    )
    if not deck_dir.exists():
        print(f"[error] 目录不存在: {deck_dir}")
        sys.exit(1)
    print(f"[upload] {deck_id} ({deck_dir}) ...")
    result = upload_deck(deck_id, deck_dir)
    public_url = os.environ.get(
        'SLIDE_AI_PUBLIC_URL', 'http://slide.liamzheng.cn')
    share_url = f'{public_url}/?deck={deck_id}'
    print(f"[ok] {result.get('title')} "
          f"· {result.get('slide_count')} 页")
    print(f"[link] {share_url}")


if __name__ == '__main__':
    main()
