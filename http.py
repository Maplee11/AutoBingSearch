import requests
from bs4 import BeautifulSoup


def bing_search(query, username, password, user_agent):
    # 设置搜索请求的URL
    url = f"https://www.bing.com/search?q={query}"

    # 构建POST请求的数据
    data = {
        "username": username,
        "password": password
    }

    # 设置请求头部信息，包括 User-Agent
    headers = {
        "User-Agent": user_agent
    }

    # 发送POST请求，同时传递数据和请求头部信息
    response = requests.post(url, data=data, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML页面
        soup = BeautifulSoup(response.text, "html.parser")

        # 提取搜索结果的标题和链接
        search_results = soup.find_all("li", class_="b_algo")

        # 打印搜索结果
        for result in search_results:
            title = result.find("h2").text
            link = result.find("a")["href"]
            print(f"标题：{title}")
            print(f"链接：{link}")
            print()
    else:
        print("搜索请求失败")


# 调用函数进行搜索，同时传递账号信息和User-Agent
bing_search("Python programming", "2281683038@qq.com", "your_password",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
