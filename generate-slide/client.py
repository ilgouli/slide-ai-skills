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
    SLIDE_AI_URL      服务地址，默认 http://slide.liamzheng.cn
    SLIDE_AI_API_KEY  API Key，未设置时自动注册并保存到
                      ~/.slide-ai/config.json
"""
import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

BASE_URL = os.environ.get(
    'SLIDE_AI_URL', 'http://slide.liamzheng.cn')

_CONFIG_PATH = (
    Path.home() / '.slide-ai' / 'config.json')


def _load_config() -> dict:
    if _CONFIG_PATH.exists():
        return json.loads(
            _CONFIG_PATH.read_text(encoding='utf-8'))
    return {}


def _save_config(data: dict):
    _CONFIG_PATH.parent.mkdir(
        parents=True, exist_ok=True)
    _CONFIG_PATH.write_text(
        json.dumps(
            data, indent=2, ensure_ascii=False),
        encoding='utf-8',
    )


def _get_api_key() -> str:
    api_key = os.environ.get('SLIDE_AI_API_KEY')
    if api_key:
        return api_key
    config = _load_config()
    if config.get('api_key'):
        return config['api_key']
    return _register()


def _register() -> str:
    print("[register] 自动注册账户 ...")
    req = urllib.request.Request(
        f'{BASE_URL}/api/users/register',
        data=b'{}',
        headers={'Content-Type': 'application/json'},
        method='POST',
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(
            f"[error] 注册失败 HTTP {e.code}: {body}")
        sys.exit(1)
    api_key = data['api_key']
    config = _load_config()
    config['api_key'] = api_key
    _save_config(config)
    print(f"[register] 完成，api_key 已保存到"
          f" {_CONFIG_PATH}")
    return api_key


def _post_json(
        url: str,
        payload: bytes,
        headers: dict) -> dict:
    req = urllib.request.Request(
        url, data=payload,
        headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"[error] HTTP {e.code}: {body}")
        sys.exit(1)


def upload_deck(
        deck_id: str,
        deck_dir: Path,
        api_key: str) -> dict:
    files = {}
    for f in sorted(deck_dir.iterdir()):
        if f.suffix == '.yml':
            files[f.name] = f.read_text(
                encoding='utf-8')
    if not files:
        print(
            f"[error] {deck_dir} 下没有找到 .yml 文件")
        sys.exit(1)
    payload = json.dumps(
        {'id': deck_id, 'files': files},
        ensure_ascii=False,
    ).encode('utf-8')
    return _post_json(
        f'{BASE_URL}/api/decks',
        payload,
        {
            'Content-Type': 'application/json',
            'X-Api-Key': api_key,
        },
    )


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
    api_key = _get_api_key()
    print(f"[upload] {deck_id} ({deck_dir}) ...")
    result = upload_deck(deck_id, deck_dir, api_key)
    token = result.get('access_token', '')
    share_url = (
        f'{BASE_URL}/?deck={deck_id}&token={token}'
    )
    print(f"[ok] {result.get('title')} "
          f"· {result.get('slide_count')} 页")
    print(f"[link] {share_url}")


if __name__ == '__main__':
    main()
