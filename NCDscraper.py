import time
from selenium import webdriver
import chromedriver_binary # PATHを通す

driver = webdriver.Chrome()
driver.get('https://user.ncd.or.jp/member/memberLogin.html') # ページを立ち上げる
time.sleep(3)

# ログインIDを打つ
user_box = driver.find_element_by_name("user") # "user"という名前でフォームを認識する
user_box.send_keys('自身のログインIDを入力') 
pass_box = driver.find_element_by_name("password")
pass_box.send_keys('自身のパスワードを入力')

# ログインボタンをクリックする
driver.find_element_by_xpath("//input[@value='ログイン']").click()
time.sleep(3)

# 手術症例一覧をクリックする
driver.find_element_by_xpath("//input[@value='手術症例\u3000一覧']").click()
time.sleep(3)

# 結果を入れる配列を用意
from selenium.webdriver.common.by import By
facility = []
ncd = []
date = []
method = []
operator = []
status = []
df = []

# Tableを抽出してそれをページ数分繰り返す
for k in range(`ページ数-1を入力`): # 一度手動でログインしてページ数を確認する
  for i in range(10,30):
    table = driver.find_element_by_xpath("/html/body/form/div[3]")
    rows = table.find_elements(By.TAG_NAME, "tr")
    cols = rows[i].find_elements(By.TAG_NAME, "td")
    facility += [cols[0].text]
    ncd += [cols[1].text]
    date += [cols[2].text]
    method += [cols[3].text]
    operator += [cols[4].text]
    status += [cols[5].text]
    df = pd.DataFrame(data={'Facility': facility, 'NCD': ncd,
    'Date': date, 'Method': method, 'Operator': operator, 'Status': status},
    columns=['Facility', 'NCD', 'Date', 'Method', 'Operator', 'Status'])
  
  # 次ページをクリック  
  driver.find_element_by_link_text(u"次ページ").click()
  time.sleep(3)

df.to_csv('~/Desktop/NCD.csv', encoding='utf_8_sig')
