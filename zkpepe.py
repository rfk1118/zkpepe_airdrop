import requests

def read_file_and_request(url, filename):
    # 读取文件中的每一行数据
    with open(filename, 'r') as file:
        lines = file.readlines()

    # 遍历每一行数据
    for line in lines:
        try:
        # 去除行尾的换行符
            line = line.strip().lower()
            # 构建请求的URL，将当前行的数据添加到URL中
            request_url = f"{url}/{line}.json"
            # 发送GET请求
            response = requests.get(request_url)

            # 检查响应的内容类型是否为HTML
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' in content_type:
                # 如果是HTML，打印0
                print(f"Data for {line}: 0")
            else:
                # 否则，打印实际的响应内容
                print(f"Data for {line}: {response.text}")
        except requests.RequestException as e:
            # 处理请求异常，打印错误信息
            print(f"Error for {line}: {e}")
            

if __name__ == "__main__":
    # 指定要请求的URL和包含数据的文件名
    api_url = "https://www.zksyncpepe.com/resources/amounts"
    data_filename = "a.txt"  # 替换为实际的文件名

    # 执行函数
    read_file_and_request(api_url, data_filename)
