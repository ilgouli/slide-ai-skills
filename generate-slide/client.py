#!/usr/bin/env python3
# coding=utf-8
"""
slide-ai client — 上传/导出 deck

用法：
    python client.py <deck-id> [deck-dir]                # 上传
    python client.py export <分享链接|deck-id> [--out <目录>]  # 导出
    python client.py bind --user <username> [--passwd <password>]

参数：
    deck-id   deck 的唯一标识，如 mask-master-intro
    deck-dir  deck 目录路径，默认 decks/<deck-id>
    export    从分享链接导出 deck（YAML + 图片）到本地目录
    bind      绑定用户名密码，用于网页登录；--passwd 可省略（交互输入）

环境变量：
    SLIDE_AI_URL      服务地址，默认 http://slide.liamzheng.cn
    SLIDE_AI_API_KEY  API Key，未设置时自动注册并保存到
                      ~/.slide-ai/config.json
"""
import os
import sys
import json
import base64
import hashlib
import getpass
import argparse
import urllib.request
import urllib.error
from urllib.parse import urlparse, parse_qs, quote
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

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


def _get_json(url: str, headers: dict) -> dict:
    req = urllib.request.Request(
        url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {}    # deck 不存在，当作无已有 assets
        body = e.read().decode()
        print(f"[error] HTTP {e.code}: {body}")
        sys.exit(1)


IMAGE_EXTS = (
    '.png', '.jpg', '.jpeg',
    '.svg', '.gif', '.webp',
)
TEXT_EXTS = (
    '.md', '.json', '.yaml', '.yml',
)
MIME_MAP = {
    '.md': 'text/markdown',
    '.json': 'application/json',
    '.yaml': 'text/yaml', '.yml': 'text/yaml',
}
MAX_IMAGE_BYTES = 5 * 1024 * 1024   # 5 MB


def _scan_assets(assets_dir: Path):
    """扫描 assets/ 子目录，返回 [{name, path, sha256, mime}]"""
    out = []
    if not assets_dir.exists():
        return out
    for f in sorted(assets_dir.iterdir()):
        ext = f.suffix.lower()
        if ext not in IMAGE_EXTS + TEXT_EXTS:
            continue
        if not f.is_file():
            continue
        size = f.stat().st_size
        if size > MAX_IMAGE_BYTES:
            print(
                f"[warn] {f.name} 超过 5MB"
                f"（{size // 1024}KB），跳过")
            continue
        digest = hashlib.sha256(
            f.read_bytes()).hexdigest()
        if ext in IMAGE_EXTS:
            mime = f'image/{ext[1:]}'
        else:
            mime = MIME_MAP.get(ext, 'text/plain')
        out.append({
            'name': f.name, 'path': f,
            'sha': digest, 'mime': mime,
        })
    return out


def upload_deck(
        deck_id: str,
        deck_dir: Path,
        api_key: str) -> dict:
    # ① yml 从 deck 根目录扫
    files = {}
    for f in sorted(deck_dir.iterdir()):
        if f.suffix == '.yml':
            files[f.name] = f.read_text(
                encoding='utf-8')
    if not files:
        print(
            f"[error] {deck_dir} 下没有找到 .yml 文件")
        sys.exit(1)

    # ② 图片只从 assets/ 子目录扫
    assets_dir = deck_dir / 'assets'
    local_assets = _scan_assets(assets_dir)

    # ③ 查服务端已有 assets，增量比对
    headers = {'X-Api-Key': api_key}
    remote = _get_json(
        f'{BASE_URL}/api/decks/{deck_id}/assets/meta',
        headers,
    )
    remote_map = {
        a['name']: a['hash'] for a in remote
    } if isinstance(remote, list) else {}

    # ④ 只把变化的图 base64 进 payload
    assets = {}
    asset_names = []
    changed = 0
    for a in local_assets:
        asset_names.append(a['name'])
        if remote_map.get(a['name']) != a['sha']:
            raw = a['path'].read_bytes()
            assets[a['name']] = (
                f'data:{a["mime"]};base64,'
                + base64.b64encode(raw).decode())
            changed += 1

    if local_assets:
        print(
            f"[assets] {len(local_assets)} 张，"
            f"变化 {changed}，"
            f"未变 {len(local_assets) - changed}")
    payload = json.dumps(
        {
            'id': deck_id,
            'files': files,
            'assets': assets,
            'asset_names': asset_names,
        },
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


def _parse_share_url(url: str):
    """从分享链接或 deck id 提取 (deck_id, token)"""
    if url.startswith('http'):
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        deck_id = qs.get('deck', [None])[0]
        token = qs.get('token', [None])[0]
        if not deck_id:
            # 支持 /gallery/<id>/<page> 或 /<user>/<id>/<page>
            parts = [p for p in parsed.path.split('/') if p]
            if len(parts) >= 2:
                deck_id = parts[-2]
        if not deck_id:
            print(f"[error] 无法从 URL 提取 deck id: {url}")
            sys.exit(1)
        return deck_id, token
    # 直接传 deck id
    return url, None


def _fetch_deck(
        deck_id: str, token: str) -> dict:
    """GET /api/decks/{id}?token=... 返回 deck 详情（含 files）"""
    url = (
        f'{BASE_URL}/api/decks/{deck_id}'
        f'?token={token}' if token
        else f'{BASE_URL}/api/decks/{deck_id}')
    req = urllib.request.Request(url, method='GET')
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"[error] HTTP {e.code}: {body}")
        sys.exit(1)


def _scan_asset_refs(files: dict) -> list:
    """扫描所有 yml 里的 assets/<name> 引用，去重返回 name 列表"""
    if yaml is None:
        return []
    names = []
    seen = set()
    for fname, content in files.items():
        if not fname.endswith('.yml'):
            continue
        try:
            data = yaml.safe_load(content) or {}
        except yaml.YAMLError:
            continue
        refs = []
        if isinstance(data, dict):
            bg = data.get('background')
            if isinstance(bg, str):
                refs.append(bg)
            block = data.get('block')
            if isinstance(block, dict):
                src = block.get('src')
                if isinstance(src, str):
                    refs.append(src)
            for side in ('left', 'right'):
                side_b = data.get(side)
                if isinstance(side_b, dict):
                    src = side_b.get('src')
                    if isinstance(src, str):
                        refs.append(src)
            body = data.get('body')
            if isinstance(body, dict):
                src = body.get('src')
                if isinstance(src, str):
                    refs.append(src)
            rows = data.get('rows')
            if isinstance(rows, list):
                for row in rows:
                    items = (row or {}).get('items', [])
                    for item in items:
                        if isinstance(item, dict):
                            src = item.get('src')
                            if isinstance(src, str):
                                refs.append(src)
        for r in refs:
            if r.startswith('assets/') and r not in seen:
                seen.add(r)
                names.append(r)
    return names


def _download_asset(
        deck_id: str, ref: str, out_dir: Path) -> bool:
    """下载单张图片到 assets/ 子目录，返回是否成功"""
    name = ref.split('/')[-1]
    url = (
        f'{BASE_URL}/api/decks/{deck_id}/assets/'
        + quote(name))
    try:
        with urllib.request.urlopen(url) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        print(f"[warn] 下载失败 {ref}: HTTP {e.code}")
        return False
    assets_dir = out_dir / 'assets'
    assets_dir.mkdir(parents=True, exist_ok=True)
    (assets_dir / name).write_bytes(data)
    return True


def export_deck(
        deck_id: str, token: str, out_dir: Path):
    """从服务端拉取 deck（yml + 图片）导出到本地目录"""
    print(f"[export] {deck_id} → {out_dir} ...")
    data = _fetch_deck(deck_id, token)
    files = data.get('files', {})
    if not files:
        print(f"[error] deck {deck_id} 无文件")
        sys.exit(1)
    title = data.get('title', deck_id)

    out_dir.mkdir(parents=True, exist_ok=True)
    for fname, content in files.items():
        (out_dir / fname).write_text(
            content, encoding='utf-8')
    print(f"[export] {len(files)} 个 yml 文件")

    refs = _scan_asset_refs(files)
    if refs:
        ok = 0
        for ref in refs:
            if _download_asset(deck_id, ref, out_dir):
                ok += 1
        print(f"[export] {ok}/{len(refs)} 张图片")
    else:
        print("[export] 无本地图片引用")

    print(f"[ok] {title} 已导出到 {out_dir}")
    print(
        "提示：修改后可用 "
        f"'python {sys.argv[0]} {deck_id} {out_dir}'"
        " 重新上传")


def bind_account(username: str, password: str = ''):
    api_key = _get_api_key()
    if not password:
        password = getpass.getpass(
            "[bind] 设置密码（用于网页登录）: ")
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
        p = argparse.ArgumentParser(
            prog='client.py bind')
        p.add_argument(
            '--user', required=True,
            help='用户名')
        p.add_argument(
            '--passwd', default='',
            help='密码（省略时交互输入）')
        a = p.parse_args(sys.argv[2:])
        bind_account(a.user, a.passwd)
        return

    if sys.argv[1] == 'export':
        p = argparse.ArgumentParser(
            prog='client.py export')
        p.add_argument(
            'url', help='分享链接或 deck id')
        p.add_argument(
            '--out', default=None,
            help='导出目录，默认 decks/<deck-id>')
        a = p.parse_args(sys.argv[2:])
        deck_id, token = _parse_share_url(a.url)
        out_dir = Path(
            a.out if a.out else f'decks/{deck_id}')
        export_deck(deck_id, token, out_dir)
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
