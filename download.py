# 下载文件
def download_file(url, path, name):
    p = Path(path) / name
    if p.exists():
        print('该文件已存在')
        return p
    try:
        r = requests.get(url)
        if not Path(path).exists():
            os.makedirs(path)
        with open(p, 'wb') as f:
            f.write(r.content)
    except requests.exceptions.ConnectionError:
        raise KeyError('文件下载失败')
    return p