#!/usr/bin/env python3
# coding=utf-8
"""
slide-ai client — 上传 deck 到 slide-ai 服务

用法：
    python client.py <deck-id> [deck-dir]
    python client.py bind <username>

参数：
    deck-id   deck 的唯一标识，如 mask-master-intro
    deck-dir  deck 目录路径，默认 decks/<deck-id>
    bind      绑定用户名密码，用于网页登录

环境变量：
    SLIDE_AI_URL      服务地址，默认 http://slide.liamzheng.cn
    SLIDE_AI_API_KEY  API Key，未设置时自动注册并保存到
                      ~/.slide-ai/config.json
"""
import os
import sys
import json
import getpass
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


def bind_account(username: str):
    api_key = _get_api_key()
    password = getpass.getpass(
        f"[bind] 设置密码（用于网页登录）: ")
    payload = json.dumps({
        'api_key': api_key,
        'username': username,
        'password': password,
    }, ensure_ascii=False).encode('utf-8')

    req = urllib.request.Request(
        f'{BASE_URL}/api/users/bind',
        data=payload,
        headers={'Content-Type': 'application/json'},
        method='POST')
    try:
        with urllib.request.urlopen(req) as resp:
            json.loads(resp.read())
        print(f"[bind] 完成，现在可用 {username} 登录网页")
        return
    except urllib.error.HTTPError as e:
        if e.code != 409:
            print(f"[error] HTTP {e.code}: "
                  f"{e.read().decode()}")
            sys.exit(1)

    # 用户名已存在，改用登录流程，获取该账号的 api_key
    print(f"[bind] 用户名已存在，尝试登录 {username} ...")
    login_payload = json.dumps({
        'username': username,
        'password': password,
    }, ensure_ascii=False).encode('utf-8')
    data = _post_json(
        f'{BASE_URL}/api/users/login',
        login_payload,
        {'Content-Type': 'application/json'},
    )
    new_key = data.get('api_key')
    if not new_key:
        print("[error] 登录失败，密码错误")
        sys.exit(1)
    config = _load_config()
    config['api_key'] = new_key
    _save_config(config)
    print(f"[bind] 已切换到账号 {username}，"
          f"api_key 已更新到 {_CONFIG_PATH}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    if sys.argv[1] == 'bind':
        if len(sys.argv) < 3:
            print("用法: python client.py bind <username>")
            sys.exit(1)
        bind_account(sys.argv[2])
        return

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
