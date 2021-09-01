import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 设置selenium使用chrome的无头模式
chrome_options = Options()
movieList = []

# chrome_options.add_argument('headless')  # 设置option,隐藏浏览器界面
# 在启动浏览器时加入配置
browser = webdriver.Chrome(
    r'C:\Users\XDH\PycharmProjects\seleniumfirst\venv\Scripts\chromedriver.exe',
    options=chrome_options)  # 获取chrome浏览器的驱动，并启动Chrome浏览器


# 对照页面布局，爬取页面数据
def get_movies_info_in_current_page():
    # a = browser.find_element_by_class_name("m-t-t")
    movie = browser.find_elements_by_class_name("recommend-movie")
    for m in movie:
        order = m.find_element_by_class_name("m-t-n")  # 排名
        name = m.find_element_by_class_name("m-t-t")  # 电影名
        r_m_info = m.find_element_by_class_name("r-m-info")
        score = r_m_info.find_element_by_class_name("score")  # 评分
        print(order.text + ":" + name.text + "\t" + score.text)
        info_detail = r_m_info.find_elements_by_class_name("info-detail")
        dire_info_l = info_detail[1].find_element_by_class_name("info-l")  # 第二个info-detail为导演信息
        dire = dire_info_l.find_element_by_class_name("info-value").text
        print("dire:" + dire)
        pub_info_m = info_detail[2].find_element_by_class_name("info-m")  # 第三个info-detail
        pub_time = pub_info_m.find_element_by_class_name("info-value").text
        print("pub-time:" + pub_time)
        info_t = info_detail[2].find_element_by_class_name("info-t")  # 第三个info-detail
        movie_time = info_t.find_element_by_class_name("info-value").text
        print("movie_time:" + movie_time)

    #
    # name = browser.find_elements_by_class_name("m-t-t")
    # # print(a.text)
    # for i in name:
    #     movieList.append(i.text)
    #     print(i.text)


browser.get('https://www.km.com/piandan/1912.html?page=1')
# 等待加载，最多等待20秒
browser.implicitly_wait(20)
browser.maximize_window()  # 窗口最大化
get_movies_info_in_current_page()
browser.execute_script("alert('浏览器将在3秒后自动关闭')")
time.sleep(3)
browser.quit()
